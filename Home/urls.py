from . import views
from django.urls import path
urlpatterns =[
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('events/',views.events, name='events'),
    path('teachers/',views.teachers, name='teachers'),
    path('teacherProfile/',views.teacherProfile,name='teacherProfile'),
    path('blog/',views.blog, name='blog'),
    path('contact/',views.contact, name='contact'),
    path('login/',views.login, name='login'),
    path('careers/',views.careers, name='careers'),
    path('register',views.register, name='register'),
]


