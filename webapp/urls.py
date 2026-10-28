from django.urls import path
from jewelapp import views
from webapp import views
urlpatterns = [
path('home/',views.home,name='home'),
path('contact/',views.contact,name='contact'),
path('savecontact/',views.savecontact,name='savecontact'),
path('home2/',views.home2,name='home2'),
path('filtedproduct/<orn_name>/',views.filtedproduct,name='filtedproduct'),
path('singleproduct/<int:orb_id>/',views.singleproduct,name='singleproduct'),
path('userregister/',views.userregister,name='userregister'),
path('save_userregister/',views.save_userregister,name='save_userregister'),
path('',views.loginform,name='loginform'),
path('userlogin/',views.userlogin,name='userlogin'),
path('about/',views.about,name='about'),
path('cart/',views.cart,name='cart'),
path('savecart/',views.savecart,name='savecart'),
path('deletecart/<int:c_id>/',views.deletecart,name='deletecart'),
path('checkout/',views.checkout,name='checkout'),
path('savecheckout/',views.savecheckout,name='savecheckout'),
path('payment/',views.payment,name='payment')

]