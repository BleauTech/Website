from django.shortcuts import render
from .forms import ContactForm

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail




# Create your views here.
def home_view(request):
	context={}
	return render(request, 'base/index.html',context)


def about_view(request):
	context={}
	return render(request, 'base/about.html',context)

def contact_view(request):
	form=ContactForm()
	context={'form':form}

	if request.method=='POST':
		print(request.POST)
		form=ContactForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			email=form.cleaned_data['email']
			person_subject=form.cleaned_data['subject']
			message=form.cleaned_data['message']

			subject = 'Someone is contacting you from BleauTech site'
			context={'massage': message, 'subject':person_subject, 'email':email, 'name':name}
			html_message = render_to_string('base/mail_template.html', context)
			plain_message = strip_tags(html_message)

			sent=send_mail(subject=subject,
				message=plain_message,
				from_email='BleauTech',
				recipient_list=['esiebomaj@gmail.com', 'esiebomaje@gmail.com', 'bleauteche@gmail.com', 'rex4dom@gmail.com'],
				fail_silently=False,
				html_message=html_message )
			context={'sent':sent}


	return render(request, 'base/contact.html',context)

def project_view(request):
	context={}
	return render(request, 'base/project.html',context)

def services_view(request):
	context={}
	return render(request, 'base/services.html',context)



