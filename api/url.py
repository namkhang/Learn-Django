
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index),
    path('create/' , views.create),
    path('getdata/<str:id>' , views.getdata),
    path('deletedata/<str:id>' , views.deletedata),
    path('updatedata/' , views.updatedata),
]
