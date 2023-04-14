from django.shortcuts import get_object_or_404, render,redirect
from .models import Category,Product
from django.http import HttpResponse



def index(request):
    category = Category.get_category()
    # product = None
    # product_count = product.count()
    categoryid = request.GET.get('categories')
    if categoryid:
        product = Product.get_all_product_by(categoryid)
        product_count = product.count()

    else:
        product = Product.get_all_product()
        product_count = product.count()

    data ={}
    data['product_count'] = product_count
    data['categories'] = category
    data['products']=product
    print(request.session.get('email'))
    return render(request,"shop-grid.html",data)

def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = 0
    for id, cart_item in cart.items():
        product = get_object_or_404(Product, id=id)
        cart_item['product'] = product
        cart_items.append(cart_item)
        cart_total += cart_item['price']
    cart_total_tax = cart_total+(cart_total*18)/100
    print(cart_item)
    return render(request, 'shoping-cart.html', {'cart_items': cart_items, 'cart_total': cart_total,'cart_total_tax':cart_total_tax})



def add_to_cart(request,id):
    product = get_object_or_404(Product, id=id)
    cart = request.session.get('cart', {})
    cart_item = cart.get(id)
    if cart_item:
        cart_item['quantity'] += 1
        cart_item['price'] = float(product.price) * float(cart_item['quantity'])
    else:
        cart[str(id)] = {'quantity': 1, 'price': float(product.price)}
    request.session['cart'] = cart
    return redirect('index')

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    print(cart)
    if str(id) in cart.keys():
        print(type(id))
        del cart[str(id)]
        request.session['cart'] = cart
        return redirect('cart')

def update_cart_item(request, id):
    product = get_object_or_404(Product, id=id)
    cart = request.session.get('cart', {})
    cart_item = cart.get(str(id))
    if cart_item:
        new_quantity = int(request.POST.get('quantity', 0))
        if new_quantity > 0:
            cart_item['quantity'] = new_quantity
            cart_item['price'] = float(product.price) * float(new_quantity)
        else:
            del cart[str(id)]
    request.session['cart'] = cart
    return redirect('cart')



def chekout(request):
    customer = request.session.get('customer')
    print(customer)
    if customer:
        cart = request.session.get('cart', {})
        cart_items = []
        cart_total = 0
        for id, cart_item in cart.items():
            product = get_object_or_404(Product, id=id)
            cart_item['product'] = product
            cart_items.append(cart_item)
            cart_total += cart_item['price']
        cart_total_tax = cart_total+(cart_total*18)/100
        context = {'cart_items':cart_items,'subtotal':cart_total,"total":cart_total_tax}    
        return render(request,'checkout.html',context)
    else:
        return redirect('cart')
