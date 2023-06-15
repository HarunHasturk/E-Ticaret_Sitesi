from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Product,Slider,BestPrices,About,Special,Testimonial,Cart,CartProduct
from django.db.models import Sum
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.

def index(request):
    products = Product.objects.all().order_by('product_id')[:3]
    sliders = Slider.objects.all()
    bestprices = BestPrices.objects.all()
    about = About.objects.all()
    specials = Special.objects.all()
    testimonials = Testimonial.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            html = render_to_string('contactform.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message
            })

            send_mail('The contact form subject', 'This is the message', 'noreply@lodge.com', ['harunahmethasturk.10@gmail.com'], html_message=html)

            return redirect('home')

    else:
        form = ContactForm()
    context = {
        'products' : products,
        'sliders' : sliders,
        'bestprices' : bestprices,
        'about' : about,
        'specials' : specials,
        'testimonials' : testimonials,
        'form' : form
    }
    return render(request, "index.html", context)


def about(request):
    about = About.objects.all()
    context = {
        'about' : about
    }
    return render(request, "about.html", context)

def jewellery(request):
    products = Product.objects.all()
    bestprices = BestPrices.objects.all()
    context = {
        'products' : products,
        'bestprices' : bestprices
    }
    return render(request, "jewellery.html", context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            html = render_to_string('contactform.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message
            })

            send_mail('The contact form subject', 'This is the message', 'noreply@harunahmethasturk1.com', ['harunahmethasturk1@gmail.com'], html_message=html)

            return redirect('home')

    else:
        form = ContactForm()
    context = {
        'form' : form
    }
    return render(request, "contact.html", context)

def add_product(request, product_id):
    if request.method == "POST":
        cartCheck = Cart.objects.filter(user_id = request.user.id).count()
        if cartCheck == 0:
            newCart = Cart.objects.create(user_id = request.user.id)
        cart = Cart.objects.filter(user_id = request.user.id).first()
        productCheck = CartProduct.objects.filter(product_id = product_id, cart_id = cart.cart_id).count()

        if productCheck == 0:
            CartProduct.objects.create(product_id = product_id, cart_id = cart.cart_id, quantity=1)
        else:
            cartProduct = CartProduct.objects.filter(product_id = product_id, cart_id = cart.cart_id).first()
            cartProduct.quantity = cartProduct.quantity + 1
            cartProduct.save()
    return redirect('home')

def cart(request):
    cartTotal = 0
    shipping = 10
    cartCheck = Cart.objects.filter(user_id = request.user.id).count()
    if cartCheck == 0:
        newCart = Cart.objects.create(user_id = request.user.id)
    cart = Cart.objects.filter(user_id = request.user.id).first()
    cartproducts = CartProduct.objects.filter(cart_id = cart.cart_id).select_related()
    
    for cartProduct in cartproducts:
        cartTotal += float(cartProduct.product.product_price[1:]) * float(cartProduct.quantity)

    context = {
        'cartproducts' : cartproducts,
        'cartTotal' : cartTotal,
        'shipping' : shipping
    }
    return render(request, "cart.html", context)

def delete_cart_product(request, cart_product_id):
    if request.method == "POST":
        CartProduct.objects.filter(id = cart_product_id).delete()
    
    return redirect('cart')

def set_cart_product_quantity(request, cart_product_id):
    if request.method == "POST":
        data = request.POST
        set_type = data.get("setType")
        cartProduct = CartProduct.objects.get(id = cart_product_id)
        if set_type == 'decrease':
            if cartProduct.quantity == 1:
                CartProduct.objects.filter(id = cart_product_id).delete()
            else:
                cartProduct.quantity = cartProduct.quantity - 1
                cartProduct.save()
        else:
            cartProduct.quantity = cartProduct.quantity + 1
            cartProduct.save()
    
    return redirect('cart')

