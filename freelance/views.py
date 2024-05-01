from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Customer, Performer, OrderCategory, Status, Order, CustomUser
from django.contrib.auth import get_user


def index(request):
    return render(request, 'index.html')


class Orders(TemplateView):
    template_name = 'orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()
        args = {
            'orders': orders,
        }
        context.update(args)
        return context


class OrderCategoryPage(TemplateView):
    template_name = 'order_category_page.html'

    def get_context_data(self, category_id, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.filter(order_category=category_id)
        args = {
            'orders': orders,
        }
        context.update(args)
        return context


class Performers(TemplateView):
    template_name = 'performers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        performers = Performer.objects.all()
        args = {
            'performers': performers,
        }
        context.update(args)
        return context


class Profile(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_categories = OrderCategory.objects.all()
        user = self.request.user

        if not user.id:
            orders = None
            profiler = None
        elif user.user_type == 'customer':
            profiler = Customer.objects.get(user=user)
            orders = Order.objects.filter(customer=profiler)
        elif user.user_type == 'performer':
            profiler = Performer.objects.get(user=user)
            orders = Order.objects.filter(performer=profiler)
        else:
            orders = None
            profiler = None

        args = {
            'order_categories': order_categories,
            'orders': orders,
            'profiler': profiler,
        }
        context.update(args)
        return context
