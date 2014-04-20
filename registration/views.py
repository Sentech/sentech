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
