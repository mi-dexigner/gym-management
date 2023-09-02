from django.shortcuts import render,get_object_or_404,redirect
from django.template.loader import get_template
from main.models import Service,Page,Faq,Package,PackageFeatures,Subscription,SiteSettings
from . import forms
import stripe
from django.contrib.auth.decorators import login_required



# Create your views here.
def Home(request):
    context = {
        'setting': get_object_or_404(SiteSettings,pk=1),
        # 'banners' : Banner.objects.all(), # Banner.objects.filter()
        'services' : Service.objects.all().order_by("title")[:3],
        'about' : get_object_or_404(Page,pk=1),
        # 'galleries': Gallery.objects.all().order_by("title"),
    }
    return render(request,"main/home.html",context)

def AboutPage(request):
    context = {
        'setting': get_object_or_404(SiteSettings, pk=1),
    }
    return render(request, "main/about.html", context)

def ServicePage(request):
    context = {
        'setting': get_object_or_404(SiteSettings, pk=1),
        'services': Service.objects.all().order_by("title"),
    }
    return render(request, "main/services.html", context)

def PageDetails(request,id):
    context = {
        'setting': get_object_or_404(SiteSettings,pk=1),
        'page': get_object_or_404(Page, id=id),
    }
    return render(request, "main/page.html", context)

def FaqList(request):
    context = {
        'setting': get_object_or_404(SiteSettings, pk=1),
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
        'setting': get_object_or_404(SiteSettings, pk=1),
        'form': forms.EnquiryForm(),
    }
    return render(request, "main/enquiry.html", context)


def Pricing(request):
    context = {
        'setting': get_object_or_404(SiteSettings, pk=1),
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
        'setting': get_object_or_404(SiteSettings, pk=1),
        'form': forms.SignUp,
        'message':message
    }
    return render(request, "main/register.html", context)


def Order(request,package_id):
    context = {
        'setting': get_object_or_404(SiteSettings, pk=1),
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
    context ={
        'setting': get_object_or_404(SiteSettings, pk=1),
    }
    return render(request, "main/success.html",context)

@login_required
def CreateCheckoutCancel(request):
    context = {
        'setting': get_object_or_404(SiteSettings, pk=1),
    }
    return render(request, "main/cancel.html", context)

@login_required
def UserDashboard(request,):
    context = {
        'setting': get_object_or_404(SiteSettings, pk=1),
    }
    return render(request, "user/dashboard.html", context)

@login_required
def UserProfileUpdate(request):
	msg=None
	if request.method=='POST':
		form=forms.ProfileForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			msg='Data has been saved'
	form=forms.ProfileForm(instance=request.user)
	return render(request, 'user/update-profile.html',{'form':form,'msg':msg})

@login_required
def UserOrderHistory(request):
    current_user = request.user
    context = {
        'setting': get_object_or_404(SiteSettings, pk=1),
        'packages': Package.objects.all(),
        'orders':Subscription.objects.filter(user=current_user)

    }
    return render(request, "user/order-history.html", context)