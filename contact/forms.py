from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    # fname = forms.CharField(
    #     label='First Name',
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    #
    # lname = forms.CharField(
    #     label='Last Name',
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )


    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {'First_name': forms.TextInput(attrs={'class': 'forms-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'forms-control'}),
                   'Subject': forms.TextInput(attrs={'class': 'forms-control'}),
                   'Email': forms.EmailInput(attrs={'class': 'forms-control'}),
                   'Message': forms.Textarea(attrs={'class': 'forms-control'})}
