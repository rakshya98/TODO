from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class TODO(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    is_completed=models.BooleanField()
    created_date=models.DateField(auto_now_add=True)  # object create garda aafei date time dinxa auto_now_add le , hamle date lehkiraakhnu parena
    updated_date=models.DateField(auto_now=True) # everytime object is modified , aafei date dinxa
    user=models.ForeignKey(User ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table='todo'
        verbose_name_plural="TODOes"
