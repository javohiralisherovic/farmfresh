from django.urls import path
from  . import views
from farmfresh.views import *

urlpatterns = [
    path('', views.infex, name='index'),
    path('', views.infex),
    path('product/', ProductsListView.as_view() , name='product'),
    path('product/search', ProductsListView.as_view() , name='search'),
    path('product-view/<int:id>/', ProductView.as_view()),
    path('about/', about,  name = 'about'),
    path('blog/', blog, name = 'blog'),
    path('contact/', contact,  name = 'contact'),
    path('detail/', detail, name = 'detail'),
    path('feature/', feature, name = 'feature'),
    path('service/', service,  name = 'service'),
    path('team/', team, name = 'team'),
    path('testimonial/', testimonial, name = 'testimonial'),
]