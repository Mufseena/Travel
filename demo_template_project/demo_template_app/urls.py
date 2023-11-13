
from django.urls import path
from . import views

urlpatterns = [
    path ('',views.index,name='index'),
    path ('contact/',views.contact,name='contact'),
    path ('destination/',views.destination,name='destination'),
    path('element/', views.element, name='element'),
    path('news/', views.news, name='news'),

]