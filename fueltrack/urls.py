from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import RegisterView, MeView

urlpatterns=[
 path('admin/',admin.site.urls),
 path('api/auth/register/',RegisterView.as_view()),
 path('api/auth/login/',TokenObtainPairView.as_view()),
 path('api/auth/refresh/',TokenRefreshView.as_view()),
 path('api/auth/me/',MeView.as_view()),
 path('api/',include('stations.urls')),
]
