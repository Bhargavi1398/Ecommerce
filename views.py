from django.shortcuts import render,redirect
from testapp.models import Ecommerce
from testapp.forms import ConformationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def get_products(request):
    ecommerce=Ecommerce.objects.all()
    item_name=request.GET.get('item_name')
    if item_name!=''and item_name is not None:
        ecommerce=ecommerce.filter(name__contains=item_name,price__gt=3000)
    my_dict={'ecommerce':ecommerce}
    return render(request,"html1/home.html",my_dict)

def Ecommerce_Data(request,id):
    ecommerce=Ecommerce.objects.get(id=id)
    return render(request,"html1/read.html",{'ecommerce':ecommerce})

@login_required
def Conformation_Data(request):
    form=ConformationForm()
    ecommerce=Ecommerce.objects.all()
    if request.method=='POST':
        order_amount = 5000000
        order_currency = 'INR'
        client=razorpay.Client(auth=('rzp_test_xspArVvYv57PrL','M2XYoooavBcVnycSWXT0CGdJ'))
        payment=client.order.create(amount=order_amount, currency=order_currency)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/home')
    my_dict={'form':form ,'ecommerce':ecommerce}
    return render(request,"html1/order.html",my_dict)
