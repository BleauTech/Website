from django import forms





class ContactForm(forms.Form):
	
	name = forms.CharField(label=None, max_length=100,)
	email = forms.EmailField()
	subject = forms.CharField(required=False, max_length=100, )
	message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your massage here'}) )
	


