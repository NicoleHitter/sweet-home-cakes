from django.shortcuts import render
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string

from .models import Address
from .forms import FeedbackForm


def feedback(request):
    """
    User can send message through the form
    """

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()

            # Confirmation email is sent on submission of form
          
            name = form.cleaned_data['name']
            original_message = form.cleaned_data['message']
            message = render_to_string(
                'feedback/confirmation_email/confirmation_email.txt', {
                    'name': name,
                    'original_message': original_message
                })
            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = [form.cleaned_data['email']]
            subject = 'Feedback'

            send_mail( 
                subject, 
                message,
                email_from,  
                email_to,                
            )

            messages.success(request, 'Message submitted successfully \
                A confirmation email is sent with original message')

    form = FeedbackForm
    company_address = Address.objects.all()

    context = {
        'form': form,
        'company_address': company_address,
    }

    template = 'feedback/feedback.html'

    return render(request, template, context)