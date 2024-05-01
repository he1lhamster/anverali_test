
from django.test import TestCase
from .models import CustomUser, Customer, Performer, OrderCategory, Status, Order
from .serializers import OrderSerializer


class ModelTests(TestCase):
    def test_user_creation(self):
        user = CustomUser.objects.create_user(email='test@example.com', username='testuser', password='password')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')

        superuser = CustomUser.objects.create_superuser(email='admin@example.com', username='admin', password='adminpassword')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_order_creation(self):
        status, created = Status.objects.get_or_create(pk=1, defaults={'state': 1, 'caption': 'Default Status'})

        user = CustomUser.objects.create_user(email='customer@example.com', username='customeruser',
                                              password='password')

        customer = Customer.objects.create(user=user)

        order_category = OrderCategory.objects.create(name='Test Category')

        order = Order.objects.create(customer=customer, title='Test Order', description='Test Description',
                                     order_category=order_category, status=status)

        self.assertEqual(order.title, 'Test Order')
        self.assertEqual(order.description, 'Test Description')
        self.assertEqual(order.order_category.name, 'Test Category')


class ViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class SerializerTests(TestCase):
    def test_order_serializer(self):
        user = CustomUser.objects.create_user(email='test@example.com', username='testuser', password='password')

        customer = Customer.objects.create(user=user)

        order_category = OrderCategory.objects.create(name='Test Category')

        status, created = Status.objects.get_or_create(pk=1, defaults={'state': 1, 'caption': 'Default Status'})

        order_data = {
            'customer': customer.pk,
            'title': 'Test Order',
            'description': 'Test Description',
            'order_category': order_category.pk,
            'status': status.pk
        }

        serializer = OrderSerializer(data=order_data)

        self.assertTrue(serializer.is_valid())

        order = serializer.save()

        self.assertEqual(order.title, 'Test Order')
        self.assertEqual(order.description, 'Test Description')
        self.assertEqual(order.order_category.name, 'Test Category')