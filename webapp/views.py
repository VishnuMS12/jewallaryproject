from django.shortcuts import render,redirect
from jewelapp.models import Jewelcate_Db,ornaments_Db
from webapp.models import ContactDb,Registerdb,CartDB,OrderDB
from django.contrib import messages
def home(request):
    data=Jewelcate_Db.objects.all()
    return render(request,"home.html",{'data':data})

def contact(request):
    return render(request,"Contact.html",)
def savecontact(request):
    if request.method =="POST":
        Name =request.POST.get('Name')
        Email = request.POST.get('Email')
        Subject = request.POST.get('Subject')
        Message = request.POST.get('Message')
        obj=ContactDb(Name=Name,Email=Email,Subject=Subject,Message=Message)
        obj.save()
        messages.success(request,"Succeccefully Submit Your contact details")
        return redirect(contact)
def home2(request):
    data=Jewelcate_Db.objects.all()
    return render(request,"home2.html",{'data':data})
def filtedproduct(request,orn_name):
    products=ornaments_Db.objects.filter(Category_Name=orn_name)
    return render(request,"filterproducts.html",{'products':products})
def singleproduct(request,orb_id):
    data=ornaments_Db.objects.get(id=orb_id)
    return render(request,"singleproduct.html",{"data":data})
def userregister(request):
    return render(request,"newregister.html")
def save_userregister(request):
    if request.method =="POST":
        username =request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        Mobile_number = request.POST.get('Mobile_number')
        Email_id=request.POST.get('Email_id')
        obj=Registerdb(username=username,password=password,confirm_password=confirm_password,Mobile_number=Mobile_number,Email_id=Email_id)
        obj.save()
        return redirect(userregister)
def loginform(request):
    return render(request,"Loginform.html")
def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pw=request.POST.get('password')
        if Registerdb.objects.filter(username=un,password=pw).exists():
            request.session['username']=un
            request.session['password'] =pw
            return redirect(home)
        else:
            return redirect(loginform)
    else:
        return redirect(loginform)
def about(request):
    return render(request,"about.html")
def cart(request):
    subtotal=0
    total=0
    data=CartDB.objects.filter(user_name=request.session['username'])
    for i in data:
        subtotal += i.Total_price
        if subtotal>150000:
            delivary_charge=1000
        else:
            delivary_charge = 5000
        total=subtotal+delivary_charge
    return render(request,"cart.html",{'data':data,'subtotal':subtotal,'total':total,'delivary_charge':delivary_charge})
def savecart(request):
    if request.method=="POST":
        quantity=request.POST.get('quantity')
        proname=request.POST.get('prodctname')
        username = request.POST.get('username')
        price = request.POST.get('price')
        total=request.POST.get('total')

    try:
        x=ornaments_Db.objects.get(Product_Name=proname)
        img=x.Ornaments_img1
    except ornaments_Db.DoesNotExist:
        img=None
    obj=CartDB( Quantity=quantity,Product_name=proname,user_name=username,Price=price,Total_price=total,Prod_img=img)
    obj.save()
    return redirect(cart)
def deletecart(request,c_id):
    x=CartDB.objects.filter(id=c_id)
    x.delete()
    return redirect(cart)
def checkout(request):
    subtotal = 0
    total = 0
    data = CartDB.objects.filter(user_name=request.session['username'])
    for i in data:
        subtotal += i.Total_price
        if subtotal > 150000:
            delivary_charge = 1000
        else:
            delivary_charge = 5000
        total = subtotal + delivary_charge
    return render(request,"checkout.html",{'data':data,'subtotal':subtotal,'total':total,'delivary_charge':delivary_charge})
def savecheckout(request):
    if request.method=="POST":
        Fname=request.POST.get('fname')
        Lname=request.POST.get('lname')
        Email = request.POST.get('email')
        Mobile = request.POST.get('mobile')
        Address =request.POST.get('address')
        Country = request.POST.get('country')
        Total = request.POST.get('total')
        City = request.POST.get('city')
        State = request.POST.get('state')
        Zip = request.POST.get('zip')
        obj = OrderDB(First_name=Fname, Last_name=Lname,Email=Email, Mobile=Mobile,Address=Address,Country=Country,Total_price=Total,City=City,State=State,ZIP_Code=Zip)
        obj.save()
        return redirect(payment)
def payment(request):
    subtotal = 0
    total = 0
    data = CartDB.objects.filter(user_name=request.session['username'])
    for i in data:
        subtotal += i.Total_price
        if subtotal > 150000:
            delivary_charge = 1000
        else:
            delivary_charge = 5000
        total = subtotal + delivary_charge
    return render(request,"payment.html",{'data':data,'subtotal':subtotal,'total':total,'delivary_charge':delivary_charge})