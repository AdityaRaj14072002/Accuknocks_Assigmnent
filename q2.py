"""Ans: Yes, by default, Django signals run in the same thread as the caller.
i can prove this by printing the thread details in both the caller and the signal:"""

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver

def save_model_instance():
    print(f"Caller thread: {threading.current_thread().name}")
    # Code to save the instance

@receiver(post_save)
def signal_receiver(sender, instance, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")

# When you save the model, you should see the same thread name for both the caller and the signal.
