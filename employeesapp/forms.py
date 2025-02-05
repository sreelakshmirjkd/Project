from django import forms
from employeesapp.models import EmployeeRegistrationModel
from django.contrib.auth.models import User

class EmployeeRegistrationForm(forms.ModelForm):

    class Meta:

        model = EmployeeRegistrationModel

        fields = ["first_name","last_name","photo","job","date_of_birth", "age", "gender", "country_code", "phone", 
                  "emergency_contact", "email", "address_line_1", "address_line_2", "city", "district", "zip_code", "state",
                  "join_date", "min_charge", "job_state", "job_district", "job_taluk","job_village", 
                  "account_holder", "account_number", "bank_name", "branch", "swift_code"]

        # exclude = ["interview_date"]

        widgets = {

            "first_name": forms.TextInput(attrs={"class":"form-control mb-2"}),
 
            "last_name": forms.TextInput(attrs={"class":"form-control mb-2"}),

            # "full_name": forms.TextInput(attrs={"class":"form-control mb-2"}),

            

            # "employee_id": forms.TextInput(attrs={"class":"form-control mb-2"}),

            "job": forms.Select(attrs={"class":"form-select mb-2"}),

            # "dob_d": forms.Select(attrs={"class":"form-control mb-2"}),

            # "dob_m": forms.Select(attrs={"class":"form-control mb-2"}),

            # "dob_y": forms.Select(attrs={"class":"form-control mb-2"}),

            "date_of_birth": forms.DateInput(attrs={"type":"date","class": "form-control mb-2"}),

            "age": forms.NumberInput(attrs={"class":"form-control mb-2"}),

            "gender": forms.Select(attrs={"class":"form-select mb-2"}),

            "country_code": forms.Select(attrs={"class":"form-select mb-2"}),

            "phone": forms.TextInput(attrs={"class":"form-control mb-2"}),

            "emergency_contact": forms.TextInput(attrs={"class":"form-control mb-2"}),

            "email": forms.EmailInput(attrs={"class":"form-control mb-2"}),

            "address_line_1": forms.TextInput(attrs={"class":"form-control mb-2"}),

            "address_line_2": forms.TextInput(attrs={"class":"form-control mb-2"}),

            "city": forms.TextInput(attrs={"class":"form-control mb-2"}),

            "district": forms.Select(attrs={"class": "form-select mb-2"}),

            "zip_code": forms.TextInput(attrs={"class":"form-control mb-2"}),

            "state": forms.Select(attrs={"class":"form-select mb-2"}),

            # "interview_date": forms.DateInput(attrs={"type":"date","class":"form-control mb-2"}),


            "join_date": forms.DateInput(attrs={"type":"date","class":"form-control mb-2"}),

            "min_charge": forms.NumberInput(attrs={"class":"form-control mb-2"}),

            "join_state": forms.Select(attrs={"class":"form-select mb-2"}),

            "join_district": forms.Select(attrs={"class":"form-selectl mb-2"}),

            "join_taluk": forms.Select(attrs={"class":"form-select mb-2"}),

            "join_village": forms.Select(attrs={"class":"form-select mb-2"}),

            "account_holder": forms.TextInput(attrs={"class":"form-control mb-2"}),

            "account_number": forms.TextInput(attrs={"class":"form-control mb-2"}),

            "bank_name": forms.TextInput(attrs={"class":"form-control mb-2"}),

            "branch": forms.TextInput(attrs={"class":"form-control mb-2"}),

            "swift_code": forms.TextInput(attrs={"class":"form-control mb-2"}),
      

        }




class EmployeeSignUpForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ["username", "password"]

# Use Form to SignUp

class LoginForm(forms.Form):

    username = forms.CharField()

    password = forms.CharField()
