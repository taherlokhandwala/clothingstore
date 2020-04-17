from django.shortcuts import render, redirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


from .forms import CreateUserForm, NewAddressForm, EditUser
from .models import Product, Cart, Address, Order

import uuid

# payment related
import stripe
stripe.api_key = "sk_test_GtDG0cn5a7hN7JmwlrguIUma00nuYEXvKc"

# Create your views here.

SIZE_CHART_MEN = [("Size", "Chest(in)", "Front Length(in)", "Across Shoulder(in)"), ("XS", 35.5, 25.1, 15.4), ("S", 37.0,
                                                                                                               25.8, 15.8), ("M", 38.5, 26.5, 16.3), ("L", 40.0, 27.3, 17.0), ("XL", 41.8, 28.0, 17.8), ("XXL", 43.0, 28.8, 18.5)]
SIZE_CHART_WOMEN = [("Size", "Bust(in)", "Waist(in)", "Hips(in)",
                     "Across Shoulder(in)", ""), ("XS", 34.5, 31.0, 42.0, 13.5), ("S", 36.5, 33.0, 44.0, 14.0), ("M", 38.5, 35.0, 46.0, 14.5), ("L", 40.5, 37.0, 48.0, 15.0), ("XL", 42.5, 39.0, 50.0, 15.5), ("XS", 44.5, 41.0, 52.0, 16.0)]
SIZE_CHART_KIDS = [("Size", "Years"), ("XS", "0-2Y"), ("S", "2-4Y"),
                   ("M", "4-6Y"), ("L", "6-8Y"), ("XL", "8-10Y"), ("XXL", "10-12Y")]


def home_page(request):
    context = {}
    return render(request, "home_page.html", context)


def category_page(request, category):
    product_display = Product.objects.filter(category=category)
    if product_display:
        context = {"products": product_display, "category": category}
        return render(request, "category_page.html", context)
    else:
        error_message = "Category Doesn't Exist."
        return render(request, 'error_page.html', {"error": error_message})


def product_page(request, category, p_id):

    if request.method == "POST":
        if request.user.is_authenticated:
            size_selected = request.POST.get("size")
            user_cart_items = Cart.objects.filter(
                customer_user_name=request.user)

            for item in user_cart_items:
                if item.product_size == size_selected and item.product_id == p_id:
                    messages.info(request, "Item already in cart.")
                    return redirect(f'/shop/{category}/{p_id}')

            item = Product.objects.get(pk=p_id)

            cart_item = Cart(
                product_id=p_id, customer_user_name=request.user, product_size=size_selected, brand=item.brand, description=item.description, price=item.price, category=category, image_source=item.image_main.url)

            cart_item.save()
            messages.info(request, "Item Added")
            return redirect(f'/shop/{category}/{p_id}')
        else:
            messages.info(request, "Please Login To Add To Cart.")
            return redirect('login_page')

    try:
        item = Product.objects.get(pk=p_id)
        if item.category != category:
            error_message = "Item Doesn't Exist."
            return render(request, "error_page.html", {"error": error_message})

        image_urls = [item.image_main.url]
        sizes = []
        size_chart = []

        if item.image_2:
            image_urls.append(item.image_2.url)
        if item.image_3:
            image_urls.append(item.image_3.url)
        if item.image_4:
            image_urls.append(item.image_4.url)
        if item.image_5:
            image_urls.append(item.image_5.url)

        if item.size_xs:
            sizes.append("XS")
        if item.size_s:
            sizes.append("S")
        if item.size_m:
            sizes.append("M")
        if item.size_l:
            sizes.append("L")
        if item.size_xl:
            sizes.append("XL")
        if item.size_xxl:
            sizes.append("XXL")

        if category == "Men":
            headers = SIZE_CHART_MEN[0]
            for x in SIZE_CHART_MEN[1:]:
                if x[0] in sizes:
                    size_chart.append(x)
        elif category == "Women":
            headers = SIZE_CHART_WOMEN[0]
            for x in SIZE_CHART_WOMEN[1:]:
                if x[0] in sizes:
                    size_chart.append(x)
        elif category == "Kid":
            headers = SIZE_CHART_KIDS[0]
            for x in SIZE_CHART_KIDS[1:]:
                if x[0] in sizes:
                    size_chart.append(x)

        context = {"image_urls": image_urls, "sizes": sizes,
                   "product": item, "size_chart": size_chart, "headers": headers}

        return render(request, "product_page.html", context)
    except ObjectDoesNotExist:
        error_message = "Item Doesn't Exist."
        return render(request, 'error_page.html', {"error": error_message})


def signup_page(request):

    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect("login_page")
        else:
            errors = form.errors
            form = CreateUserForm()
            context = {"form": form, "error": errors}
            return render(request, "signup_page.html", context)

    form = CreateUserForm()
    context = {"form": form}
    return render(request, "signup_page.html", context)


def login_page(request):

    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == "POST":
        username = (request.POST.get("username")).strip()
        password = (request.POST.get("password")).strip()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, "Invalid username or password")
            return render(request, "login_page.html", {})

    return render(request, "login_page.html", {})


@login_required(login_url='login_page')
def logout_user(request):
    logout(request)
    return redirect("login_page")


