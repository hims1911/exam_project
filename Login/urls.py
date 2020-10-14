from django.urls import path
from .import views

urlpatterns =[
    path('exams',views.exams,name='start_test'),
    path('registration',views.registration,name='register'),
    path('',views.login ,name ="Login") ,
    path('logout',views.logout,name='logout'),
    path('instruction',views.PostForm, name="instruction"),
    path('submit',views.submit,name='submit'),
    path('technical' ,views.technical,name='technical') ,
    path('timer',views.timer,name='timer')
]