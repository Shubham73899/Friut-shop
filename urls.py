
from django.urls import path
from.views import *

urlpatterns = [
    path('',home,name="home"),
    path('product/<int:id>',product,name='product'),
    path('login/',login_user,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',logout_user,name='logout'),
    path('category/<int:id>',catgory,name='category'),
    path('about/',about , name='about'),
]
