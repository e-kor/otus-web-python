import logging

import dramatiq
from django.conf import settings
from django.core.mail import send_mail


@dramatiq.actor
def send_contact_mail(contact_email, body):
    subj = f"contact email from {contact_email}"
    _, admin_emails = zip(*settings.ADMINS)
    emails = [contact_email, *admin_emails]
    send_mail(subj, body, settings.DEFAULT_FROM_EMAIL, emails, )
    logging.info('sent emails to %s with body %s', emails, body)
