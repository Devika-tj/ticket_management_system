from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class AssignedTicket(models.Model):
    STATUS_CHOICES=[
        ('PENDING','Pending'),
        ('RESOLVED','Resolved'),
        ('OPEN','Open'),
        ('CLOSED','Closed')
    ]
    title=models.CharField(max_length=20)
    description=models.TextField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='OPEN')
    assigned_to=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True,blank=True,related_name='assigned_tickets')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_tickets')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"#{self.id}-{self.title}({self.status})"
    
