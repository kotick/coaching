from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Clases.views.index', name='index'),
    url(r'^index$', 'Clases.views.index', name='index'),
    url(r'^QuienesSomos$', 'Clases.views.quienessomos', name='quienessomos'),
    url(r'^ComoFunciona$', 'Clases.views.comofunciona', name='comofunciona'),
    url(r'^Inscribete$', 'Clases.views.inscribete', name='inscribete'),
    url(r'^Profesor$', 'Clases.views.profesor', name='profesor'),
    url(r'^logout$', 'Clases.views.logout_view', name='logout'),
    url(r'^login$', 'Clases.views.login_view', name='login_view'),
    url(r'^crear/usuario$', 'Clases.views.crear_usuario', name='crear_usuario'),
    # url(r'^$', 'Coaching.views.home', name='home'),
    # url(r'^Coaching/', include('Coaching.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
