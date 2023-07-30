from django.shortcuts import render
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string

from .forms import ContactForm


def contact(request):
    """
    User can send message through the form
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            # Confirmation email is sent on submission of form
          
            name = form.cleaned_data['name']
            original_message = form.cleaned_data['message_body']
            message = render_to_string(
                'contact/confirmation_msg/confirmation_msg.txt', {
                    'name': name,
                    'original_message': original_message
                })
            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = [form.cleaned_data['email']]
            subject = 'Contact'

            send_mail( 
                subject, 
                message,
                email_from,  
                email_to,                
            )

            messages.success(request, 'Message submitted successfully \
                A confirmation email is sent with original message')

    form = ContactForm

    context = {
        'form': form,
    }

    template = 'contact/contact.html'

    return render(request, template, context)