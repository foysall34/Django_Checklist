from django.urls import path
from .views import  AddictionListView , SelectAddictionView

urlpatterns = [

    path('addictions/', AddictionListView.as_view(), name='addiction-list'),
    path('addictions/select/', SelectAddictionView.as_view(), name='user-addiction-create'),
  
  
]
