from django.contrib import admin
from django.urls import path,include
from product.views import index,cart,add_to_cart,remove_from_cart,update_cart_item,chekout,process_payment

urlpatterns = [
    path('',index,name='index'),
    path('cart/',cart,name='cart'),
    path('cart/<int:id>',add_to_cart,name='cart'),
    path('cart/remove/<int:id>',remove_from_cart,name='removecart'),
    path('cart/update/<int:id>',update_cart_item,name='updatecart'),
    path('cart/checkout',chekout,name='checkout'),
    path('checkout/',chekout, name='checkout'),
    path('process_payment/',process_payment, name='process_payment'),

]