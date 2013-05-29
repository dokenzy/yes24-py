# -*- coding: utf-8 -*-


def textstrip(f):
	'''return strippted text.'''
	def wrap(*args):
		return f(*args).strip()
	return wrap
	
def value_or_msg(val, msg='None'):
	'''return value or message'''
	if val:
		return val.group(0)
	else:
		return BOOK_MESSAGES[msg]

ERR_MESSAGES = {'bookId': 'This script requires yes24 book id.',
					'invalid_value': 'This book Id is not valid.',
					'unknown_error': 'Unknown Error is occured.'}
BOOK_MESSAGES = {'None': 'N/A'}