@login_required(login_url='login_page')
def cart_page(request):

    cart_items = Cart.objects.filter(customer_user_name=request.user)

    if request.method == "POST":
        product_id = request.POST.get("primary_key")
        product_size = request.POST.get("product_size")
        for item in cart_items:
            if ((str(item.product_id) == product_id) and (item.product_size == product_size)):
                item.delete()
                break
        return redirect('cart_page')

    item_count = len(cart_items)
    total = 0
    for product in cart_items:
        total += product.price

    context = {"items": cart_items, "total": total,
               "count": item_count}
    return render(request, "cart_page.html", context)


@login_required(login_url='login_page')
def saved_addresses_page(request):

    if request.method == "POST":
        if request.POST.get("delete-address") == "delete-address":
            address_id = request.POST.get("address-id")
            instance = Address.objects.get(pk=address_id)
            instance.delete()
            return redirect('saved_addresses_page')
        else:
            new_address = NewAddressForm(request.POST)
            if new_address.is_valid():
                instance = Address(name=new_address.cleaned_data["name"], mobile=new_address.cleaned_data["mobile"], pin_code=new_address.cleaned_data["pin_code"], state=new_address.cleaned_data["state"],
                                   address=new_address.cleaned_data["address"], locality=new_address.cleaned_data["locality"], city=new_address.cleaned_data["city"], customer_user_name=request.user)
                instance.save()
                return redirect('saved_addresses_page')
    new_address_form = NewAddressForm()
    addresses = Address.objects.filter(customer_user_name=request.user)
    address_count = len(addresses)
    context = {"addresses": addresses,
               "form": new_address_form, "count": address_count}
    return render(request, "saved_addresses_page.html", context)


address = ""
order_id = 0
user_global = ""
total_bill_amount = 0
@login_required(login_url='login_page')
def shipping_page(request):

    addresses = Address.objects.filter(customer_user_name=request.user)
    cart_items = Cart.objects.filter(customer_user_name=request.user)

    if request.method == "POST":
        if request.POST.get("new-address") == "new-address":
            new_address = NewAddressForm(request.POST)
            if new_address.is_valid():
                instance = Address(name=new_address.cleaned_data["name"], mobile=new_address.cleaned_data["mobile"], pin_code=new_address.cleaned_data["pin_code"], state=new_address.cleaned_data["state"],
                                   address=new_address.cleaned_data["address"], locality=new_address.cleaned_data["locality"], city=new_address.cleaned_data["city"], customer_user_name=request.user)
                instance.save()
                return redirect('shipping_page')
        else:
            address_id = request.POST.get("shipping-address")
            if address_id:

                global address
                global order_id
                global user_global
                global total_bill_amount
                address = Address.objects.get(pk=address_id)
                order_id = uuid.uuid4().node
                total_bill_amount = 0
                for product in cart_items:
                    total_bill_amount += product.price

                user_global = request.user
                return render(request, "payment_page.html", {"total": total_bill_amount, "order_id": order_id})
            else:
                messages.info(request, "Please select an address")
                return redirect('shipping_page')

    new_address_form = NewAddressForm()
    count = len(cart_items)
    context = {"form": new_address_form,
               "addresses": addresses}
    if count:
        return render(request, "shipping_page.html", context)
    else:
        return redirect('cart_page')


def payment_page(request):

    if request.method == "POST":
        global user_global
        global order_id
        global address
        try:
            customer = stripe.Customer.create(
                name=user_global,
                source=request.POST.get("stripeToken")
            )

            charge = stripe.Charge.create(
                customer=customer,
                amount=total_bill_amount*100,
                currency="inr",
                description=f"Clothing store order - {order_id}",
            )
            if charge.status == 'succeeded':
                cart_items = Cart.objects.filter(
                    customer_user_name=user_global)
                for item in cart_items:
                    instance = Order(brand=item.brand, description=item.description,
                                     price=item.price, customer_user_name=user_global, image_source=item.image_source, name=address.name, mobile=address.mobile, pin_code=address.pin_code, state=address.state, city=address.city, locality=address.locality, address=address.address, order_id=order_id)
                    instance.save()
                    item.delete()
                return render(request, "order_placed_page.html", {"status": True})
            else:
                return render(request, "order_placed_page.html", {"status": False})

        except stripe.error.CardError:
            return render(request, "order_placed_page.html", {"status": False})


@login_required(login_url='login_page')
def orders_page(request):
    orders = Order.objects.filter(customer_user_name=request.user)
    context = {"orders": orders}
    return render(request, "orders_page.html", context)


@login_required(login_url='login_page')
def edit_profile_page(request):

    if request.method == "POST":
        if request.POST.get("change-name") == "change-name":
            edit_user_form = EditUser(
                request.POST, instance=request.user)
            if edit_user_form.is_valid():
                edit_user_form.save()
                return redirect('home_page')
            else:
                messages.info(request, "Invalid Details")
                return redirect('edit_profile_page')
        else:
            current_password = request.POST.get("old-password")
            new_password1 = request.POST.get("new-password1")
            new_password2 = request.POST.get("new-password2")
            user = User.objects.get(username=request.user)
            if not user.check_password(current_password):
                messages.info(request, "Invalid Password")
                return redirect('edit_profile_page')
            if new_password1 != new_password2:
                messages.info(request, "New Passwords Don't Match")
                return redirect('edit_profile_page')
            user.set_password(new_password1)
            user.save()
            messages.info(request, "Password Changed")
            return redirect('edit_profile_page')

    edit_user_form = EditUser(instance=request.user)
    context = {"edit_user_form": edit_user_form}
    return render(request, "edit_profile_page.html", context)
