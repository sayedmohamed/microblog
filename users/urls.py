from django.conf.urls.defaults import patterns, include, url



urlpatterns = patterns('microblog.users.views',
    url(r'^register/$', 'register', name='register'),
)
