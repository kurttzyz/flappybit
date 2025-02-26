from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site


def DepositConfirmationMail(request, data):
    email_subject = 'Deposit has been made'
    email_body =  render_to_string('email/depositmail.html',{
        'first_name':data.user.first_name,
        'last_name': data.user.last_name,
        'wallet': data.payment_method.name,
        'amount': data.amount,
        'reference': data.reference_number,
        'deposit_type': data.promo,
        'email': data.user.email,
        'date': data.payment_method,
        'pk': data.pk,
        'domain': request.get_host(),
        'protocol': request.scheme
    })
    email = EmailMessage(subject=email_subject, body=email_body,
        from_email='TestMail <info.testmail@zohomail.com>', to=['kurtmartin11262004@gmail.com',]
        )
    email.content_subtype = 'html'
    email.send()