from django.db import models
from backend.models import User
from django.utils import timezone


class Minislot(models.Model):

    status = (
        ('WON', 'WON'),
        ('LOSS', 'LOSS'),
        ('PENDING', 'PENDING')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result1 = models.CharField(max_length=20)
    result2 = models.CharField(max_length=20)
    result3 = models.CharField(max_length=20)
    stake = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    status =  models.CharField(max_length=30, choices=status, default='PENDING')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"User: {self.user.email} ------ Result Sequence: {self.result1}-{self.result2}-{self.result3} ----- Amount: {self.amount}"
    
    def save(self, *args, **kwargs):
        if self.result1 == self.result2 and self.result3:
            self.amount = self.stake * 5
            self.user.balance += int(self.amount)
            self.user.save()
            self.status = 'WON'
        elif self.result1 == self.result2 or self.result2 == self.result3:
            self.amount = self.stake * 2
            self.user.balance += int(self.amount)
            self.user.save()
            self.status = 'WON'
        else:
            self.status = 'LOSS'

        super().save(*args, **kwargs)


class HeadorTail(models.Model):
    value = (
        ('HEAD', 'HEAD'),
        ('TAIL', 'TAIL')
    )

    opt = (
        ('PENDING', 'PENDING'),
        ('LOSS', 'LOSS'),
        ('WON', 'WON'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stake = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    option = models.CharField(max_length=50, choices=value, blank=True, null=True)
    outcome = models.CharField(max_length=50, choices=value, blank=True, null=True)
    status = models.CharField(max_length=50, choices=opt, default='PENDING')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"User: {self.user.email}------ Outcome: {self.outcome}-------- Winnings: {self.amount}"
    
    def save(self, *args, **kwargs):

        if self.option == self.outcome:
            self.amount = self.stake * 2
            self.user.balance += int(self.amount)
            self.user.save()
            self.status = 'WON'
        else:
            self.status = 'LOSS'
        super().save(*args, **kwargs)



class BottleSpin(models.Model):
    value = (
        ('UP', 'UP'),
        ('DOWN', 'DOWN')
    )

    opt = (
        ('PENDING', 'PENDING'),
        ('LOSS', 'LOSS'),
        ('WON', 'WON'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stake = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    option = models.CharField(max_length=50, choices=value, blank=True, null=True)
    outcome = models.CharField(max_length=50, choices=value, blank=True, null=True)
    status = models.CharField(max_length=50, choices=opt, default='PENDING')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"User: {self.user.email}------ Outcome: {self.outcome}-------- Winnings: {self.amount}"
    
    def save(self, *args, **kwargs):

        if self.option == self.outcome:
            self.amount = self.stake * 2
            self.user.balance += int(self.amount)
            self.user.save()
            self.status = 'WON'
        else:
            self.status = 'LOSS'
        super().save(*args, **kwargs)



class RockPapperSissors(models.Model):
    value = (
        ('ROCK', 'ROCK'),
        ('PAPER', 'PAPER'),
        ('SISSORS', 'SISSORS')
    )

    opt = (
        ('PENDING', 'PENDING'),
        ('LOSS', 'LOSS'),
        ('WON', 'WON'),
        ('DRAW', 'DRAW'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stake = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    option = models.CharField(max_length=50, choices=value, blank=True, null=True)
    outcome = models.CharField(max_length=50, choices=value, blank=True, null=True)
    status = models.CharField(max_length=50, choices=opt, default='PENDING')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"User: {self.user.email}------ Outcome: {self.outcome}-------- Winnings: {self.amount}"
    
        

    
    def save(self, *args, **kwargs):

        if self.option == 'ROCK' and self.outcome == 'SISSORS' or self.option == 'SISSORS' and self.outcome == 'PAPER' or self.option == 'PAPER' and self.outcome == 'ROCK':
            self.amount = self.stake * 2
            self.user.balance += int(self.amount)
            self.user.save()
            self.status = 'WON'
        elif self.option == self.outcome:
            self.status = 'Draw'
            self.user.balance += self.stake
            self.user.save()
        else:
            self.status = 'LOSS'
        super().save(*args, **kwargs)

    


