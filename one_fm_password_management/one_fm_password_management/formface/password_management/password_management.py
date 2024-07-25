# -*- coding: utf-8 -*-
# Copyright (c) 2020, ONE FM and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import nxm, re
from nxm.model.document import Document
from nxm import _
from nxm.utils.password import get_decrypted_password, set_encrypted_password

class PasswordManagement(Document):
	def validate(self):
		self.validate_my_url(True)
		self.validate_strong_password()
		self.set_credentials_owner()

	@nxm.whitelist()
	def check_my_password_strength(self):
		if self.password:
			return get_password_strength(self.password)
		return False

	@nxm.whitelist()
	def validate_my_url(self, throw=False):
		if self.url:
			valid_url_schemes = ("http", "https")
			return nxm.utils.validate_url(self.url, throw=throw, valid_schemes=valid_url_schemes)

	def set_credentials_owner(self):
		if not self.credentials_owner:
			self.credentials_owner = self.owner

	def validate_strong_password(self):
		if self.password and self.ensure_strong_password:
			my_password = self.password
			if not self.is_new():
				my_password = get_decrypted_password(self.formface, self.name, 'password', raise_exception=True)
			self.password_strength = get_password_strength(my_password)
			if self.ensure_strong_password and self.password_strength != "Strong":
				nxm.throw(_("Password is not good, Include symbols, numbers, lowercase and uppercase letters in the password"))

	@nxm.whitelist()
	def generate_password(self):
		return create_new_password()

	@nxm.whitelist()
	def set_new_password(self, old_password, new_password):
		if get_decrypted_password(self.formface, self.name, 'password', raise_exception=True) == old_password:
			if self.ensure_strong_password and get_password_strength(new_password) != "Strong":
				nxm.throw(_("Password is not good, Include symbols, numbers, lowercase and uppercase letters in the password"))
			set_encrypted_password(self.formface, self.name, new_password, 'password')
			self.reload()
			return True
		else:
			nxm.msgprint(_("Old Password is not valid, please fill correct Old Password to Set New Password.!!"))
			return False

	@nxm.whitelist()
	def get_my_password(self):
		if check_user_exist_in_list(self):
			return get_decrypted_password(self.formface, self.name, 'password', raise_exception=True)
		else:
			nxm.throw(_("You have no permission to view the password."))

@nxm.whitelist()
def get_password_strength(pwd):
	# ref: https://www.codespeedy.com/check-the-password-strength-in-python/
	if(len(pwd)>=8):
		# must contain one digit similarly we say that for lowercase, uppercase and special characters
		if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})', pwd))==True):
			return 'Strong'
		elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})', pwd))==True):
			return 'Good'
	else:
		return 'Weak'

@nxm.whitelist()
def validate_url(url):
	regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

	if(bool(re.match(regex, url))==True):
		return True
	return False

@nxm.whitelist()
def create_new_password():
	import random
	str = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
	pwd = "".join(random.sample(str, 8))
	while get_password_strength(pwd) != "Strong":
		pwd = "".join(random.sample(str, 8))
	return pwd

def check_user_exist_in_list(doc):
	if doc.user_list:
		for user in doc.user_list:
			if user.user == nxm.session.user:
				return True
	return True if (nxm.session.user in ['Administrator', doc.credentials_owner]) else False
