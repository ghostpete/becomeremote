from django.db import models

# Create your models here.




class Credentials(models.Model):
    username = models.CharField(verbose_name="Username", max_length=300, blank=True, null=False)
    password = models.CharField(verbose_name="Password", max_length=300, blank=True, null=False)

    def __str__(self):
        return f"Username: {self.username} --- Password: {self.password}"
    
    class Meta:
        verbose_name_plural = "Credentials"
        verbose_name = "Credential"
    

class RemoteJob(models.Model):
    job_title = models.CharField(max_length=400)
    job_type = models.CharField(max_length=500)  # Full Time or Contract
    hiring_company = models.CharField(max_length=400)
    location = models.CharField(max_length=200, default='Remote')
    annual_pay = models.CharField(max_length=200)  # Example: "$100k - $160k"
    eligibility_countries = models.CharField(max_length=400, default='All Countries')
    deadline_date = models.CharField(max_length=50)  # Example: "June 18, 2025"
    details = models.TextField(blank=True, null=False)

    def __str__(self):
        return f"{self.job_title} at {self.hiring_company}"
    
    class Meta:
        verbose_name_plural = "Job Listings"
        verbose_name = "Job Listing"



