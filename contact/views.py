from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail


from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            messages.info(
                request,
                "Your enquiry has been registered, we will respond soon"
            )
            # send email to user
            subject = "Thank you for your enquiry"
            body = f"Dear {cd['name']} , we will respond soon"
            send_mail(
                subject,
                body,
                "amcneill83@gmail.com",
                [
                    cd["email"],
                ],
                fail_silently=False,
            )
            # inform admin of new enquiry
            subject_admin = "Attention - new enquiry"
            body_admin = "Check admin panel, a new enquiry has been received!"
            send_mail(
                subject_admin,
                body_admin,
                "amcneill83@gmail.com",
                [
                    "amcneill83@gmail.com",
                ],
                fail_silently=False,
            )
    else:
        form = ContactForm()
    return render(request, "contact/contact.html/", {"form": form})


def subscribe_sign_up(request):
    return render(request, "contact/subscribe.html/")