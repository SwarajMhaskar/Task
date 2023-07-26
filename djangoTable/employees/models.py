from django.db import models

class TableRow(models.Model):
    emp_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    department = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"{self.emp_id}: {self.name}"
