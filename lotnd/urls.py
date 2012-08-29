from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'lotnd.search.home', name='home'),
    url(r'^results$', 'lotnd.search.results', name='results'),
    # Examples:
    # url(r'^$', 'lotnd.views.home', name='home'),
    # url(r'^lotnd/', include('lotnd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
