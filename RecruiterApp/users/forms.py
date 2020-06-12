from django import forms
from crispy_forms.helper import FormHelper
from django.core.validators import RegexValidator
from crispy_forms.layout import Layout, Submit, Row, Column
from django.core.exceptions import ValidationError
from crispy_forms.layout import Field
from django.core.validators import MinLengthValidator

class CustomCheckbox(Field):
    template = 'custom_checkbox.html'
STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class RegistrationForm(forms.Form):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name','pattern':'[A-Za-z ]+','title':'Enter Characters Only '}))
    email = forms.EmailField(required=True)
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Present Institute/Company'})
    )
    state = forms.ChoiceField(choices=STATES)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['email'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['company'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['state'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['password'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['confirm_password'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column(css_class='form-control form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('company', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('password', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('confirm_password', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            Submit('Sign up', 'Submit', css_class='btn btn-primary')
        )

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['password'].widget.attrs['style'] = 'width:100%; height:40px;'
       
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email'),
                Column(css_class='form-control form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            
            Submit('Sign in', 'Submit', css_class='btn btn-primary')
        )
    
class EmailVerifyForm(forms.Form):
    
    email = forms.EmailField(required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
           
            Submit('Sign up', 'Submit', css_class='btn btn-primary')
        )
