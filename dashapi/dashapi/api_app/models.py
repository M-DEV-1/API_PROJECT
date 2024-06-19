from django.db import models

# Create your models here.

class stock(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    # automatically notes the date and time
    
    shortname = models.CharField(max_length=5)
    stockname = models.CharField(max_length=200)
    # NVDA, NVIDIA Corp
    
    class Option(models.TextChoices):
        BUY = 'BUY', 'Buy'
        SELL = 'SELL', 'Sell'
    option = models.CharField(max_length=4, choices=Option.choices, default = Option.BUY)
    # BUY/SELL
    
    quantity = models.IntegerField() 
    # 5 units
    
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # 120.89
    
    def __str__(self):
        return self.stockname
    
    