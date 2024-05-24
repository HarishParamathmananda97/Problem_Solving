from django.urls import path
from . import views

urlpatterns = [
    path('',views.myfunctioncall, name="index"),
    path('about',views.myfunctionabout, name="about"),
    path('add/<int:a>/<int:b>',views.myfunctionadd, name="add"),
    path('intro/<str:name>/<int:age>', views.intro, name="Intro")
]