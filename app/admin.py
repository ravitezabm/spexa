from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from .models import *
from ckeditor.fields import RichTextField
from django import forms

admin.site.register(Banner)
admin.site.register(Project)
admin.site.register(Testimonial)
admin.site.register(Service)
admin.site.register(Certificate)
admin.site.register(CompanyProfile)
admin.site.register(Career)
# admin.site.register(ProductCategory)
# admin.site.register(Product)
admin.site.register(AboutSection)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)