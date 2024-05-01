from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .rest_view import CustomUserViewSet, CustomerViewSet, PerformerViewSet, OrderViewSet

app_name = 'freelance'

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'performers', PerformerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('orders/', views.Orders.as_view(), name='orders'),
    path('orders/categories/<int:category_id>/', views.OrderCategoryPage.as_view(), name='order_category_page'),
    path('performers/', views.Performers.as_view(), name='performers'),
    path('api/', include(router.urls)),
]
