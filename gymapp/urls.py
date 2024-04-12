from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from gymapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate_bmi/', views.calculate_bmi, name='calculate_bmi'),
    path('terms_and_conditions/', views.terms_and_conditions_view, name='terms_and_conditions'),
    path('about/', views.about, name='about'),
    path('ActivatedMember/', views.ActivatedMember, name='ActivatedMember'),
    path('ActivateMember/', views.ActivateMember, name='ActivateMember'),
    path('AddMember/', views.AddMember, name='AddMember'),
    path('data/', views.data, name='data'),
    path('footer/', views.footer, name='footer'),
    path('location/', views.location, name='location'),
    path('login/', views.login, name='login'),
    path('memberdata/', views.memberdata, name='memberdata'),
    path('Memberlist/', views.Memberlist, name='Memberlist'),
    path('Membership/', views.Membership, name='membership'),
  #  path('navbar/', views.navbar, name='navbar'),
    path('owner/', views.owner, name='owner'),
    path('ownerwork/', views.ownerwork, name='ownerwork'),
    path('product/', views.product, name='product'),
    path('productdata/', views.productdata, name='productdata'),
    path('signup/', views.signup, name='signup'),
    path('trainer/', views.trainer, name='trainer'),
   
   
   
   #admin back ke liye
    path('panel/', views.panel, name='panel'),
    path('admin_404/', views.admin_404, name='admin_404'),
    path('admin_blank/', views.admin_blank, name='admin_blank'),
    path('admin_buttons/', views.admin_buttons, name='admin_buttons'),
    path('admin_cards/', views.admin_cards, name='admin_cards'),
    path('admin_charts/', views.admin_charts, name='admin_charts'),
    path('admin_forgot_password/', views.admin_forgot_password, name='admin_forgot_password'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_index/', views.admin_index, name='admin_index'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_register/', views.admin_register, name='admin_register'),
    path('admin_tables/', views.admin_tables, name='admin_tables'),
    path('admin_utilities_animation/', views.admin_utilities_animation, name='admin_utilities_animation'),
    path('admin_utilities_border/', views.admin_utilities_border, name='admin_utilities_border'),
    path('admin_utilities_color/', views.admin_utilities_color, name='admin_utilities_color'),
    path('admin_utilities_other/', views.admin_utilities_other, name='admin_utilities_other'),
    path('error/', views.error, name='error'),
    path('admin_reg_trainer/', views.admin_reg_trainer, name='admin_reg_trainer'),
    path('admin_trainer/', views.admin_trainer, name='admin_trainer'),
     path('admin_expaire/', views.admin_expaire, name='admin_expaire'),
     path('admin_active/', views.admin_active, name='admin_active'),
    path('admin_total/', views.admin_total, name='admin_total'),
    path('admin_tables2/', views.admin_tables2, name='admin_tables2'),
   
    # Add other URL patterns as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)