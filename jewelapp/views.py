from django.shortcuts import render,redirect
from jewelapp.models import Jewelcate_Db,ornaments_Db
from webapp.models import ContactDb,Registerdb,OrderDB
import os.path
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def new(request):
    total=OrderDB.objects.count()
    contact=ContactDb.objects.count()
    return render(request,"index.html",{'total':total,'contact':contact})
def addcate(request):
    return render(request,"addcategory.html")
def savejewelcat(request):
    if request.method =="POST":
        Category_Na =request.POST.get('Category_Name')
        Product_Na = request.POST.get('Product_name')
        price = request.POST.get('Price')
        Descri = request.POST.get('Description')
        img=request.FILES['Cat_img']
        obj=Jewelcate_Db(Category_Name=Category_Na,Product_Name=Product_Na,Price=price,Description=Descri,Cat_img=img)
        obj.save()
        return redirect(addcate)
def displaycate(request):
    data=Jewelcate_Db.objects.all()
    return render(request,"displaycaegories.html",{'data':data})
def editcatego(request,cat_id):
    data = Jewelcate_Db.objects.get(id=cat_id)
    if request.method=="POST":
        data.Category_Name=request.POST.get('Category_Name')
        data.Product_Name=request.POST.get('Product_Name')
        data.Price = request.POST.get('Price')
        data.Description = request.POST.get('Description')
        if 'Cat_img' in request.FILES:
            old_img=data.Cat_img.path
            if os.path.exists(old_img):
                os.remove(old_img)
            data.Cat_img=request.FILES['Cat_img']
        data.save()
        return redirect('displaycate')
    return render(request,"editcategories.html",{'data':data})

def delcate(request,cat_id):
    x=Jewelcate_Db.objects.filter(id=cat_id)
    x.delete()
    return redirect('displaycate')
def ornaments(request):
    return render(request,"ornamentsadd.html")
#
def saveornaments(request):
    if request.method =="POST":
        Category_Name =request.POST.get('Category_Name')
        Product_Name = request.POST.get('Product_name')
        Price = request.POST.get('Price')
        Description = request.POST.get('Description')
        Weight = request.POST.get('Weight')
        Item_gross_weight = request.POST.get('Item_gross_weight')
        Item_net_weight = request.POST.get('Item_net_weight')
        Chain_length = request.POST.get('Chain_length')
        Diameter = request.POST.get('Diameter')
        Ornaments_img1=request.FILES['Ornaments_img1']
        Ornaments_img2 = request.FILES['Ornaments_img2']
        obj=ornaments_Db(Category_Name=Category_Name,Product_Name=Product_Name,Price=Price,Description=Description,Weight=Weight,Item_gross_weight=Item_gross_weight,Item_net_weight=Item_net_weight,Chain_length=Chain_length,Diameter=Diameter,Ornaments_img1=Ornaments_img1,Ornaments_img2=Ornaments_img2)
        obj.save()
        return redirect(ornaments)
def displayornaments(request):
    data = ornaments_Db.objects.all()
    return render(request, "displayornaments.html", {'data': data})
def editornaments(request,orn_id):
    data=ornaments_Db.objects.get(id=orn_id)
    if request.method == "POST":
        data.Category_Name = request.POST.get('Category_Name')
        data.Product_Name = request.POST.get('Product_Name')
        data.Price = request.POST.get('Price')
        data.Description = request.POST.get('Description')
        data.Weight = request.POST.get('Weight')
        data.Item_gross_weight = request.POST.get('Item_gross_weight')
        data.Item_net_weight = request.POST.get('Item_net_weight')
        data.Chain_length = request.POST.get('Chain_length')
        data.Diameter = request.POST.get('Diameter')
        if 'Ornaments_img1' in request.FILES:
            orn_img=data.Ornaments_img1.path
            if os.path.exists(orn_img):
                os.remove(orn_img)
            data.Ornaments_img1=request.FILES['Ornaments_img1']
        if 'Ornaments_img2' in request.FILES:
            orn_img2=data.Ornaments_img2.path
            if os.path.exists(orn_img2):
                os.remove(orn_img2)
            data.Ornaments_img2=request.FILES['Ornaments_img2']
        data.save()
        return redirect('displayornaments')
    return render(request,"ornamentsedit.html",{'data':data})

def delornaments(request,orn_id):
    x=ornaments_Db.objects.filter(id=orn_id)
    x.delete()
    return redirect('displayornaments')
def admin1(request):
    return render(request,"adminnlogin.html")
def adminloged(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password =request.POST.get('password')
        if User.objects.filter(username__contains=username).exists():
            x=authenticate(username=username,password=password)
            if x is not None:
                login(request,x)
                request.session['username']=username
                request.session['password'] = password

                return  redirect(new)
            else:
                return redirect(admin1)
        else:
            return redirect(admin1)

def displaycontact(request):
    data=ContactDb.objects.all()
    return render(request,"displaycontact.html",{'data':data})
def deletecontact(request,con_id):
    x = ContactDb.objects.filter(id=con_id)
    x.delete()
    return redirect('displaycontact')
def displayuser(request):
    data=Registerdb.objects.all()
    return render(request,"displayuser.html",{'data':data})
def deleteuser(request,user_id):
    x = Registerdb.objects.filter(id=user_id)
    x.delete()
    return redirect('displayuser')
def orderdisplay(request):
    data=OrderDB.objects.all()
    return render(request,"displayorder.html",{'data':data})
