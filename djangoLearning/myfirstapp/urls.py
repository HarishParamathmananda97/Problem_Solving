from django.urls import path
from . import views

urlpatterns = [
    path('',views.myfunctioncall, name="index"),
    path('about',views.myfunctionabout, name="about"),
    path('add/<int:a>/<int:b>',views.myfunctionadd, name="add"),
    path('intro/<str:name>/<int:age>', views.intro, name="Intro"),
    path('myfirstpage', views.myfirstpage, name = 'myfirstpage'),
    path('mysecondpage', views.mysecondpage, name = 'mysecondpage'),
    path('mythirdpage/<int:a>/<int:b>', views.mythirdpage, name = 'mythirdpage'),
    path('myimagepage', views.myimagepage, name='myimagepage'),
    path('myimagepage2', views.myimagepage2, name='myimagepage2'),
    path('myform', views.myform, name='myform'),
    path('mysubmittedform', views.mysubmittedform, name='mysubmittedform'),
    path('myform2', views.myform2, name='myform2'),
]