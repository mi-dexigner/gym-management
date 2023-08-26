from django.shortcuts import render,get_object_or_404,redirect
from django.template.loader import get_template
from main.models import Banner,Service,Page,Faq,Package,PackageFeatures,Gallery,Subscription
from . import forms
import stripe
from django.contrib.auth.decorators import login_required



# Create your views here.
def Home(request):
    context = {
        #'navbars': Page.objects.all().order_by("title"),
        'banners' : Banner.objects.all(), # Banner.objects.filter()
        'services' : Service.objects.all().order_by("title")[:3],
        'about' : get_object_or_404(Page,pk=1),
        'galleries': Gallery.objects.all().order_by("title"),
    }
    return render(request,"main/home.html",context)

def AboutPage(request):
    context = {
    }
    return render(request, "main/about.html", context)

def ServicePage(request):
    context = {
    }
    return render(request, "main/services.html", context)

def PageDetails(request,id):
    context = {
        #'navbars': Page.objects.all().order_by("title"),
        'page': get_object_or_404(Page, id=id),
    }
    return render(request, "main/page.html", context)

def GalleryList(request):
    context = {
        'galleries': Gallery.objects.all().order_by("title"),
    }
    return render(request,"main/gallery.html",context)
def FaqList(request):
    context = {
        'faqs': Faq.objects.all(),
        #'faq': get_object_or_404(Faq,),
    }
    return render(request, "main/faq.html", context)

def EnquiryForm(request):
    if request.method == 'POST':
        form = forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': forms.EnquiryForm(),
    }
    return render(request, "main/enquiry.html", context)


def Pricing(request):
    context = {
        'packages': Package.objects.all(),
        'features': PackageFeatures.objects.all(),
    }
    return render(request, "main/pricing.html", context)

def RegisterForm(request):
    message = None
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        if form.is_valid():
            form.save()
            message = 'Thank you for the Registration'
    context = {
        'form': forms.SignUp,
        'message':message
    }
    return render(request, "main/register.html", context)


def Order(request,package_id):
    context = {
        'package_detail': get_object_or_404(Package,pk=package_id),
    }
    return render(request, "main/checkout.html", context)


stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'
def CreateCheckoutSession(request,package_id):
 package = get_object_or_404(Package,pk=package_id)
 session = stripe.checkout.Session.create(
     line_items=[{
         'price_data': {
             'currency': 'usd',
             'product_data': {
                 'name': package.package_name,
             },
             'unit_amount': package.price*100,
         },
         'quantity': 1,
     }],
     mode='payment',
     success_url='http://127.0.0.1:8000/success?session_id={CHECKOUT_SESSION_ID}',
     cancel_url='http://127.0.0.1:8000/cancel',
     client_reference_id = package_id
 )

 return redirect(session.url, code=303)

from django.core.mail import EmailMessage
@login_required
def CreateCheckoutSuccess(request):

    session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(session_id)
    package_id = session.client_reference_id
    package = get_object_or_404(Package, pk=package_id)
    user = request.user
    # customer = stripe.Customer.retrieve(session.customer)

    Subscription.objects.create(
        package=package,
        user=user,
        price=package.price,
    )
    subject = 'Order Email'
    html_content = get_template('main/orderemail.html').render({'title': package.package_name})
    from_email = 'idre172@gmail.com'

    msg = EmailMessage(subject, html_content, from_email, ['dev@yopmail.com'])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    return render(request, "main/success.html")

def CreateCheckoutCancel(request):
    context = {
    }
    return render(request, "main/cancel.html", context)