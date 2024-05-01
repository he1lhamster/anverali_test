from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    ]

urlpatterns += [
    path('', include('freelance.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's auth URLs

    # path('accounts/register/', user_views.MyRegisterFormView.as_view(), name="register"),
]

