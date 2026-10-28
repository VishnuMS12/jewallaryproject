from django.urls import path
from jewelapp import views
# from webapp import views
urlpatterns = [
path('new/',views.new,name='new'),
path('addcate/',views.addcate,name='addcate'),
path('savejewelcat/',views.savejewelcat,name='savejewelcat'),
path('displaycate/',views.displaycate,name='displaycate'),
path('editcatego/<int:cat_id>',views.editcatego,name='editcatego'),
path('delcate/<int:cat_id>',views.delcate,name='delcate'),
path('ornaments/',views.ornaments,name='ornaments'),
path('saveornaments/',views.saveornaments,name='saveornaments'),
path('displayornaments/',views.displayornaments,name='displayornaments'),
path('editornaments/<int:orn_id>/',views.editornaments,name='editornaments'),
path('delornaments/<int:orn_id>/',views.delornaments,name='delornaments'),
path('admin1/',views.admin1,name='admin1'),
path('adminloged/',views.adminloged,name='adminloged'),
path('displaycontact/',views.displaycontact,name='displaycontact'),
path('deletecontact/<int:con_id>/',views.deletecontact,name='deletecontact'),
path('displayuser/',views.displayuser,name='displayuser'),
path('deleteuser/<int:user_id>/',views.deleteuser,name='deleteuser'),
path('orderdisplay/',views.orderdisplay,name='orderdisplay'),

]