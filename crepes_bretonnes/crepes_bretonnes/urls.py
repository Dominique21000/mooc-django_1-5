#-*- coding : utf8 -*-
from blog import views
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#urlpatterns = [
    #url(r'admin/$', admin.site.urls),
#    url(r'accueil/$', 'blog.views.home'),
#]

urlpatterns = [
    url(r'^accueil/','blog.views.home'),
    url(r'^blog/', include('blog.urls'),)
    ]

urlpatterns += staticfiles_urlpatterns()