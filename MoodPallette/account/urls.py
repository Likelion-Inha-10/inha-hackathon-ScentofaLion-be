from django.contrib import admin
from django.urls import path
from account import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('/', views.test),
    path('login/', csrf_exempt(views.login.as_view())),
    path('logout/', views.logout),
    path('signup/', csrf_exempt(views.signup.as_view())),
    path('<int:userId>/', csrf_exempt(views.account_API.as_view())),
]
