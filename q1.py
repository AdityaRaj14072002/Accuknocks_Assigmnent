""" ANS: By default, Django signals are executed synchronously.
To prove this, here’s a code snippet that demonstrates this behavior:"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from time import sleep

@receiver(post_save)
def signal_receiver(sender, instance, **kwargs):
    print("Signal started")
    sleep(5)  # Simulates a long-running task
    print("Signal finished")

# Now, create or save a model instance
# If signals were asynchronous, the process wouldn't wait for 5 seconds.
# Instead, it blocks for 5 seconds proving the synchronous nature of signals.

# Note: The sleep function halts execution for 5 seconds, proving that signals are processed synchronously.