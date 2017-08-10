from django.conf.urls import url
from todo.views import TodoClassView

urlpatterns = [
    url(r'^$', TodoClassView.as_view(), name="TodoClassView" ),
    # url(r'^testing/',views.testing, name="testing"),
]