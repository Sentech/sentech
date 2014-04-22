from django.db import models
#from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class UserProfile(models.Model):

	"""
		Definition of UserProfile Model.
	"""

	# link with django user

	user = models.OneToOneField(User)

	# other fields
	registration_complete = models.BooleanField(default=False)

	twitter_account = models.CharField(
		_('Twitter nickname'), max_length=16, default='', blank=True,
		validators=[
		RegexValidator(
			regex=r'("^$")|(^[A-Za-z0-9_]+$)',
			message='Please provide a valid Twitter handle.')])

	linkedin_url = models.URLField(
		_('LinkedIn profile url'), blank=True, null=False, default='',
		validators=[
		RegexValidator(
			regex=r'("^$")|(^http(s)?://(.*?)linkedin.com/)',
			message='Please provide a valid LinkedIn url.')])

	viadeo_url = models.URLField(
	_('Viadeo profile url'), blank=True, null=False, default='',
	validators=[
	RegexValidator(
		regex=r'("^$")|(^http(s)?://(.*?)viadeo.com/)',
		message='Please provide a valid LinkedIn url.')])

	facebook_url = models.URLField(
	_('Facebook profile url'), blank=True, null=False, default='',
	validators=[
	RegexValidator(
		regex=r'("^$")|(^http(s)?://(.*?)facebook.com/)',
		message='Please provide a valid Facebook url.')])

	personal_website_url = models.URLField(
	_('Personal website url'), blank=True, null=False, default='')

	resume = models.TextField(
	_('Resume'), blank=True, default='')

	gender = models.NullBooleanField(
	_('Gender'),
	choices=(
		(None, 'Gender'),
		(True, 'Female'),
		(False, 'Male')),
	default=None)

	def picture_upload_path(self, filename) :
		name = self.user.username
		fname, dot, extension = filename.rpartition('.')
		return 'profiles/%s.%s' % (name, extension)

	user_picture = models.FileField(
	_('Image profile'),
	upload_to=picture_upload_path,
	null=True,
	blank=True)

	def account_verified(self):
		if self.user.is_authenticated:
			result = EmailAddress.objects.filter(email=self.user.email)
			if len(result):
				return result[0].verified
		return False

	def __unicode__(self):
		return "{}'s profile".format(self.user.username)











