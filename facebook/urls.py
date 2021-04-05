from django.urls import path,include
from.import views

urlpatterns = [
    path('fb',views.fbFunction,name='fb'),
    path('calc',views.calcFunction,name='calc'),
]