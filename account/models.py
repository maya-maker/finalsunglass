from django.db import models




class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_no = models.IntegerField()
    create_password  = models.CharField(max_length=20)


    def __str__(self):
        return self.email
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False