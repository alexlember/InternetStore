from django.conf.urls import url

from internet_store import views

app_name = 'internet_store'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/', views.user),
    url(r'^courier/', views.courier),
]
