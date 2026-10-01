from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def ticket_attachment_path(instance, filename):
    """Generates a dynamic upload path for attachments based on ticket ID"""
    return f"tickets/ticket_{instance.id}/{filename}" if instance.id else f"tickets/unsorted/{filename}"


class Ticket(models.Model):
  
    REQUEST_TYPE_CHOICES = [
        ('HARDWARE', 'Hardware Issue (Laptop, Monitor, Mouse)'),
        ('SOFTWARE', 'Software Access (MS Office, IDEs, OS updates)'),
        ('NETWORK', 'Network & Wi-Fi Connectivity'),
        ('ACCOUNT', 'Account Password Reset / Lockout'),
        ('LOGIN','Login issue'),
        ('OTHER', 'Others (Specify below)'),
    ]

    
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

   
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('PENDING', 'Pending'),
        ('RESOLVED', 'Resolved'),
    ]

   
    title = models.CharField(max_length=200)
    
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES, default='HARDWARE', help_text="Select your request type from the dropdown")
    other_request_text = models.CharField( max_length=255,blank=True,null=True,help_text="If you selected 'Others', please specify here")
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES,default='MEDIUM')
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='OPEN')
    attachment = models.FileField( upload_to=ticket_attachment_path, blank=True,null=True,help_text="Attach the file")

    
    raised_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='my_tickets',
        help_text="The user who created this ticket"
    )
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] 
    def __str__(self):
        return f"Ticket #{self.id}: {self.title} ({self.status})"

    @property
    def age_in_days_and_hours(self):
        """
        Calculates and returns how long ago the ticket was created 
        in a human-readable days and hours format.
        """
        now = timezone.now()
        duration = now - self.created_at
        
        days = duration.days
        hours = duration.seconds // 3600

        if days == 0:
            return f"{hours} hour(s) ago"
        return f"{days} day(s), {hours} hour(s) ago"



