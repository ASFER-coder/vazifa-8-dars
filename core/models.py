from django.db import models

# Create your models here.
class Expense(models.Model):
    description = models.CharField(max_length=200)
    amount = models.FloatField()
    category = models.CharField(choices=[
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('shopping', 'Shopping'),
        ('entertainment', 'Entertainment'),
        ('bills', 'Bills'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description