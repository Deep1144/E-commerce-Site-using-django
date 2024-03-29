from django.shortcuts import render
from django.http import HttpResponse
from . models import product , Contact ,Orders
from math import ceil
# Create your views here.
def index(request):
    #products = product.objects.all()
    #print(products)
    #n=len(products)
    allprods= []
    catprods = product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    print(cats)
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        print(n)
        nslides = ceil(n/4)
        allprods.append([prod , range(1,nslides),nslides])
    #allprods = [[products,range(1,nslides),nslides],
    #            [products,range(1,nslides),nslides]]
    params = {'allprods':allprods}
    # params = {'product':products,'no_of_slides':nslides,'range':range(1,nslides)}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email =request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")

        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def prodview(request,myid):
    Product = product.objects.get(id=myid)
    return render(request,'shop/prodview.html',{'product': Product})

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get("itemsjson")
        name = request.POST.get("name")
        email =request.POST.get("email")
        address =request.POST.get("address1") + " " + request.POST.get("address2")
        city =request.POST.get("city")
        state=request.POST.get("state")
        zip_code =request.POST.get("zip_code")
        phone = request.POST.get("phone" )

        order = Orders(items_json = items_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request,'shop/checkout.html',{'thank':thank , 'id':id})
    return render(request,'shop/checkout.html')