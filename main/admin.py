from django.contrib import admin
from main.models import Service,Page,Faq,Enquiry,Package,PackageFeatures,Subscriber,Subscription,SiteSettings
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)

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

# class PackageDiscountAdmin(admin.ModelAdmin):
#     list_display = ('package','total_months','total_discounts')
# admin.site.register(PackageDiscount,PackageDiscountAdmin)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('customer','image_tag','mobile')
admin.site.register(Subscriber,SubscriberAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user','package','price')
admin.site.register(Subscription,SubscriptionAdmin)

class SiteSettingsAdmin(admin.ModelAdmin):
    class Meta:
        model = SiteSettings
        exclude = ()
    list_display = ('id','logo','site_title','site_description','contact_email','contact_phone','copyright_text')
    readonly_fields = ('id',)
    def has_add_permission(self, request):
        return False  # Disable the ability to add new SiteSettings objects

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            return True  # Allow editing of existing SiteSettings objects by their ID
        return False
admin.site.register(SiteSettings,SiteSettingsAdmin)