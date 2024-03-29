from django.contrib import admin
from django.urls import path
from product import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('red/', csrf_exempt(views.red.as_view())),
    path('yellow/', csrf_exempt(views.yellow.as_view())),
    path('green/', csrf_exempt(views.green.as_view())),
    path('blue/', csrf_exempt(views.blue.as_view())),
    path('black/', csrf_exempt(views.black.as_view())),
    path('white/', csrf_exempt(views.white.as_view())),
    path('purple/', csrf_exempt(views.purple.as_view())),
    path('<int:userId>/', csrf_exempt(views.getuser.as_view())),
    path('getColor/', csrf_exempt(views.getColor.as_view())),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
