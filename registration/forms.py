# -*- coding: utf-8 -*-
import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User





class RegisterForm(forms.ModelForm):

	"""
		User Register Form
	"""

	def clean_username(self):

		"""
			Ensure that username is valid
		"""

		data = self.cleaned_data['username']

		if not re.match(r'(^[a-z0-9_-]+$)', data):
			raise ValidationError(_('Only Latin letters (both capital and lower case), underscore & dash authorized.'))

		users = User.objects.filter(username=data)

		if users :
			raise ValidationError(_('A user account with the username %s already exist.' % (data)))
		return data

	def clean_password_verified(self):

		password1 = self.cleaned_data['password']
		password2 = self.cleaned_data['password_verified']

		if not password2:
			raise ValidationError(_('You must confirm your password.'))
		if password2 != password1:
			raise ValidationError(_('Your passwords do not match.'))

	def clean_email(self):
		data = self.cleaned_data['email']

		users = User.objects.filter(email=data)
		if users :
			raise ValidationError(_('A user account with the user name %s already exist.' % (data)))

		return data


	email = forms.EmailField()

	password = forms.CharField()

	password_verified = forms.CharField()

	class Meta:
		model = User
		fields = ('username','password','email', 'last_login', 'date_joined')




class LoginForm(forms.Form):
	"""
		Login Form

		Username
		Password

	"""

	def clean_username(self):

		"""
			Ensure that username is correct.
		"""

		data = self.cleaned_data['username']
		users = User.objects.filter(username=data)
		if not users:
			raise ValidationError('Please give a valid username.')


		return data


	username = forms.CharField()


	password = forms.CharField()
