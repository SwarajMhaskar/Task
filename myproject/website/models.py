from django.db import models

class Emp(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Salary=models.CharField(max_length=100)
    DOJ=models.DateField()

    def __str__(self) :
        return self.id + ' ' + self.Name 
    
