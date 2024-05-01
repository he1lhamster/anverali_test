from rest_framework.routers import DefaultRouter
from .rest_view import CustomUserViewSet, CustomerViewSet, PerformerViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'performers', PerformerViewSet)
router.register(r'orders', OrderViewSet)
