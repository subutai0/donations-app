from django.db import models

class Charity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='charity_images')

    def __str__(self):
        return self.name
    
# In models.py of charities app

class Donation(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=10, choices=[('one-time', 'One-time'), ('monthly', 'Monthly'), ('yearly', 'Yearly')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation of {self.amount} to {self.charity.name}"


class Donation(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=10, choices=[('one-time', 'One-time'), ('monthly', 'Monthly'), ('yearly', 'Yearly')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation of {self.amount} to {self.charity.name}"
