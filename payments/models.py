from django.db import models
from backend.models import User
# Create your models here.

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Maya', 'Maya'),
        ('GCash', 'GCash'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Verified', 'Verified'),
        ('Rejected', 'Rejected'),
    ]

    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    amount           = models.DecimalField(max_digits=10, decimal_places=2)
    action           = models.CharField(max_length=20, choices=STATUS_CHOICES)
    reference_number = models.CharField(max_length=50)
    status           = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    payment_method   = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='Gcash')
    date_created     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.reference_number} - {self.status} ({self.payment_method})"
    

class Withdrawal(models.Model):
    PENDING  = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]
    
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    amount         = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    phone_number   = models.CharField(max_length=15)
    status         = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)  # Default status
    action         = models.CharField(max_length=20, choices=STATUS_CHOICES, default="withdraw")
    created_at     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.status}"

    def approve_withdrawals(self, request, queryset):
        for withdrawal in queryset.filter(status='Pending'):  # Match model default
            if withdrawal.amount <= withdrawal.user.balance:
                withdrawal.status = 'Approved'
                withdrawal.user.balance.save()
                withdrawal.save()
        self.message_user(request, "Selected withdrawals have been approved.")
    approve_withdrawals.short_description = "Approve selected withdrawals"

    def reject_withdrawals(self, request, queryset):
        updated = queryset.filter(status='Pending').update(status='Rejected')  # Match model default
        self.message_user(request, f"{updated} withdrawal(s) marked as Rejected.")
    reject_withdrawals.short_description = "Reject selected withdrawals"