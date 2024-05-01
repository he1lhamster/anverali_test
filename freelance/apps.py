
from django.apps import AppConfig
from django.db import connection


def insert_data(truncate: bool = False):
    from freelance.models import CustomUser, Customer, Performer, Order, OrderCategory, Status
    # if truncate:
    #     Customer.objects.all().delete()
    #     Performer.objects.all().delete()
    #     CustomUser.objects.all().delete()
    #     Status.objects.all().delete()
    #     OrderCategory.objects.all().delete()
    #     Order.objects.all().delete()

    # Create order categories
    category1 = OrderCategory.objects.create(id=1, name='Category A')
    category2 = OrderCategory.objects.create(id=2, name='Category B')
    category3 = OrderCategory.objects.create(id=3, name='Category C')

    customer1 = CustomUser.objects.create(email='customer1@example.com', username='customer1', phone='123456789',
                                          user_type='customer')
    customer1.set_password('customer1')
    customer1.save()

    customer2 = CustomUser.objects.create(email='customer2@example.com', username='customer2', phone='987654321',
                                          user_type='customer')
    customer2.set_password('customer2')
    customer2.save()

    customer3 = CustomUser.objects.create(email='customer3@example.com', username='customer3', phone='555555555',
                                          user_type='customer')
    customer3.set_password('customer3')
    customer3.save()

    performer1 = CustomUser.objects.create(email='performer1@example.com', username='performer1',
                                           phone='111111111', user_type='performer')
    performer1.set_password('performer1')
    performer1.performers.first().categories.add(category1)
    performer1.save()

    performer2 = CustomUser.objects.create(email='performer2@example.com', username='performer2',
                                           phone='222222222',
                                           user_type='performer')
    performer2.set_password('performer2')
    performer2.performers.first().categories.add(category1, category2)
    performer2.save()

    performer3 = CustomUser.objects.create(email='performer3@example.com', username='performer3',
                                           phone='333333333',
                                           user_type='performer')
    performer3.set_password('performer3')
    performer3.performers.first().categories.add(category2, category3)
    performer3.save()

    performer4 = CustomUser.objects.create(email='performer4@example.com', username='performer4',
                                           phone='444444444',
                                           user_type='performer')
    performer4.set_password('performer4')
    performer4.performers.first().categories.add(category1, category2, category3)
    performer4.save()

    performer5 = CustomUser.objects.create(email='performer5@example.com', username='performer5',
                                           phone='555555555',
                                           user_type='performer')
    performer5.set_password('performer5')
    performer5.performers.first().categories.add(category3)
    performer5.save()

    # Create statuses
    status1 = Status.objects.create(id=1, state=1, caption='Создан')
    status2 = Status.objects.create(id=2, state=2, caption='Выполняется')
    status3 = Status.objects.create(id=3, state=3, caption='Исполнен')
    status4 = Status.objects.create(id=4, state=4, caption='Отменен')

    # Create orders
    order1 = Order.objects.create(customer=Customer.objects.get(user_id=customer1.id),
                                  performer=Performer.objects.get(user_id=performer1.id),
                                  description='Order 1 description', rate=0,
                                  status=status2, order_category=category1, title='Order 1 Title')
    order2 = Order.objects.create(customer=Customer.objects.get(user_id=customer1.id),
                                  performer=Performer.objects.get(user_id=performer2.id),
                                  description='Order 2 description', rate=0,
                                  status=status2, order_category=category2, title='Order 2 Title')
    order3 = Order.objects.create(customer=Customer.objects.get(user_id=customer2.id),
                                  performer=Performer.objects.get(user_id=performer1.id),
                                  description='Order 3 description', rate=0,
                                  status=status2, order_category=category3, title='Order 3 Title')
    order4 = Order.objects.create(customer=Customer.objects.get(user_id=customer2.id),
                                  performer=Performer.objects.get(user_id=performer2.id),
                                  description='Order 4 description', rate=5,
                                  status=status3, order_category=category1, title='Order 4 Title')
    order5 = Order.objects.create(customer=Customer.objects.get(user_id=customer3.id),
                                  description='Order 5 description', rate=0,
                                  status=status1, order_category=category2, title='Order 5 Title')
    order6 = Order.objects.create(customer=Customer.objects.get(user_id=customer3.id),
                                  performer=Performer.objects.get(user_id=performer3.id),
                                  description='Order 6 description', rate=0,
                                  status=status2, order_category=category3, title='Order 6 Title')
    order7 = Order.objects.create(customer=Customer.objects.get(user_id=customer3.id),
                                  performer=Performer.objects.get(user_id=performer4.id),
                                  description='Order 7 description', rate=0,
                                  status=status2, order_category=category1, title='Order 7 Title')
    order8 = Order.objects.create(customer=Customer.objects.get(user_id=customer3.id),
                                  performer=Performer.objects.get(user_id=performer4.id),
                                  description='Order 8 description', rate=10,
                                  status=status3, order_category=category2, title='Order 8 Title')
    order9 = Order.objects.create(customer=Customer.objects.get(user_id=customer3.id),
                                  performer=Performer.objects.get(user_id=performer5.id),
                                  description='Order 9 description', rate=3,
                                  status=status3, order_category=category3, title='Order 9 Title')
    order10 = Order.objects.create(customer=Customer.objects.get(user_id=customer3.id),
                                   description='Order 10 description', rate=0,
                                   status=status1, order_category=category1, title='Order 10 Title')


class FreelanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'freelance'

    def ready(self):
        from freelance.models import CustomUser
        if CustomUser._meta.db_table in connection.introspection.table_names() and CustomUser.objects.count() == 1:
            print('Insert Data')
            insert_data(truncate=False)
