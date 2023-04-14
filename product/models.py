from django.db import models



class Category(models.Model):
    c_name = models.CharField(max_length=100)


    def __str__(self):
        return self.c_name
    
    @staticmethod
    def get_category():
        return Category.objects.all()



class Product(models.Model):
    p_name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=500,default='')
    price = models.DecimalField(decimal_places=2,max_digits=5)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='products')


    def __str__(self):
        return self.p_name
    

    @staticmethod
    def get_all_product():
        return Product.objects.all()
    
    @staticmethod
    def get_all_product_by(categoryid):
        if categoryid:
            return Product.objects.filter(Category=categoryid)
        else:
            return Product.objects.all()
        

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
