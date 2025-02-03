from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import user

def customer_info(request):
    if 'billing_btn' in request.POST:
        return HttpResponseRedirect('/cus_bill/')
    
    
    elif 'search_btn' in request.POST:
        return HttpResponseRedirect('/search/')
    

    elif 'form_btn' in request.POST:
        pn = request.POST.get('product-name')
        pp = request.POST.get('purchasing-price')
        q = request.POST.get('quantity')
        cn = request.POST.get('customer-number')
        d = request.POST.get('date')
        c_data = user(product_name=pn, quantity=q, customer_number=cn, purshasing_price=pp, date=d)
        c_data.save()



    cus_info = user.objects.all()
    return render(request, 'index.html', {'cus_info':cus_info})

def search_bar(request):
    products = []
    search = request.GET.get('search_txt', '')
    products = user.objects.filter(product_name__icontains=search)
    return render(request, 'second.html', {'products':products})
def customer_bill(request):
    cus_info = user.objects.all()
    total_amt = 0
    for product in cus_info:
        product.total_price = product.purshasing_price * product.quantity
        total_amt+=product.total_price
    net_p = total_amt*0.10
    net_pl = total_amt-net_p
    return render(request, 'third.html', {'cus_info':cus_info, 'total_amt':total_amt, 'net_p':net_pl})