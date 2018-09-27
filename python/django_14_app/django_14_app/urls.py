from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^polls/datetime', 'polls.views.current_datetime'),
    (r'^polls/templated', 'polls.views.templated_view'),
    (r'^polls/cached', 'polls.views.cached_templated_view'),
    # Examples:
    # url(r'^$', 'django_14_app.views.home', name='home'),
    # url(r'^django_14_app/', include('django_14_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)