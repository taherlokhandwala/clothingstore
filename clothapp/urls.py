from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from clothing import settings
from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('shop/<str:category>', views.category_page, name="category_page"),
    path('shop/<str:category>/<int:p_id>',
         views.product_page, name="product_page"),
    path('account/signup', views.signup_page, name="signup_page"),
    path('account/login', views.login_page, name="login_page"),
    path('account/logout', views.logout_user, name="logout_user"),
    path('account/cart', views.cart_page, name="cart_page"),
    path('account/address', views.saved_addresses_page,
         name="saved_addresses_page"),
    path('account/shipping', views.shipping_page,
         name="shipping_page"),
    path('account/orders', views.orders_page,
         name="orders_page"),
    path('account/edit', views.edit_profile_page,
         name="edit_profile_page"),
    path('payment/', views.payment_page,
         name="payment_page"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
