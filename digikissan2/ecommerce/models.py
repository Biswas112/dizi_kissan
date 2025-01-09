
from django.db import models
from django.contrib.auth.models import User

class Create_Seller_Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=150)  # Corrected spelling
    business_name_nepali = models.CharField(max_length=150, blank=True, null=True)
    business_address = models.TextField()
    business_contact_number = models.CharField(max_length=15)  # Corrected spelling
    business_email = models.EmailField()
    
    # Verification Information
    citizenship_number = models.CharField(max_length=20, blank=True, null=True)
    pan_number = models.CharField(max_length=20, blank=True, null=True)
    goverment_id = models.FileField(upload_to='documents/', blank=True)
    verification_status = models.CharField(
        max_length=20,
        choices=[('pending', 'pending'), ('Verified', 'Verified'), ('Rejected', 'Rejected')],
        default='pending'
    )
    
    # Bank Information
    bank_account_number = models.CharField(max_length=30)
    bank_name = models.CharField(
        max_length=100,
        choices=[
            ('Rastriya Banijya', 'Rastriya Banijya'),
            ('Nabil Bank', 'Nabil Bank'),
            ('Himalaya Bank', 'Himalaya Bank'),
            ('Global IME', 'Global IME'),
            ('Nepal Investment', 'Nepal Investment'),
            ('Agriculture Development', 'Agriculture Development')
        ],
        null=True,
        blank=True
    )
    ifcs_code = models.CharField(max_length=11)
    payment_gateway_id = models.CharField(max_length=100, blank=True, null=True)
    
    # Business Categories
    categories = models.CharField(
        max_length=50,
        choices=[
            ('Vegetables', 'Vegetables'),
            ('Fruits', 'Fruits'),
            ('Rice', 'Rice'),
            ('Spices', 'Spices'),
            ('Other', 'Other')
        ],
        default='Other'
    )
    
    # Seller Statistics
    total_sales = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    reviews_count = models.PositiveIntegerField(default=0)
    
    # Additional Info
    profile_picture = models.ImageField(upload_to='seller_pictures/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.business_name


class Tag(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    
class Products(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    seller=models.ForeignKey(Create_Seller_Account,on_delete=models.CASCADE)
    poduct_image=models.ImageField(upload_to='products/')
    product_name=models.CharField(max_length=100)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    product_description=models.TextField()
    stock_quantity=models.PositiveIntegerField(default=0)
    status=models.CharField(max_length=100,choices=[('avilable','Avilable'),('out_of_stock','Out of Stock'),("discounted","Discounted")],default="avilable")
    discount_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    average_ratings=models.DecimalField(max_digits=3,decimal_places=2,default=0.0)
    date_added=models.DateField(auto_now_add=True)
    is_fetuared=models.BooleanField(default=False)
    tags=models.ManyToManyField(Tag,blank=True)
    product_weight= models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    avilable_from=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.product_name
    
    
    
