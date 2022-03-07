from django.urls import path,include
from.views import disp,func1,index,create,edit,update,delete,login,user_logout,home
urlpatterns=[
    path('tom/',disp),
    path('hari/',func1),
    path('index/',index),
    path('neeraja/',create),
    path("edit/<str:name>/",edit),
    path('update/<str:name>/',update),
    path('delete/<str:name>/',delete),
    path('login/',login),
    path('logout/',user_logout),
    path('',home),
    ]


