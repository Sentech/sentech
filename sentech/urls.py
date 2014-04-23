from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from views import HomePageView

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'sentech.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #admin page
    url(r'^admin/', include(admin.site.urls)),

    # homepage
    url(r'^$', HomePageView.as_view(), name='home'),

    #accounts
    url(r'^accounts/', include('allauth.urls')),

    #planets
    url(r'^planet/', include('planet.urls')),
)
