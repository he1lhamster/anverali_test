from models import User, Customer, Performer, OrderCategory, Status, Order
from django.utils import timezone

# Create users
customer1 = Customer.objects.create(email='customer1@example.com', username='customer1', phone='123456789', user_type='customer')
customer2 = Customer.objects.create(email='customer2@example.com', username='customer2', phone='987654321', user_type='customer')
customer3 = Customer.objects.create(email='customer3@example.com', username='customer3', phone='555555555', user_type='customer')

performer1 = Performer.objects.create(email='performer1@example.com', username='performer1', phone='111111111', user_type='performer')
performer2 = Performer.objects.create(email='performer2@example.com', username='performer2', phone='222222222', user_type='performer')
performer3 = Performer.objects.create(email='performer3@example.com', username='performer3', phone='333333333', user_type='performer')
performer4 = Performer.objects.create(email='performer4@example.com', username='performer4', phone='444444444', user_type='performer')
performer5 = Performer.objects.create(email='performer5@example.com', username='performer5', phone='555555555', user_type='performer')

# Create order categories
category1 = OrderCategory.objects.create(name='Category A')
category2 = OrderCategory.objects.create(name='Category B')
category3 = OrderCategory.objects.create(name='Category C')

# Create statuses
status1 = Status.objects.create(state=1, caption='Pending')
status2 = Status.objects.create(state=2, caption='Processing')
status3 = Status.objects.create(state=3, caption='Completed')

# Create orders
order1 = Order.objects.create(customer=customer1, performer=performer1, description='Order 1 description', rate=1, status=status1, order_category=category1)
order2 = Order.objects.create(customer=customer1, performer=performer2, description='Order 2 description', rate=7, status=status2, order_category=category2)
order3 = Order.objects.create(customer=customer2, performer=performer1, description='Order 3 description', rate=3, status=status2, order_category=category3)
order4 = Order.objects.create(customer=customer2, performer=performer2, description='Order 4 description', rate=5, status=status3, order_category=category1)
order5 = Order.objects.create(customer=customer3, performer=performer3, description='Order 5 description', rate=5, status=status3, order_category=category2)
order6 = Order.objects.create(customer=customer3, performer=performer3, description='Order 6 description', rate=8, status=status1, order_category=category3)
order7 = Order.objects.create(customer=customer3, performer=performer4, description='Order 7 description', rate=4, status=status2, order_category=category1)
order8 = Order.objects.create(customer=customer3, performer=performer4, description='Order 8 description', rate=10, status=status3, order_category=category2)
order9 = Order.objects.create(customer=customer3, performer=performer5, description='Order 9 description', rate=3, status=status1, order_category=category3)
order10 = Order.objects.create(customer=customer3, performer=performer5, description='Order 10 description', rate=6, status=status2, order_category=category1)
