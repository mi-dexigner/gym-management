from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
# Create your models here.

# import a signal library
from django.db.models.signals import post_save
from django.dispatch import receiver


#Banners
class Banner(models.Model):
    img = models.ImageField(upload_to='banners/')
    alt_text = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural ='Banners'

    def __str__(self):
        return f'{self.alt_text} | {self.image_tag}'

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url) )

class Service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img = models.ImageField(upload_to='services/',null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url) )


class Page(models.Model):
    title=models.CharField(max_length=150)
    detail = models.TextField()


    def __str__(self):
        return self.title

class Faq(models.Model):
    question=models.CharField(max_length=150)
    answer = models.TextField()


    def __str__(self):
        return self.question


class Enquiry(models.Model):
    full_name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    phone=models.CharField(max_length=150)
    message = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name

class Gallery(models.Model):
    title = models.CharField(max_length=150)
    img = models.ImageField(upload_to='gallery/',null=True)

    class Meta:
        verbose_name_plural ='Galleries'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url) )


class Package(models.Model):
    package_name = models.CharField(max_length=150,null=False)
    # description = models.TextField()
    price = models.PositiveIntegerField()
    max_member = models.PositiveIntegerField(null=True)
    highlight_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural ='Packages'

    def __str__(self):
        return self.package_name


class PackageFeatures(models.Model):
        package = models.ManyToManyField(Package, null=True)
        name = models.CharField(max_length=140)

        class Meta:
            verbose_name_plural = 'Package Details'

        def __str__(self):
            return f'{self.name}'


class PackageDiscount(models.Model):
    package = models.ForeignKey(Package,on_delete=models.CASCADE, null=True)
    total_months = models.PositiveIntegerField(default=0)
    total_discounts = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Package Discount'

    def __str__(self):
        return str(self.total_months)

class Subscriber(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile = models.CharField(max_length=20)
    address = models.TextField()
    img = models.ImageField(upload_to='customer/', null=True)

    class Meta:
        verbose_name_plural = 'Customer'

    def __str__(self):
        return str(self.customer)

    def image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" width="80" />' % (self.img.url) )
        else:
            return 'no-image'


@receiver(post_save,sender=User)
def create_subscriber(sender,instance,created,**kwrags):
	if created:
		Subscriber.objects.create(customer=instance)

class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    package = models.ForeignKey(Package,on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return str(self.package)

