from store.forms import LoginForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CreateCheckoutSessionView
from .views import my_webhook_view
from django.conf.urls.static import static
from django.conf import settings


app_name = 'store'


urlpatterns = [
    path('', views.home, name="home"),
    # URL for Cart and Checkout
    path('ar-view',views.ar_view,name='ar_view'),
    path('webhook/stripe',my_webhook_view, name = 'webhook-stripe'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path("add-to-wishlist/", views.add_to_wishlist, name="add-to-wishlist"),
    path('remove-cart/<int:cart_id>/', views.remove_cart, name="remove-cart"),
    path('remove-wishlist/<int:wishlist_id>/', views.remove_wishlist, name="remove-wishlist"),
    path('plus-cart/<int:cart_id>/', views.plus_cart, name="plus-cart"),
    path('minus-cart/<int:cart_id>/', views.minus_cart, name="minus-cart"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('success/',views.success,name='success'),
    path('failure/', views.failure, name='failure'),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('orders/', views.orders, name="orders"),
    path('search/', views.search, name="search"),
    path('invoice/<int:orderID>/<int:productID>/', views.invoice, name='invoice'),
    path('query/', views.query, name='query'),
    path('newsletter/',views.newsletter, name = 'newsletter'),


    #URL for Products
    path('review/',views.Review_rate, name="review-rate"),
    path('product/<slug:slug>/', views.detail, name="product-detail"),
    path('categories/', views.all_categories, name="all-categories"),
    path('<slug:slug>/', views.category_products, name="category-products"),
    

    # URL for Authentication
    path('accounts/register/', views.RegistrationView.as_view(), name="register"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='account/login.html', authentication_form=LoginForm), name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/add-address/', views.AddressView.as_view(), name="add-address"),
    path('accounts/remove-address/<int:id>/', views.remove_address, name="remove-address"),
    path('logout_user', views.logout_user, name="logout"),

    path('accounts/password-change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html', form_class=PasswordChangeForm, success_url='/accounts/password-change-done/'), name="password-change"),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name="password-change-done"),

    path('accounts/password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html', form_class=PasswordResetForm, success_url='/accounts/password-reset/done/'), name="password-reset"), # Passing Success URL to Override default URL, also created password_reset_email.html due to error from our app_name in URL
    path('accounts/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name="password_reset_done"),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html', form_class=SetPasswordForm, success_url='/accounts/password-reset-complete/'), name="password_reset_confirm"), # Passing Success URL to Override default URL
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name="password_reset_complete"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
