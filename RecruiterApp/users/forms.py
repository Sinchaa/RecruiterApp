from django import forms
from crispy_forms.helper import FormHelper
from django.core.validators import RegexValidator,FileExtensionValidator,MinLengthValidator
from crispy_forms.layout import Layout, Submit, Row, Column
from django.core.exceptions import ValidationError
from crispy_forms.layout import Field
import os

class CustomCheckbox(Field):
    template = 'custom_checkbox.html'
STATES = (
    ('', 'Choose...'),
    ('MP', 'Madhya Pradesh'),
    ('KA', 'Karnataka'),
    ('RJ', 'Rajasthan'),
    ('UP', 'Uttar Pradesh'),
    ('MH', 'Maharashtra'),
    ('GJ', 'Gujarat')
)
DEGREES = (
    ('', 'Choose...'),
    ('BE', 'Bachelor of Engineering'),
    ('BTech', 'Bachelor of Technology'),
    ('BCA', 'Bachelor of Computer Application '),
    ('ME', 'Master of Engineering'),
    ('MTech', 'Master of Technology'),
    ('MCA', 'Master of Computer Application '),
    
)

class nameWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        super().__init__([
            forms.TextInput(attrs={'placeholder': 'John','pattern':'[A-Za-z ]+','title':'Enter Characters Only '}),
            forms.TextInput(attrs={'placeholder': 'Doe','pattern':'[A-Za-z ]+','title':'Enter Characters Only '})
        ], attrs)
    
    def decompress(self, value):
        if value:
            return value.split(' ')
        return ['','']

class nameField(forms.MultiValueField):

    widget = nameWidget
    def __init__(self,*args,**kwargs):

        fields=(
            forms.CharField(),
            forms.CharField()
        )
    
        super().__init__(fields,*args,**kwargs)
    
    def compress(self,data_list):
        # return ['fisrtname','lastname']
        return f'{data_list[0]}{data_list[1]}'

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
        

class ApplicationForm(forms.Form):
    
    name = nameField()
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder': 'johndoe@mail.com'}))
    dob = forms.DateField(required=True,widget=forms.TextInput(attrs={'placeholder': 'dd/mm/yyyy'}))
    phoneNo = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'placeholder': '1234567890','pattern':'[0-9]+','title':'Enter Numbers Only '}))
    First_Address =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Building No.1'}))
    Second_Address =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Street No.1'}))
    qualification = forms.ChoiceField(choices=DEGREES)
    skills=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Python, Java, C, C++'}))
    resume = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['email'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['dob'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['phoneNo'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['First_Address'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['Second_Address'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['qualification'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['skills'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['resume'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('phoneNo', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('dob', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('First_Address', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('Second_Address', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('qualification', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('skills', css_class='form-group col-md-4 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('resume', css_class='form-group col-md-4 mb-0'),

                css_class='form-row'
            ),
            Submit('Sign up', 'Submit', css_class='btn btn-primary')
        )