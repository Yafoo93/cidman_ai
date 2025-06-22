from django.db import models

# Create your models here.
class Case(models.Model):
    case_number = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.case_number
