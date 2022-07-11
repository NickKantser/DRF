from django.db import models

class AttributeName(models.Model):
    nazev = models.CharField(max_length=50, null=True, blank=True)
    kod = models.CharField(max_length=50, null=True, blank=True)
    zobrazit = models.BooleanField(default=True, blank=True)

class AttributeValue(models.Model):
    hodnota = models.CharField(max_length=50)

class Attribute(models.Model):
    nazev_atributu_id = models.ForeignKey('AttributeName', on_delete=models.CASCADE)
    hodnota_atributu_id = models.ForeignKey('AttributeValue', on_delete=models.CASCADE)

class Product(models.Model):

    nazev = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    cena = models.DecimalField(max_digits=8, decimal_places=2)
    mena = models.CharField(max_length=5, default='CZK')
    published_on = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=True, blank=True)


class ProductAttributes(models.Model):
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

class Image(models.Model):
    nazev = models.CharField(max_length=120, null=True, blank=True)

class ProductImage(models.Model):
    nazev = models.CharField(max_length=50)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    obrazek_id = models.ForeignKey('Image', on_delete=models.CASCADE)

class Catalog(models.Model):
    nazev = models.CharField(max_length=120, null=True, blank=True)
    obrazek_id = models.ForeignKey('Image', on_delete=models.CASCADE, null=True, blank=True)
    products_ids = models.ManyToManyField('Product', null=True, blank=True)
    attributes_ids = models.ManyToManyField('Attribute', null=True, blank=True)
