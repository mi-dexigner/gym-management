from django.contrib import admin
from main.models import Banner,Service,Page,Faq,Enquiry,Gallery,Package,PackageFeatures,PackageDiscount,Subscriber,Subscription
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text','image_tag',)
    # pass
admin.site.register(Banner,BannerAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Service,ServiceAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Page,PageAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','phone')
admin.site.register(Enquiry,EnquiryAdmin)

class FaqAdmin(admin.ModelAdmin):
    list_display = ('question',)
admin.site.register(Faq,FaqAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Gallery,GalleryAdmin)

class PackageAdmin(admin.ModelAdmin):
    list_editable = ('highlight_status',)
    list_display = ('package_name','price','highlight_status')
admin.site.register(Package,PackageAdmin)

class PackageFeatureAdmin(admin.ModelAdmin):
    list_display = ('name','get_package')
    def get_package(self, obj):
        return "|".join([sub.package_name for sub in obj.package.all()])
    get_package.short_description = 'Package'  # Set column header name
admin.site.register(PackageFeatures,PackageFeatureAdmin)

class PackageDiscountAdmin(admin.ModelAdmin):
    list_display = ('package','total_months','total_discounts')
admin.site.register(PackageDiscount,PackageDiscountAdmin)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('customer','image_tag','mobile')
admin.site.register(Subscriber,SubscriberAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user','package','price')
admin.site.register(Subscription,SubscriptionAdmin)