from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from views import HomePageView

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'sentech.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomePageView.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),

    #url(r'^user/', include('registration.urls', namespace='registration')),

    url(r'^accounts/', include('allauth.urls')),

)
