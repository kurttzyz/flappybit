from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Payment

# This signal verify whether to credit the 50 the referred user needs to deposit 200 before having 50
@receiver(post_save, sender=Payment)
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