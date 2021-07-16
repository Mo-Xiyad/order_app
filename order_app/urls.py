from django.contrib import admin
from django.urls import path, include
from flower import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),  # new
    path('', views.landing_page, name='landing_page'),
    path('order', views.order, name='order'),
    path('multiple_order', views.multiple_order, name='multiple_order'),
    path('edit_order/<int:pk>', views.edit_order, name='edit_order'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('product_page', views.product_page, name='product_page'),
    path('slected_item/<int:product_pk>', views.slected_item, name='slected_item'),
]
