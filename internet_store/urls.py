from django.conf.urls import url

from internet_store import views

app_name = 'internet_store'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/', views.user),
    url(r'^courier/', views.courier),
    url(r'^product_type/', views.product_type),
    url(r'^product/', views.product),
    url(r'^marketing_source/', views.marketing_source),
    url(r'^street/', views.street),
    url(r'^region/', views.region),
    url(r'^generate/', views.generate),
    url(r'^reload_deliveries/', views.reload_deliveries),
    url(r'^delivery/', views.delivery)
]
