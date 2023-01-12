from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('del/<int:id>/', views.rem, name='remo'),
    path('addnew/', views.addNew, name='addNewCourse'),
    path('save/', views.save, name='save'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update')
]
#this is urls.py