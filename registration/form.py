# -*- coding: utf-8 -*-
import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime





class RegisterForm(forms.ModelForm):

  """
    User Register Form
  """

  def _clean_names(self, data):

    """
          Ensure that data is valid.

      Variable data can contain only Latin letters (both capital and
      lower case), spaces and the character '.
    """

    if not re.match(r'(^[A-Za-z\' ]+$)', data):
      raise ValidationError('Seul les caractéres latins sont utilisés.')

    return data

  def clean_username(self):
    """ Ensure that username is valid """

    data = self.cleaned_data['username']
    if not re.match(r'(^[a-z0-9_-]+$)', data):
      raise ValidationError('Seul les caractéres latins sont utilisés.')

    users = User.objects.filter(username=data)

    if users :
      raise ValidationError( u"Un compte utilisateur avec le nom d'utilisateur %s existe déjà" % (data))

    return data

  def clean_password_verified(self):
    password1 = self.cleaned_data['password']
    password2 = self.cleaned_data['password_verified']

    if not password2:
      raise ValidationError('Vous devez confirmer votre mot de passe')
    if password2 != password1:
      raise ValidationError('Vos mots de passe ne correspondents pas')

  def clean_email(self):
    data = self.cleaned_data['email']

    users = User.objects.filter(email=data)
    if users :
      raise ValidationError( u"Un compte utilisateur avec l'email %s existe déjà" % (data))

    return data


  email = forms.EmailField(_('Votre email'))

  #today = datetime.today()
  #last_login = forms.DateField(default=today)
  #date_joined = forms.DateField(default=today)

  password = forms.CharField(_('Mot de passe'),
    widget=forms.PasswordInput(attrs={'class':'large'}),
    required='True',
    error_messages={'required':_('Merci de donner un mot de passe')}
    )

  password_verified = forms.CharField(_('Retapez votre mot de passe'),
    widget=forms.PasswordInput(attrs={'class':'large'}),
    required='True',
    error_messages={'required':_('Merci de confirmer votre mot de passe')})

  class Meta:
    model = User
        fields = ('username','password','email', 'last_login', 'date_joined')




class LoginForm(forms.Form):
  """
    Formulaire de connexion

    Nom d'utilisateur
    Mot de passe

  """

  def clean_username(self):

    """ Ensure that username is correct """

    data = self.cleaned_data['username']
    users = User.objects.filter(username=data)
    if not users:
      raise ValidationError('Please give a valid username.')

    return data


  username = forms.CharField(_('User name'),
    widget=forms.TextInput(),
    required='True',
    error_messages={'required':_("Username required")})


  password = forms.CharField(_('Mot de passe'),
    widget=forms.PasswordInput(),
    required='True',
    error_messages={'required':_('Merci de donner un mot de passe')})

