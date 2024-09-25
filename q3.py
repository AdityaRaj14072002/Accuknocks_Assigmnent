"""Ans: Yes, Django signals run in the same database transaction as the caller, meaning if the transaction fails, the signal does not get executed."""

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save)
def signal_receiver(sender, instance, **kwargs):
    print("Signal running in transaction")
    if transaction.get_autocommit():
        print("No active transaction")
    else:
        print("Signal in transaction")

# Code to save an instance wrapped in a transaction block
with transaction.atomic():
    # Save the instance here
    pass

#In the signal receiver, if transaction.get_autocommit() is False, it confirms the signal runs in the transaction context.