from django.shortcuts import render

from django.core.mail import EmailMessage
def home(request):
    return render(request, 'home.html')


email = EmailMessage(
    'Hello',
    'Body goes here',
    'murali123manyam@gmail.com',
    ['to1@example.com', 'to2@example.com'],
    ['bcc@example.com'],
    reply_to=['another@example.com'],
    headers={'Message-ID': 'foo'},
)

from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings


def sendMail(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sending an email with Django"
            message = cd['message']

            # send the email to the recipent
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])

            # set the variable initially created to True
            messageSent = True

    else:
        form = EmailForm()

    return render(request, 'sendmail.html', {

        'form': form,
        'messageSent': messageSent,

    })