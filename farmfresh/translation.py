from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'author_name',)


@register(Feature)
class FeatureTranslationOptions(TranslationOptions):
    fields = ('title','description',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'category',)


@register(Farmer)
class FarmerTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'designation', 'adress',)


@register(Customer)
class CustomerTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'comment', 'adress',)


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title','description',)