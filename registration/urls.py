from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # login - register

    url(r'^login/$', 'registration.views.userLogin', name='userLogin'),
    url(r'^register/$', 'registration.views.userRegister', name='userRegister'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),

)
