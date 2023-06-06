

from django.urls import path
from main_app import views

urlpatterns = [
    path('',views.home,name='main_app-home'),
    path('add/',views.add,name='main_app-add'),
    path('delete/<int:id>',views.delete,name='main_app-delete'),
    path('edit/<int:id>',views.edit,name='main_app-edit'),
    path('delete-all',views.delete_all,name="main_app-deleteall"),
    path('markcomplete/<int:id>',views.markcomplete ,name='main_app-markcomplete'),
    path('404/',views.not_found,name='main_app-404')
]
