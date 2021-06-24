  
from celery import task
from django.core.mail import send_mail

@task
def comment_placed(user):

    message = ('user '+ user.id+' has plased a comment right now')
    mail_sent = send_mail(user.id,
                          message,
                          'daniil.halytskyi@gmail.com',
                          [order.email])
    return mail_sent