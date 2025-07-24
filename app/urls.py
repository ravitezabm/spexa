from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_view, name='about'),
    path('downloads/', views.downloads, name='downloads'),
    path('career', views.career, name='career'),
    path('contact', views.contact, name='contact'),
    path('projects/', views.all_projects, name='all_projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('services/', views.all_services, name='all_services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('all_products/', views.category_or_products, name='all_products'),
    path('category/<slug:slug>/', views.category_or_products, name='category_or_products'),
    path('product/<slug:slug>/', views.product_single, name='product_single'),

    # if needed
]
