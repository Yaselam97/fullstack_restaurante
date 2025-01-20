from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='dishes/')

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)  # Nome del mittente
    email = models.EmailField()  # Email del mittente
    message = models.TextField()  # Messaggio inviato
    timestamp = models.DateTimeField(auto_now_add=True)  # Data e ora di invio

    def __str__(self):
        return f"Messaggio da {self.name} ({self.email}) il {self.timestamp}"