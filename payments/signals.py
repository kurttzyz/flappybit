from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Deposit, Withdrawal, TransactionHistory

# This signal verify whether to credit the 50 the referred user needs to deposit 200 before having 50
@receiver(post_save, sender=Deposit)
def handle_verified_payment(sender, instance, **kwargs):
    if instance.status == 'Verified' and instance.amount >= 200:
        # Check if the user has a referring user
        referring_user = instance.user.referred_by
        if referring_user:
            # Credit referral reward
            referral_reward = referring_user.reward_per_referral
            referring_user.referral_income += referral_reward
            referring_user.save()
            # Optionally log or notify
            print(f"Referral reward of {referral_reward} credited to {referring_user.username}.")


@receiver(post_save, sender=Deposit)
def createDepositHistory(instance, created, sender, **kwargs):
    if created:
        TransactionHistory.objects.create(user= instance.user, amount= instance.amount, status = instance.status, action='Deposit', date_created = instance.date_created, reference_number=instance.reference_number)

@receiver(post_save, sender=Withdrawal)
def createWithdrawalHistory(instance, created, sender, **kwargs):
    if created:
        TransactionHistory.objects.create(user= instance.user, amount= instance.amount, status = instance.status, action='Withdrawal', date_created = instance.date_created, reference_number=instance.reference_number)


@receiver(post_save, sender=Deposit)
def UpdateDepositHistorySave(sender, instance, created, **kwargs):
    if created == False:
        history  = TransactionHistory.objects.filter(reference_number=instance.reference_number).update(status = instance.status)

@receiver(post_save, sender=Withdrawal)
def UpdateWithdrawHistorySave(sender, instance, created, **kwargs):
    if created == False:
        history  = TransactionHistory.objects.filter(reference_number=instance.reference_number).update(status = instance.status)