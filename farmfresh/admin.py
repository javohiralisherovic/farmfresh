from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from .models import *


class ProductAdminForm(forms.ModelForm):
    description_en = forms.CharField()
    description_uz = forms.CharField()

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("name",)


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ("title", "slug", "author_name", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "image"


@admin.register(Feature)
class FeatureAdmin(TranslationAdmin):
    list_display = ("title", "description")


@admin.register(Farmer)
class FarmerAdmin(TranslationAdmin):
    list_display = ("first_name", "last_name", "designation", "city", "adress", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "image"


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ("title", "description", "category", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Image"


@admin.register(Customer)
class CustomerAdmin(TranslationAdmin):
    model = Customer
    extra = 1
    list_display = ("first_name", "last_name", "city", "adress", "comment")


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ("title", "description")


# admin.site.register(Customer)
# admin.site.register(Farmer)
# admin.site.register(Product)
admin.site.register(Fact)
admin.site.register(AboutUs)
admin.site.register(Contact)
admin.site.register(Payment)
admin.site.register(Country)
admin.site.register(City)
