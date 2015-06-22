from django.db import models
from random import randrange
# Example set is Crockford's encoding:
# http://www.crockford.com/wrmg/base32.html
CHARSET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
LENGTH = 16
MAX_TRIES = 1024

# Create your models here.
def generateCode(check_query,uniqid_field_name):
	"""
	Upon saving, generate a code by randomly picking LENGTH number of
	characters from CHARSET and concatenating them. If code has already
	been used, repeat until a unique code is found, or fail after trying
	MAX_TRIES number of times. (This will work reliably for even modest
	values of LENGTH and MAX_TRIES, but do check for the exception.)
	Discussion of method: http://stackoverflow.com/questions/2076838/
	"""
	loop_num = 0
	unique = False
	while not unique:
		if loop_num < MAX_TRIES:
			new_code = ''
			for i in range(LENGTH):
				new_code += CHARSET[randrange(0, len(CHARSET))]
				kwargs = { uniqid_field_name: new_code }
			if not check_query(**kwargs):
				unique = True
			loop_num += 1
		else:
			raise ValueError("Couldn't generate a unique code.")

	return new_code