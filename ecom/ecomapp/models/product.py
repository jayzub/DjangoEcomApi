from django.db import models

def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    return 'uploads/%s.%s' % (instance.name, extension)


class Product(models.Model):
    name = models.CharField(max_length=50)
    barcode = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # discount = models.IntegerField(null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    # inventory = models.IntegerField()
    size = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)


    def __str__(self):
        return self.name

    def get_imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    image_url = property(get_imageURL)