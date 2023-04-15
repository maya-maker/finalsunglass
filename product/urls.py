from django.contrib import admin
from django.urls import path,include
from product.views import index,cart,add_to_cart,remove_from_cart,update_cart_item,chekout,payment_done

urlpatterns = [
    path('',index,name='index'),
    path('cart/',cart,name='cart'),
    path('cart/<int:id>',add_to_cart,name='cart'),
    path('cart/remove/<int:id>',remove_from_cart,name='removecart'),
    path('cart/update/<int:id>',update_cart_item,name='updatecart'),
    path('cart/checkout',chekout,name='checkout'),
    path('payment_done/', payment_done, name='payment_done'),
    # path('cart/payment',payment,name='payment'),

]