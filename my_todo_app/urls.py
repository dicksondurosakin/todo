# urls for my todo app
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('delete',views.delete_task,name='item_delete')
]