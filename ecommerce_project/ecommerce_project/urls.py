from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('reviews/', include('reviews.urls')),
    path('', home, name='home'),  # Add the home URL pattern
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)