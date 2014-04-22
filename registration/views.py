from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from registration.models import UserProfile
from registration.forms import LoginForm

from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def next(request):
  uri = ''
  next = ''
  action = request.get_full_path()
  next_sep = '/?next='
  if next_sep in action:
    uri = action.split('?next=')
    next= uri[1]
  else :
    next='/'

  if next[0] != '/':
    next = '/'+ next

  return next

def userLogin(request):
  redirect = ''
  redirect = next(request)

  if not request.user.is_authenticated():
    if request.method == 'POST':
      userlogin = LoginForm(request.POST)
      if userlogin.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
          login(request, user)
          messages.success(request, 'successfully login.')
          return HttpResponseRedirect(redirect)
      else:
        messages.error(request, 'Your username and/or password were incorrect.')
    else:
      userlogin =  LoginForm()
  else :
    messages.warning(request, 'You\'re already connected')
    return HttpResponseRedirect(redirect)

  return render_to_response('login.html', {'login': userlogin} ,context_instance=RequestContext(request))

def userRegister(request):
  redirect = ''
  redirect = next(request)

  if not request.user.is_authenticated():
    if request.method == 'POST':
      data = request.POST.copy()
      data['date_joined'] = datetime.today()
      data['last_login'] = datetime.now()
      userregister = RegisterForm(data)

      if userregister.is_valid():
        username = userregister.cleaned_data['username']
        email = userregister.cleaned_data['email']
        password = userregister.cleaned_data['password']
        user = User.objects.create_user(username, email, password)
        user_profile = UserProfile(user=user)
        user_profile.save()
        registed = authenticate(username=username, password=password)
        login(request, registed)
        return HttpResponseRedirect(redirect)
      else :
        messages.error(request, _('There\'re errors in the form! Thank you to correct before continuing'))
    else :
      userregister = RegisterForm()
  else :
    messages.warning(request, _('You\'re already connected'))
    return HttpResponseRedirect(redirect)

  return render_to_response('register.html', {'register': userregister} ,context_instance=RequestContext(request))


def profile(request, username=None):

  if request.user.is_authenticated():
    if username :
      user = get_object_or_404(User, username__iexact=username)
    else :
      user = request.user

    try :
      user.userprofile
    except ObjectDoesNotExist :
      user_profile = UserProfile(user=user)
      user_profile.save()
  else :
    messages.warning(request, 'Connectez vous pour voir les profils utilisateurs')
    return HttpResponseRedirect('/login')

  return render_to_response('auth/profile.html',{'pageuser': user, 'user_profile': user.userprofile}, context_instance=RequestContext(request))

