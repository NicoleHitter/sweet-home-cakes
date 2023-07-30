from django.shortcuts import render
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string

from .forms import FeedbackForm



def feedback(request):
    """
    Customers can send a message with the form
    """

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()

           

    form = FeedbackForm

    context = {
        'form': form,
    }

    template = 'feedback/feedback.html'

    return render(request, template, context)
