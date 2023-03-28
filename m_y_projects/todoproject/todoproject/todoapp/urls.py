
from django.urls import path

from todoapp import views

app_name='todoapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),

    path('cbvhome/',views.Task_list_view.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Task_detail_view.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Task_Update.as_view(),name='cbvupdate'),


    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete')
]
