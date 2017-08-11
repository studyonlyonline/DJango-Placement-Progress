from django.conf.urls import url
from todo.views import TodoClassView, TestingClassView

app_name = 'todo'

urlpatterns = [
    url(r'^$', TodoClassView.as_view(), name="TodoClassView" ),
    url(r'^test/$', TestingClassView.as_view(), name="TestingClassView" ),
    # url(r'^testing/',views.testing, name="testing"),
]