from django.conf.urls import url

from api import views


urlpatterns = [
    url(r'^variants/$', views.variant_list_view, name="variants")
]
