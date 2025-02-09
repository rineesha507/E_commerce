from django.urls import path,include
from .views import ProductViewSet, CategoryViewSet,RegisterView,LoginView

from rest_framework.routers import DefaultRouter
# from .views import LoginAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
        path('', include(router.urls)),
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('api/auth/register/', RegisterView.as_view(),name='auth_register'),
        path('api/auth/login/', LoginView.as_view(),name='auth_login')

        

]
