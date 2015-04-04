from django import template
import datetime
register = template.Library()

@register.filter
def sinceyear(val):

	YEAR_TOTAL_SECONDS = 31536000

	now = datetime.datetime.now(datetime.timezone.utc)
	print(val)
	print(now)

	if val:
		year = round((now - val).total_seconds() / YEAR_TOTAL_SECONDS)
		if year <= 0:
			return "less than a year"
		else:
			return "about " + str(year) + (" years" if year > 0 else " year")
	return "less than a year"