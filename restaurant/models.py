from django.db import models

# Create your models here.
class MenuItem(models.Model):
    CATEGORY_CHOICES =[
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')
    
    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price}"
    
class Chef(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    image = models.ImageField(upload_to='chef_images/')

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"