from django.db import models

class JobOffer(models.Model):
    company_name = models.CharField(max_length = 50)
    company_email = models.EmailField()
    job_title = models.CharField(max_length = 60)
    job_description=models.TextField()
    salary=models.FloatField()
    city=models.CharField(max_length=35)
    state = models.CharField(max_length = 35)
    created_at=models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    def __str__(self)  :
        return self.company_name
    
    
    
    
    
