
from django.urls import path

from todoapp import views
app_name='todoapp'

urlpatterns = [
    path(' ',views.index, name='index'),

]
