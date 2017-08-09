from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.TodoView, name="Todo" ),
    url(r'^testing/',views.testing, name="testing"),
]