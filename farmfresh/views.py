from .models import *
from django.db.models import Q
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect 
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404


# Create your views here.


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            if new_comment.save:
                return redirect('blog')
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def infex(request):
    if request.method == "POST":
        email = request.POST.get('email')

        newsletter = Newsletter(
            email=email,
        )
        print(email)
        newsletter.save()

    productsdisplay = Product.objects.all()
    farmersdisplay = Farmer.objects.all()
    customersdisplay = Customer.objects.all()
    postsdisplay = Post.objects.all()
    featuredisplay = Feature.objects.all()
    servicedisplay = Service.objects.all()
    aboutdisplay = AboutUs.objects.all()
    factdisplay = Fact.objects.all()
    context = {"Product":productsdisplay, "Farmer":farmersdisplay, "Service":servicedisplay,
     "Customer":customersdisplay, "Post":postsdisplay, "Feature":featuredisplay, 'AboutUs': aboutdisplay, 'Fact':factdisplay}
    # print (context)

    def get_queryset(self):
        return Feature.objects.get(id=self.kwargs.get('id'))
    return render(request, "index.html", context)


@csrf_protect 
def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')

        newsletter = Newsletter(
            email=email,
        )
        print(email)
        newsletter.save()
        
    if request.method == "GET":
        name = request.GET.get('name')
        email = request.GET.get('email')
        subject = request.GET.get('subject')
        message = request.GET.get('message')

        contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        # print(name,email,subject,message)
        contact.save()
        # return redirect('index')
        
        
    aboutdisplay = AboutUs.objects.all()
    context = {'AboutUs': aboutdisplay}
    return render(request, 'contact.html', context)



class ProductsListView(ListView):
    model=Product
    template_name = 'product.html'
    context_object_name = 'product'
    success_url ='/'

    def get_context_data(self, **kwargs):
        q = Product.objects.all()

        url_dict = self.request.GET
        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(title__icontains=text) | Q(description__icontains=text))

        if 'from-price' in url_dict and url_dict['from-price']:
            from_price = int(url_dict['from-price'])
            q = q.filter(price__gte=from_price)
        
        if 'to-price' in url_dict and url_dict['to-price']:
            to_price = int(url_dict['to-price'])
            q = q.filter(price__lte=to_price)

        featuredisplay = Feature.objects.all()
        context = {'product': q, "Feature": featuredisplay}
        return context


class ProductView(ListView):
    model=Product
    template_name = 'product_view.html'
    context_object_name = 'product'
    success_url ='/'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context.update({
            'AboutUs': AboutUs.objects.all(),
            'Feature': Feature.objects.all(),
        })
        return context

    def get_queryset(self):
        return Product.objects.get(id=self.kwargs.get('id'))

 
def about(request):
    if request.method == "POST":
        email = request.POST.get('email')

        newsletter = Newsletter(
            email=email,
        )
        print(email)
        newsletter.save()

    farmersdisplay = Farmer.objects.all()
    aboutdisplay = AboutUs.objects.all()
    factdisplay = Fact.objects.all()
    context = {"Farmer":farmersdisplay, 'AboutUs': aboutdisplay, 'Fact':factdisplay}
    return render(request, 'about.html', context)


def blog(request):
    if request.method == "POST":
        email = request.POST.get('email')

        newsletter = Newsletter(
            email=email,
        )
        print(email)
        newsletter.save()

    postsdisplay = Post.objects.all()
    categorydisplay = Category.objects.all()
    aboutdisplay = AboutUs.objects.all()
    context = {"Post":postsdisplay, "Category":categorydisplay, 'AboutUs': aboutdisplay}
    return render(request, 'blog.html', context)


def feature(request):
    if request.method == "POST":
        email = request.POST.get('email')

        newsletter = Newsletter(
            email=email,
        )
        print(email)
        newsletter.save()
        
    servicedisplay = Service.objects.all()
    aboutdisplay = AboutUs.objects.all()
    featuredisplay = Feature.objects.all()
    context = {"Service":servicedisplay, 'AboutUs': aboutdisplay, "Feature":featuredisplay}
    return render(request, 'feature.html', context)


def detail(request):
    if request.method == "POST":
        email = request.POST.get('email')

        newsletter = Newsletter(
            email=email,
        )
        print(email)
        newsletter.save()

    postsdisplay = Post.objects.all()
    categorydisplay = Category.objects.all()
    customersdisplay = Customer.objects.all()
    aboutdisplay = AboutUs.objects.all()
    context = {"Customer":customersdisplay, "Post":postsdisplay, "Category":categorydisplay, 'AboutUs': aboutdisplay}
    return render(request, 'detail.html', context)


def service(request):
    if request.method == "POST":
        email = request.POST.get('email')

        newsletter = Newsletter(
            email=email,
        )
        print(email)
        newsletter.save()

    customersdisplay = Customer.objects.all()
    servicedisplay = Service.objects.all()
    aboutdisplay = AboutUs.objects.all()
    context = {"Customer":customersdisplay, "Service":servicedisplay, 'AboutUs': aboutdisplay}
    return render(request, 'service.html', context)


def team(request):
    if request.method == "POST":
        email = request.POST.get('email')

        newsletter = Newsletter(
            email=email,
        )
        print(email)
        newsletter.save()

    farmersdisplay = Farmer.objects.all()
    aboutdisplay = AboutUs.objects.all()
    context = {"Farmer":farmersdisplay, 'AboutUs': aboutdisplay}
    return render(request, 'team.html', context)


def testimonial(request):
    if request.method == "POST":
        email = request.POST.get('email')

        newsletter = Newsletter(
            email=email,
        )
        print(email)
        newsletter.save()

    customersdisplay = Customer.objects.all()
    aboutdisplay = AboutUs.objects.all()
    context = {"Customer":customersdisplay, 'AboutUs': aboutdisplay}
    return render(request, 'testimonial.html', context)

