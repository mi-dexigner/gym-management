from django.urls import path
from .views import Home,AboutPage,ServicePage,PageDetails,FaqList,EnquiryForm,Pricing,RegisterForm,Order,CreateCheckoutSession,CreateCheckoutSuccess,CreateCheckoutCancel,UserDashboard,UserProfileUpdate,UserOrderHistory

app_name = "main"
urlpatterns = [
    path('', Home,name="home"),
    path('page/<int:id>/', PageDetails,name="page"),
    path('about/', AboutPage,name="about"),
    path('services/', ServicePage,name="services"),
    path('faq/', FaqList,name="faq"),
    path('pricing/', Pricing,name="pricing"),
    path('checkout/<int:package_id>/', Order,name="order"),
    path('checkout-session/<int:package_id>/', CreateCheckoutSession,name="checkout-session"),
    path('success/', CreateCheckoutSuccess,name="checkout-success"),
    path('cancel/', CreateCheckoutCancel,name="checkout-success"),
    path('accounts/signup/', RegisterForm,name="register"),
    path('contact/', EnquiryForm,name="contact"),


    # User Dashboard Section
    path('account/user-dashboard/', UserDashboard, name="user-dashboard"),
    path('account/update-profile',UserProfileUpdate,name='update-profile'),
    path('account/order/', UserOrderHistory, name='order-history'),

]

