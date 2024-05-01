
from django.test import TestCase
from .models import CustomUser, Customer, Performer, OrderCategory, Status, Order
from django.utils import timezone
from .serializers import OrderSerializer


class ModelTests(TestCase):
    def test_user_creation(self):
        # Test creating a user
        user = CustomUser.objects.create_user(email='test@example.com', username='testuser', password='password')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')

        # Test creating a superuser
        superuser = CustomUser.objects.create_superuser(email='admin@example.com', username='admin', password='adminpassword')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_order_creation(self):
        # Create a Status instance with id 1 if it doesn't exist
        status, created = Status.objects.get_or_create(pk=1, defaults={'state': 1, 'caption': 'Default Status'})

        # Create a CustomUser instance
        user = CustomUser.objects.create_user(email='customer@example.com', username='customeruser',
                                              password='password')

        # Create a Customer instance associated with the CustomUser
        customer = Customer.objects.create(user=user)

        # Create an OrderCategory instance
        order_category = OrderCategory.objects.create(name='Test Category')

        # Create an Order instance with the associated customer, order category, and status
        order = Order.objects.create(customer=customer, title='Test Order', description='Test Description',
                                     order_category=order_category, status=status)

        # Assert the correctness of the created order
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
        # Create a CustomUser instance
        user = CustomUser.objects.create_user(email='test@example.com', username='testuser', password='password')

        # Create a Customer instance associated with the CustomUser
        customer = Customer.objects.create(user=user)

        # Create an OrderCategory instance
        order_category = OrderCategory.objects.create(name='Test Category')

        # Create a Status instance with id 1 if it doesn't exist
        status, created = Status.objects.get_or_create(pk=1, defaults={'state': 1, 'caption': 'Default Status'})

        # Prepare order data with the associated customer, order category, and status
        order_data = {
            'customer': customer.pk,
            'title': 'Test Order',
            'description': 'Test Description',
            'order_category': order_category.pk,
            'status': status.pk
        }

        # Create an OrderSerializer instance with the prepared data
        serializer = OrderSerializer(data=order_data)

        # Check if the serializer is valid
        self.assertTrue(serializer.is_valid())

        # Save the order instance
        order = serializer.save()

        # Assert the correctness of the saved instance's attributes
        self.assertEqual(order.title, 'Test Order')
        self.assertEqual(order.description, 'Test Description')
        self.assertEqual(order.order_category.name, 'Test Category')