from django.conf.urls import url

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'data/', views.Data.as_view()),
]


urlpatterns += staticfiles_urlpatterns()