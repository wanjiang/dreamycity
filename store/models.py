from django.db import models

# Create your models here.
# Item Category
class StoreCategory(models.Model):
        categoryName = models.CharField(max_length=128)
        def __unicode__(self):
            return unicode(self.categoryName)

class Supplier(models.Model):
        supplierName = models.CharField(max_length=128)
        def __unicode__(self):
            return unicode(self.supplierName)
class Order(models.Model):
        supplier = models.ForeignKey(Supplier)
        orderDate = models.DateTimeField('Order Date')
        orderID = models.CharField(max_length=128)
        comment = models.CharField(max_length=128)
        isReturn = models.BooleanField(default=False)
        def __unicode__(self):
            return  unicode(self.orderDate)

class StoreItem(models.Model):
        category = models.ForeignKey(StoreCategory)
        itemName = models.CharField(max_length=128)
        itemSName = models.CharField(max_length=128)
        itemID = models.CharField(max_length=128)
        description = models.CharField(max_length=1024)
        price = models.DecimalField(max_digits=16,decimal_places=2)
        suggestPrice = models.DecimalField(max_digits=16,decimal_places=2)
        cost = models.DecimalField(max_digits=16,decimal_places=2)
        quantity = models.IntegerField(default=0)
        unit = models.CharField(max_length=20)
        supplier = models.ForeignKey(Supplier)
        picture = models.CharField(max_length=128)
        itemLink = models.CharField(max_length=128)
        reoderLever = models.CharField(max_length=20)
        isDeleted = models.BooleanField(default=False)
        # item quantity that need reoder
        buyQuantity = models.IntegerField(default=0)
        def __unicode__(self):
            return  unicode(self.itemName)

class OrderItem(models.Model):
        category = models.ForeignKey(StoreCategory)
        itemID = models.ForeignKey(StoreItem)
        orderID = models.ForeignKey(Order)
        supplier = models.ForeignKey(Supplier)
        itemName = models.CharField(max_length=128)
        cost = models.DecimalField(max_digits=16,decimal_places=2)
        quantity = models.IntegerField(default=0)
        unit = models.CharField(max_length=20)
        picture = models.CharField(max_length=128)
        lackQuantity = models.IntegerField(default=0)
        brokenQuantity = models.IntegerField(default=0)
        def __unicode__(self):
            return  unicode(self.itemName)