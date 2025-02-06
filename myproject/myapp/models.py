# from django.db import models

# class Message(models.Model):
#     text = models.TextField()  # Store the message text
#     created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

#     def __str__(self):
#         return self.text[:50]  # Show first 50 characters

from django.db import models

class ValentineMessage(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class LongTextSubmission(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]  # Show first 50 characters in admin