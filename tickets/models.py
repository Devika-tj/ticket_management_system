# from django.db import models
# from django.conf import settings


# class Ticket(models.Model):

#     ISSUE_CHOICES = [
#         ('HARDWARE', 'Hardware Issue'),
#         ('SOFTWARE', 'Software Issue'),
#         ('NETWORK', 'Network / Internet Issue'),
#         ('PRINTER', 'Printer / Scanner Issue'),
#         ('EMAIL', 'Email Issue'),
#         ('LOGIN', 'Login / Password Issue'),
#         ('WEBSITE', 'Website Issue'),
#         ('PORTAL', 'DTE Portal / Application Issue'),
#         ('DATABASE', 'Database / Data Issue'),
#         ('OTHER', 'Other'),
#     ]


#     created_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='tickets'
#     )

#     issue_type = models.CharField(
#         max_length=20,
#         choices=ISSUE_CHOICES
#     )

   
#     subject = models.CharField(
#         max_length=200
#     )


#     description = models.TextField()


#     # Automatically records when ticket was created
#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     def __str__(self):
#         return self.subject