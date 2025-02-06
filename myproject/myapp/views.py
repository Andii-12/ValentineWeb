from django.shortcuts import render, redirect
from .models import ValentineMessage
from .models import LongTextSubmission

# from django.http import HttpResponse
# from .models import ValentineMessage  # Import your model
# from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def home2(request):
    return render(request, 'home2.html')

def home3(request):
    return render(request, 'home3.html')

def home4(request):
    return render(request, 'home4.html')

def home5(request):
    return render(request, 'home5.html')

def home6(request):
    return render(request, 'home6.html')


def save_message(request):
    if request.method == "POST":
        message_text = request.POST.get("message")
        if message_text:
            ValentineMessage.objects.create(text=message_text)
            return redirect("home3")  # Ensure 'home3' is defined in your URLs
    return render(request, "home2.html")  # If no message, stay on home2

# def home5_view(request):
#     if request.method == "POST":
#         long_text = request.POST.get("long_text")
#         if long_text:  # Ensure it's not empty
#             LongTextSubmission.objects.create(text=long_text)  # ✅ Use correct model
#             return redirect("home6")  # ✅ Redirect correctly

#     return render(request, "home5.html")

def home5_view(request):
    if request.method == "POST":
        long_text = request.POST.get("long_text")
        if long_text:  
            LongTextSubmission.objects.create(text=long_text)
            return redirect("home6")  # Redirect after submission
    return render(request, "home5.html")


# def save_message(request):
#     if request.method == "POST":
#         message_text = request.POST.get("message")  # Get input value
#         if message_text:
#             # Save to database
#             ValentineMessage.objects.create(text=message_text)
#             messages.success(request, "Message saved successfully!")
#             return redirect("home")  # Redirect to home after saving
#     return HttpResponse("Invalid request", status=400)