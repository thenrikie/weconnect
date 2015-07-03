from django.db import models
from users.models import SubBusiness, Business, District
from authentication.models import User
from django.db.models import Q
from uniqid import models as UniqidModel
# Create your models here.



class Question(models.Model):
	TYPE = (
		('CheckboxSelectMultiple', 'CheckboxSelectMultiple'),
		('Select', 'Select'),
		('RadioSelect', 'RadioSelect'),
		('Text', 'Text')
	)

	sub_business = models.ForeignKey(SubBusiness)
	type = models.CharField(max_length=25, verbose_name='', choices=TYPE)
	text = models.CharField(max_length=512)
	desc_text = models.CharField(max_length=512, null=True, default=None, blank=True)
	rank = models.IntegerField(null=True, default=None, blank=True)
	tag = models.CharField(max_length=512, null=True, default=None, blank=True)

	def desc(self):
		return self.desc_text or self.text

	def __str__(self):
		return self.text + " <" + self.sub_business.business_set.first().name + ": " + self.sub_business.name + ">"


class QuestionOption(models.Model):
	
	question = models.ForeignKey(Question)
	text = models.CharField(max_length=512)

	def __str__(self):
		return self.text

def generateUniqid():
	return UniqidModel.generateCode(Project.objects.filter, 'uniqid')

class Project(models.Model):

	uniqid = models.CharField(max_length=UniqidModel.LENGTH, editable=False, unique=True, null=True)

	URGENCY = (
		('flexible', 'I can be flexible'),
		('asap', 'As soon as possible'),
		('week', 'Sometime this week'),
		('specific', 'Specific date')
	)

	CANCEL_REASON = (
		('no_help_needed', 'I no longer need help with this project'),
		('found_someone', 'I have found someone else to help me'),
		('no_right_candidate', 'The companies I was introduced to are not right for this project'),
		('other', 'Other')
	)

	TRAVEL = (
 		('anywhere', 'Anywhere in Hong Kong'),
 		('some_areas', 'Only some areas in Hong Kong'),
 		('no', 'I need the pro only to travel to me'),
	)

	business = models.ManyToManyField(Business)
	sub_business = models.ManyToManyField(SubBusiness)
	question_option = models.ManyToManyField(QuestionOption)


	urgency = models.CharField(max_length=25,
			verbose_name='When do you need this service?',
			choices=URGENCY,
			default='flexible'
	)

	specific_date = models.DateField(null=True, blank=True, verbose_name='Date')
	deadline = models.DateTimeField(null=True)
	user = models.ForeignKey(User)

	budget_lower = models.FloatField(blank=True, null=True)
	budget_upper = models.FloatField(blank=True, null=True)

	#to be deleted
	can_travel = models.BooleanField(default=False, verbose_name='I can travel to the pro')
	travel_to_pro = models.CharField(
		max_length=25, 
		verbose_name='I can travel to the pro',
		choices=TRAVEL,
		default='anywhere'
	)

	#to be deleted
	company_travel = models.BooleanField(default=False, verbose_name='They travel to me')

	travel_distance = models.ManyToManyField(District, related_name='project_travel_distance_set', blank=True)
	my_place = models.ForeignKey(District, related_name='my_place', verbose_name='I am located')

	desc = models.CharField(max_length=1024, blank=True, verbose_name='Anything else they should know')
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	cancelled = models.BooleanField(default=False)
	cancelled_reason = models.CharField(max_length=25, choices=CANCEL_REASON, null=True, default=None)
	cancelled_reason_other = models.CharField(max_length=1024, null=True, blank=True)

	def question_answers(self,question_id):
		return [a.id for a in self.question_option.filter(question=question_id)]

	def question_answer_texts(self,question_id):
		return [a.text for a in self.question_option.filter(question=question_id)]


	def question_answer_set(self):
		qas = [{ 'question' : q} for q in self.sub_business.first().question_set.filter(Q(tag__isnull=True) | Q(tag=''))]
		for qa in qas:
			qa['answer_texts'] = self.question_answer_texts(qa['question'].id)

		return qas

	def type_of_work(self):
		return self.get_question_by_tag('type_of_work')

	def type_of_service(self):
		return self.get_question_by_tag('type_of_service')

	def get_question_by_tag(self, tag):
		qa = {'question' : self.sub_business.first().question_set.get(tag=tag)}
		qa['answer'] = self.question_option.filter(question=qa['question'].id)

		return qa if qa['question'] else None

	def save(self, *args, **kwargs):
		if not self.uniqid:
			self.uniqid = generateUniqid()
		super(Project, self).save(*args, **kwargs)

	def __str__(self):
		return 'id: ' + str(self.id) + '; creator: ' + self.user.email + '; type: ' + self.sub_business.first().name

	def pitch_count(self):
		return self.pitch_set.exclude(state__in=['waiting', 'company_rejected']).count()

	def ready_pitch(self):
		return self.pitch_set.exclude(state__in=['waiting', 'company_rejected'])

	def waiting_pitch(self):
		return self.pitch_set.filter(state='waiting')

	def awarded(self):
		if self.pitch_set.filter(state='hired').count() > 0:
			return True
		return False

	def urgency_text(self):
		for u in self.URGENCY:
			if u[0] == self.urgency:
				return u[1]
		return "?"

	def travel_to_pro_text(self):
		for t in self.TRAVEL:
			if t[0] == self.travel_to_pro:
				return t[1]
		return "?"

	def unread_message_count(self):
		from pitches.models import Message
		return Message.objects.filter(read=False, pitch__project=self, recipient=self.user).count()

class QuestionAnswer(models.Model):
	text = models.CharField(max_length=512)
	project = models.ForeignKey(Project)
	question = models.ForeignKey(Question)

	def __str__(self):
		return self.text