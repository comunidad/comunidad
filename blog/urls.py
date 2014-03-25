from django.contrib import admin, url, include, patterns
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', RedirectView.as_view(url='/blog/')),
)