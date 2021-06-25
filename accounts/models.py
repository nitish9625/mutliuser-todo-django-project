from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Todo(models.Model):
    status_choice = [
        ('C','COMPLETE'),
        ('P','PANDING'),
    ]
    priority_choice = [
        ('1', '1️⃣'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),
        ('6', '6️⃣'),
        ('7', '7️⃣'),
        ('8', '8️⃣'),
        ('9', '9️⃣'),
        ('10', '🔟'),
    ]

    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=status_choice)
    priority = models.CharField(max_length=10, choices=priority_choice)

    def __str__(self):
        return self.title
