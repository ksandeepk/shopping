from .models import Category, Product,Registration
from cart.forms import CartAddProductForm
from shop.forms import RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import ProductForm,RegistrationForm,LoginForm,ContactForm,CartForm
from django.http import HttpResponse
from django.core.mail import send_mail,BadHeaderError



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

def register(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            k=Registration(name=name,password=password,email=email)
            k.save()
            sub="registration success"
            sender='manovidela22@gmail.com'
            msg="Hello Mr/Ms."+request.POST['name']
            to=request.POST['email']
            print(to)
            send_mail(sub,msg,sender,[to])
            return HttpResponse("Register Successfully. Once check your mail") 
    return render(request,'shop/register.html',{'form':form})

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            yourname = form.cleaned_data['yourname']
            mobile_number = form.cleaned_data['mobile_number']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(subject, message, 'manovidela22@gmail.com', [email])
            return HttpResponse('Success! Thank you for your message.')
    return render(request, "shop/contact.html", {'form': form})


def login(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user=Registration.objects.get(email = email,password=password)
                return render(request,"shop/product/list.html",{'name':user.name})
            except Registration.DoesNotExist:
                return HttpResponse("login fail")
    return render(request,'shop/login.html',{'form':form})

def search(request):
    if request.method=='POST':
        name=request.POST['prdt']
        sp=Product.objects.filter(name__icontains=name)
        if sp:
            return render(request,'shop/product/list.html',{'products':sp})
        else:
            return render(request,'shop/product/list.html',{'msg':'No product'})
    return render(request,'shop/product/list.html')       

def viewimg(request):
    data=Product.objects.all()
    n=request.POST.get('pname',' ')
    p=request.POST.get('pprice',' ')
    i=request.POST.get('pimg',' ')
    request.session['name']=n
    return render(request,'shop/im.html',{"data":data})

def see(request,id):
    data=Product.objects.get(id=id)
    return render(request,'shop/cart.html',{'data':data})
