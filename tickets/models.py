from django.conf import settings

from django.db import models
from django.conf import settings

class Department(models.Model):

    name=models.CharField(max_length=100,unique=True)
    is_active=models.BooleanField(default=True)

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name

class RequestType(models.Model):

    department=models.ForeignKey(Department,on_delete=models.CASCADE, related_name='request_types')
    name=models.CharField(max_length=20)
    is_active=models.BooleanField(default=True)

    class Meta:
        ordering=['name']

        constraints=[models.UniqueConstraint(fields=['department','name'],name='unique_request_per_department')] 

        def __str__(self):
            return self.name

class Ticket(models.Model):

    STATUS_CHOICES=[
        ('OPEN','Open'),
        ('IN_PROGRESS','In_Progress'),
        ('RESOLVED','Resolved'),
        ('CLOSED','Closed')
    ]

    PRIORITY_CHOICES=[
        ('URGENT','Urgent'),
        ('LOW','Low'),
        ('MEDIUM','Medium')
    ]
    ticket_no=models.PositiveIntegerField(unique=True,editable=False,null=True)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='tickets')
    title=models.CharField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.PROTECT,related_name='tickets')
    request_type=models.ForeignKey(RequestType,on_delete=models.PROTECT,related_name='tickets')
    other_request=models.CharField(max_length=100,blank=True)
    remarks=models.TextField(blank=True)
    status=models.CharField(max_length=30,choices=STATUS_CHOICES,default='Open')
    priority=models.CharField(max_length=30,choices=PRIORITY_CHOICES,default='Medium')
    assigned_to=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name='assigned_tickets',limit_choices_to={'role':'support'})

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_at']
    
    class TicketAttachment(models.Model):
        ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name='ticket_attachment')
    class TicketComment(models.Model):
        ticket_comment=models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name='ticket_comment')




































# from django.utils import timezone


# def ticket_attachment_path(instance, filename):
#     """Generates a dynamic upload path for attachments based on ticket ID"""
#     return f"tickets/ticket_{instance.id}/{filename}" if instance.id else f"tickets/unsorted/{filename}"




# class Ticket(models.Model):
  
#     REQUEST_TYPE_CHOICES = [
#         ('HARDWARE', 'Hardware Issue (Laptop, Monitor, Mouse)'),
#         ('SOFTWARE', 'Software Access (MS Office, IDEs, OS updates)'),
#         ('NETWORK', 'Network & Wi-Fi Connectivity'),
#         ('ACCOUNT', 'Account Password Reset / Lockout'),
#         ('LOGIN','Login issue'),
#         ('OTHER', 'Others (Specify below)'),
#     ]

    
#     PRIORITY_CHOICES = [
#         ('LOW', 'Low'),
#         ('MEDIUM', 'Medium'),
#         ('HIGH', 'High'),
#     ]

   
#     STATUS_CHOICES = [
#         ('OPEN', 'Open'),
#         ('PENDING', 'Pending'),
#         ('RESOLVED', 'Resolved'),
#         ('CLOSED','Closed')
#     ]

#     SECTION_CHOICES = [
#     ('ESTABLISHMENT', 'Establishment'),
#     ('PURCHASE', 'Purchase'),
#     ('FINANCE', 'Finance'),
#     ('GRADATION', 'Gradation'),
# ]

    
    

#     ticket_no=models.PositiveIntegerField(unique=True,editable=False,null=True)
#     title = models.CharField(max_length=200)
#     request_type = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES, default='HARDWARE', help_text="Select your request type from the dropdown")
#     other_request_text = models.CharField( max_length=255,blank=True,null=True,help_text="If you selected 'Others', please specify here")
#     priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES,default='MEDIUM')
#     status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='OPEN')
#     attachment = models.FileField( upload_to=ticket_attachment_path, blank=True,null=True,help_text="Attach the file")
#     section=models.ForeignKey(max_length=20,choices=SECTION_CHOICES,default='ESTABLISHMENT')
#     remarks=models.TextField(max_length=20,blank=True)
    
#     assigned_to=models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True
#         )

    

    
#     raised_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='my_tickets',
#         help_text="The user who created this ticket"
#     )


   
       
    
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

  
       

#     class Meta:
#         ordering = ['-created_at'] 
#     def __str__(self):
#         return f"Ticket #{self.id}: {self.title} ({self.status})"

#     @property
#     def age_in_days_and_hours(self):
#         """
#         Calculates and returns how long ago the ticket was created 
#         in a human-readable days and hours format.
#         """
#         now = timezone.now()
#         duration = now - self.created_at
        
#         days = duration.days
#         hours = duration.seconds // 3600

#         if days == 0:
#             return f"{hours} hour(s) ago"
#         return f"{days} day(s), {hours} hour(s) ago"

# class TicketComment(models.Model):
#     ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE, related_name='comments')
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ticket_comments')
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True) 

#     def __str__(self):
#         return f"Comment by {self.author.username} on Ticket #{self.ticket.id}"
    




<<<<<<< HEAD

class Department(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )


    is_active = models.BooleanField(
        default=True
    )


    class Meta:

        ordering = ['name']


    def __str__(self):

        return self.name


class RequestType(models.Model):

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='request_types'
    )


    name = models.CharField(
        max_length=150
    )


    is_active = models.BooleanField(
        default=True
    )


    class Meta:

        ordering = ['name']


        constraints = [
            models.UniqueConstraint(
                fields=[
                    'department',
                    'name'
                ],
                name='unique_request_per_department'
            )
        ]


    def __str__(self):

        return self.name


class Ticket(models.Model):

    STATUS_CHOICES = [

        (
            'open',
            'Open'
        ),

        (
            'in_progress',
            'In Progress'
        ),

        (
            'resolved',
            'Resolved'
        ),
    ]


    PRIORITY_CHOICES = [

        (
            'low',
            'Low'
        ),

        (
            'medium',
            'Medium'
        ),

        (
            'high',
            'High'
        ),
    ]


    ticket_no = models.PositiveIntegerField(
        unique=True,
        editable=False,
        null=True
    )


    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tickets'
    )


    title = models.CharField(
        max_length=200
    )


    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name='tickets'
    )


    request_type = models.ForeignKey(
        RequestType,
        on_delete=models.PROTECT,
        related_name='tickets'
    )


    other_request = models.CharField(
        max_length=255,
        blank=True
    )


    remarks = models.TextField(
        blank=True
    )


    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='open'
    )


    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='medium'
    )


    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tickets',
        limit_choices_to={
            'role': 'support'
        }
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    class Meta:

        ordering = [
            '-created_at'
        ]


    def save(self, *args, **kwargs):

        if self.ticket_no is None:

            last = Ticket.objects.order_by(
                '-ticket_no'
            ).first()


            self.ticket_no = (
                last.ticket_no + 1
                if last and last.ticket_no
                else 1
            )


        super().save(
            *args,
            **kwargs
        )


    def __str__(self):

        return f'TICKET-{self.ticket_no}'


class TicketAttachment(models.Model):

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='attachments'
    )


    file = models.FileField(
        upload_to='ticket_attachments/%Y/%m/'
    )


    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )


class TicketComment(models.Model):

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='comments'
    )


    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


    comment = models.TextField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        ordering = [
            'created_at'
        ]
=======
>>>>>>> 82df279bf52b0f355fac946df2c5d9634d173ff1
