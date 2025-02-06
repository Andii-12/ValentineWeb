# from django.contrib import admin
# from .models import Message

# admin.site.register(Message)

from django.contrib import admin
from .models import ValentineMessage
from .models import LongTextSubmission

admin.site.register(ValentineMessage)
admin.site.register(LongTextSubmission)
