from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Sum, Avg
from django.dispatch import receiver
from django.utils import timezone
from enum import Enum
from django.db.models.signals import post_save, post_migrate

import freelance.apps


class UserType(Enum):
    ADMIN = 'admin'
    CUSTOMER = 'customer'
    PERFORMER = 'performer'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    reg_date = models.DateTimeField(default=timezone.now)
    user_type = models.CharField(max_length=20, choices=[(tag.value, tag.value) for tag in UserType])

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self._state.adding:
            super().save(*args, **kwargs)
            if self.user_type == 'customer':
                Customer.objects.create(user=self)
            elif self.user_type == 'performer':
                Performer.objects.create(user=self)
        else:
            super().save(*args, **kwargs)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Customer(models.Model):

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table = 'customer'

    user = models.ForeignKey(CustomUser, related_name='customers', on_delete=models.CASCADE)


class OrderCategory(models.Model):
    class Meta:
        verbose_name = 'Order category'
        verbose_name_plural = 'Order categories'
        db_table = 'order_category'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Performer(models.Model):
    class Meta:
        verbose_name = 'Performer'
        verbose_name_plural = 'Performers'
        db_table = 'performer'

    user = models.ForeignKey(CustomUser, related_name='performers', on_delete=models.CASCADE)
    total_rate = models.FloatField(default=0)
    categories = models.ManyToManyField(OrderCategory)
    orders_completed = models.IntegerField(default=0)

    def update_total_rate(self):
        self.total_rate = self.orders.filter(rate__gt=0).aggregate(average=Avg('rate'))['average'] or 0
        self.orders_completed = self.orders.filter(status__state=3).count()
        self.save()


class Status(models.Model):
    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
        db_table = 'status'

    state = models.IntegerField()
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Order(models.Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'freelance_order'

    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    performer = models.ForeignKey(Performer, related_name='orders', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    reg_date = models.DateTimeField(default=timezone.now)
    rate = models.IntegerField(null=True, default=0)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    order_category = models.ForeignKey(OrderCategory, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.performer:
            self.performer.update_total_rate()
