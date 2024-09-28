from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from gymapp import views
from django_distill import distill_path

def get_index():
    return None

urlpatterns = [
        distill_path('', views.index, name='index', distill_func=get_index),
    
    path('terms_and_conditions/', views.terms_and_conditions_view, name='terms_and_conditions'),
    path('about/', views.about, name='about'),
    path('ActivatedMember/', views.ActivatedMember, name='ActivatedMember'),
    path('ActivateMember/', views.ActivateMember, name='ActivateMember'),
    path('AddMember/', views.AddMember, name='AddMember'),
   
    path('footer/', views.footer, name='footer'),
    path('location/', views.location, name='location'),
    path('login/', views.login, name='login'),

    path('Membership/', views.Membership, name='membership'),
    path('detail_login/',  views.detail_login, name='detail_login'),
    path('memberfromsite/',  views.memberfromsite, name='memberfromsite'),
    path('track/<int:member_id>/', views.track, name='track'),

   
  #  path('navbar/', views.navbar, name='navbar'),
    path('owner/', views.owner, name='owner'),
    path('ownerwork/', views.ownerwork, name='ownerwork'),
   
    
   
    path('trainer/', views.trainer, name='trainer'),

    path('pro_about/', views.pro_about, name='pro_about'),
    
    path('pro_blog_detail/<int:blog_id>/', views.pro_blog_detail, name='pro_blog_detail'),
    path('pro_blog/', views.pro_blog, name='pro_blog'),
    path('pro_contact/', views.pro_contact, name='pro_contact'),
    path('pro_index/', views.pro_index, name='pro_index'),
    path('pro_product_detail/', views.pro_product_detail, name='pro_product_detail'),
    path('pro_product/', views.pro_product, name='pro_product'),
    
    path('quick_view/<int:product_id>/', views.quick_view, name='quick_view'),
    path('quick_protein/<int:product_id>/', views.quick_protein, name='quick_protein'),
    path('quick_product/<int:product_id>/', views.quick_product, name='quick_product'), 
     path('buy_nowp/', views.buy_nowp, name='buy_nowp'),
     path('buy_nowe/', views.buy_nowe, name='buy_nowe'),
     path('buy_nows/', views.buy_nows, name='buy_nows'),
     path('order_list/', views.order_list, name='order_list'),
      path('delete_order_item/<int:order_id>/', views.delete_order_item, name='delete_order_item'),
      path('order_success/', views.order_success, name='order_success'),
       path('download_slip/<int:order_id>/', views.download_slip, name='download_slip'),
   
   #admin back ke liye
    path('panel/', views.panel, name='panel'),

    path('admin_forgot_password/', views.admin_forgot_password, name='admin_forgot_password'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_index/', views.admin_index, name='admin_index'),
    path('admin_base/', views.admin_base, name='admin_base'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_register/', views.admin_register, name='admin_register'),
    path('admin_tables/', views.admin_tables, name='admin_tables'),

    path('error/', views.error, name='error'),
    path('admin_reg_trainer/', views.admin_reg_trainer, name='admin_reg_trainer'),
    path('admin_trainer/', views.admin_trainer, name='admin_trainer'),
     path('admin_expaire/', views.admin_expaire, name='admin_expaire'),
     path('admin_active/', views.admin_active, name='admin_active'),
    path('admin_total/', views.admin_total, name='admin_total'),
    path('admin_tables2/', views.admin_tables2, name='admin_tables2'),
    path('admin_mdelete/<int:member_id>/', views.admin_mdelete, name='admin_mdelete'),
    path('admin_medit/<int:member_id>/', views.admin_medit, name='admin_medit'),
    path('admin_mdetail/<int:member_id>/', views.admin_mdetail, name='admin_mdetail'),
    path('admin_tdelete/<int:trainer_id>/', views.admin_tdelete, name='admin_tdelete'),
    path('admin_tedit/<int:trainer_id>/', views.admin_tedit, name='admin_tedit'),
    path('admin_tdetail/<int:trainer_id>/', views.admin_tdetail, name='admin_tdetail'),
    path('gym_imga_upload/', views.gym_imga_upload, name='gym_imga_upload'),
    path('gym_imgdelete/<int:image_id>/', views.gym_imgdelete, name='gym_imgdelete'),
    path('admin_siteuser/', views.admin_siteuser, name='admin_siteuser'),
    path('admin_onsitereg<int:siteuser_id>/', views.admin_onsitereg, name='admin_onsitereg'),
    path('admin_onsiteedit/', views.admin_onsiteedit, name='admin_onsiteedit'),
    path('custom_site/', views.custom_site, name='custom_site'),
    path('display_gym_info/', views.display_gym_info, name='display_gym_info'),

     # URL pattern for the product list page
    path('product_list', views.product_list, name='product_list'),
    # URL pattern for adding a new product
    path('add_product/', views.add_product, name='add_product'),
    # URL pattern for editing a product (assuming you have a product_id)
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    # URL pattern for deleting a product (assuming you have a product_id)
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),

     # URL pattern for the product list page
    path('protein_list', views.protein_list, name='protein_list'),
    path('add_protein/', views.add_protein, name='add_protein'),
    path('edit_protein/<int:product_id>/', views.edit_protein, name='edit_protein'),
    path('delete_protein/<int:product_id>/', views.delete_protein, name='delete_protein'),

     # URL pattern for the product list page
    path('equipment_list', views.equipment_list, name='equipment_list'),
    path('add_equipment/', views.add_equipment, name='add_equipment'),
    path('edit_equipment/<int:product_id>/', views.edit_equipment, name='edit_equipment'),
    path('delete_equipment/<int:product_id>/', views.delete_equipment, name='delete_equipment'),
    
    path('add_blog/', views.add_blog, name='add_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    
   
    # Add other URL patterns as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)