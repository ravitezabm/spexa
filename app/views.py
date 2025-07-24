from django.shortcuts import render, get_object_or_404
from .models import Banner, Service, Product, Project, Testimonial, ProductCategory, AboutSection


def index(request):
    banners = Banner.objects.filter(show_on_homepage=True)
    services = Service.objects.all()
    # featured_categories = Category.objects.all()[:3]
    projects = Project.objects.all()[:4]# or filter with a flag
    testimonials = Testimonial.objects.all()

    context = {
        'banners': banners,
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
    }
    return render(request, 'index.html', context)

def all_projects(request):
    projects = Project.objects.all()
    services = Service.objects.all()

    return render(request, 'all_projects.html', {'projects': projects,'services':services})

def project_detail(request, slug):
    services = Service.objects.all()
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_single.html', {'project': project,'services':services})

def all_services(request):
    services = Service.objects.all()
    return render(request, 'all_services.html', {'services': services})

def service_detail(request, slug):
    services = Service.objects.all()
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'services.html', {'service': service,'services': services})

def category_or_products(request, slug=None):
    services = Service.objects.all()
    if slug:
        category = get_object_or_404(ProductCategory, slug=slug)
        subcategories = category.subcategories.all()
        if subcategories.exists():
            return render(request, 'product_list.html', {
                'categories': subcategories,
                'products': None,
                'parent_category': category,
                'services': services
            })
        else:
            products = category.products.all()
            return render(request, 'product_list.html', {
                'categories': None,
                'products': products,
                'parent_category': category,
                'services': services
            })
    else:
        # First page – show top-level categories
        top_categories = ProductCategory.objects.filter(parent=None)
        return render(request, 'product_list.html', {
            'categories': top_categories,
            'products': None,
            'parent_category': None,
            'services': services
        })
def product_single(request, slug):
    services = Service.objects.all()
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:4]

    return render(request, 'product_single.html', {'product': product,'related_products': related_products,'services':services})

def about_view(request):
    about = AboutSection.objects.first()
    services = Service.objects.all()

    return render(request, 'about.html', {'about': about,'services':services})

def downloads(request):
    services = Service.objects.all()
    return render(request,'downloads.html',{'services':services})

def career(request):
    services = Service.objects.all()
    return render(request,'career.html',{'services':services})

def contact(request):
    services = Service.objects.all()
    return render(request,'contact.html',{'services':services})