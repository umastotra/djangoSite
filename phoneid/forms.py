from django import forms

class ContactPlusForm(forms.Form):
    phone_number = forms.CharField(label='Phone Number', max_length=100)
    zip = forms.CharField(label='Zip Code', max_length=100)

    def clean(self):
        cleaned_data = super(ContactPlusForm, self).clean()
        phone_number = cleaned_data.get('phone_number')
        zip = cleaned_data.get('zip')
        if not phone_number and not zip:
            raise forms.ValidationError('Phone Number and Zip Code are required!')