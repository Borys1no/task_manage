from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # HTML
    path('accounts/', include('accounts.urls')),
    path('task/', include('task.urls')),

    # API
    path('api/accounts/', include('accounts.api_urls')),
    path('api/', include('task.api_urls')),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
