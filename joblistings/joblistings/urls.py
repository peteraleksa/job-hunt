from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'joblistings.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'search.views.home_page', name='home'),
    #url(r'^results/', 'search.views.results_page', name='results'),
    url(r'^admin/', include(admin.site.urls)),
)
