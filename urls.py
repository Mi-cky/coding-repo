
from django.urls import path
from . import views  

urlpatterns = [
    path('',views.home),
    path('signup(request)',views.signup),
    path('show.html',views.show),
    path('signup.html',views.signup),
    path('login.html',views.login_user,name='login'),
    path('about.asp',views.about),
    path('signout.html',views.signout),
]