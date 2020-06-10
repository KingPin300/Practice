"""
:usage: from pw_hash import *
"""
import hashlib

def is_pw(val1, val2):
	"""
	:def:
		check to see if a password and hash are the same.
	:param: str val1
		the password that you want check.
	:param: str val2
		the hashed password.
	:return: bool, int
		'True' or 'False' or '-1' if couldn't work.
	"""
	if (type(val1) is str) and (type(val2) is str):
		return val2 == hashlib.sha256(str.encode(val1)).hexdigest()
	return -1

def what_pw(val):
	"""
	:def:
		turn a password into a hashed string.
	:param: str val
		the password that you want to hash.
	:return: str, int
		'hash string of password' or '-1' if couldn't work.
	"""
	if type(val) is str:
		return hashlib.sha256(str.encode(val)).hexdigest()
	return -1
