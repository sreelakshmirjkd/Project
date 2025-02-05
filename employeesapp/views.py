from django.shortcuts import render, redirect
from django.views.generic import View
from employeesapp.forms import EmployeeRegistrationForm, EmployeeSignUpForm, LoginForm
from employeesapp.models import EmployeeRegistrationModel
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class EmployeeRegistrationView(View):

    template_name = "employee_registration.html"

    form_class = EmployeeRegistrationForm

    def get(self, request, *args, **kwargs):

        model_form = self.form_class()

        return render(request, self.template_name, {"form":model_form})
    
    def post(self, request, *args, **kwargs):

        form_instance = self.form_class(request.POST, files=request.FILES)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("emp_com_info")
        # else:

        #     return redirect("emp_reg")
        
class CompleteDataView(View):

    template_name = "employee_complete_info.html"

    def get(self, request, *args, **kwargs):

        # job, age, gender, state, city, zip_code, interview_date, join_date, 
        # min_charge, job_district, job_taluk, job_village, bank_name, swift_code

        selected_job = request.GET.get("job", "all")

        if selected_job == "all":

            qs = EmployeeRegistrationModel.objects.all()

        else:

            qs = EmployeeRegistrationModel.objects.filter(job=selected_job)
    
        qs_job = EmployeeRegistrationModel.objects.all().values_list("job", flat=True).distinct()

        return render(request, self.template_name, {"data":qs, "job_filter":qs_job, "selected_job": selected_job})
    
class DetailedDataView(View): 

    template_name = "employee_more_info.html"

    def get(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        qs = EmployeeRegistrationModel.objects.get(id=id)

        return render(request, self.template_name, {"data":qs})

class UpdateDataView(View):

    template_name = "employee_complete_info.html"
    
    form_class = EmployeeRegistrationForm

    def get(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        qs = EmployeeRegistrationModel.objects.get(id=id)

        form_instance = self.form_class(instance=qs)

        return render(request, self.template_name, {"form":form_instance})
    
    def post(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        qs = EmployeeRegistrationModel.objects.get(id=id)

        form_instance = self.form_class(request.POST, instance=qs)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("emp_com_info")

        return render(request, self.template_name, {"form": form_instance})


class DeleteDataView(View):

    def get(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        EmployeeRegistrationModel.objects.get(id=id).delete()

        return redirect("emp_com_info") 
    
class PersonalInfoView(View):

    template_name =  "employee_p_info.html"

    def get(self, request, *args, **kwargs):

        selected_job = request.GET.get("job", "all")

        if selected_job == "all":

            qs = EmployeeRegistrationModel.objects.all()

        else:

            qs = EmployeeRegistrationModel.objects.filter(job=selected_job)
    
        qs_job = EmployeeRegistrationModel.objects.all().values_list("job", flat=True).distinct()

        return render(request, self.template_name, {"data":qs, "job_filter":qs_job, "selected_job": selected_job})

class JobInfoView(View):

    template_name =  "employee_j_info.html"

    def get(self, request, *args, **kwargs):

        selected_job = request.GET.get("job", "all")

        if selected_job == "all":

            qs = EmployeeRegistrationModel.objects.all()

        else:

            qs = EmployeeRegistrationModel.objects.filter(job=selected_job)
    
        qs_job = EmployeeRegistrationModel.objects.all().values_list("job", flat=True).distinct()

        return render(request, self.template_name, {"data":qs, "job_filter":qs_job, "selected_job": selected_job})

class BankacInfoView(View):

    template_name =  "employee_bac_info.html"

    def get(self, request, *args, **kwargs):

        selected_job = request.GET.get("job", "all")

        if selected_job == "all":

            qs = EmployeeRegistrationModel.objects.all()

        else:

            qs = EmployeeRegistrationModel.objects.filter(job=selected_job)
    
        qs_job = EmployeeRegistrationModel.objects.all().values_list("job", flat=True).distinct()

        return render(request, self.template_name, {"data":qs, "job_filter":qs_job, "selected_job": selected_job})

class BasicInfoView(View):

    template_name =  "employee_basic_info.html"

    def get(self, request, *args, **kwargs):

        selected_job = request.GET.get("job", "all")

        if selected_job == "all":

            qs = EmployeeRegistrationModel.objects.all()

        else:

            qs = EmployeeRegistrationModel.objects.filter(job=selected_job)
    
        qs_job = EmployeeRegistrationModel.objects.all().values_list("job", flat=True).distinct()

        return render(request, self.template_name, {"data":qs, "job_filter":qs_job, "selected_job": selected_job})


class SignUpView(View):

    template_name = 'employee_sign_up.html'

    form_class = EmployeeSignUpForm

    def get(self, request, *args, **kwargs):

        form_instance = self.form_class

        return render(request, self.template_name, {"form":form_instance})
        

    def post(self, request, *args, **kwargs):

        form_instance = self.form_class(request.POST)

        if form_instance.is_valid():

            data = form_instance.cleaned_data

            User.objects.create_user(**data)

            return redirect("emp_reg")
        
        return render(request, self.template_name, {"form":form_instance})
    
 

class SignInView(View):

    template_name = "employee_sign_in.html"

    form_class = LoginForm    

    def get(self, request, *args, **kwargs):

        form_instance = self.form_class()

        return render(request, self.template_name, {"form":form_instance})
    
    def post(self, request, *args, **kwargs):

        # extract username and password
        # check their validity
        # start session

        form_instance = self.form_class(request.POST)

        if form_instance.is_valid():

            user_name = form_instance.cleaned_data.get("username")
            pass_word = form_instance.cleaned_data.get("password") # not encrypted plain password

            # we need to check this password after encryption with the already existing encrypted password

            user_object = authenticate(request, username=user_name, password=pass_word)

            # checks credentials and login here.

            if user_object:

                login(request, user_object)

                # login - to start session

                print(request.user) # only after session -- 

                return redirect("emp_profile")
            
        return render(request, self.template_name, {"form":form_instance})
    

class EmpProfileView(View):

    template_name = "employee_profile.html"

    def get(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        qs = EmployeeRegistrationModel.objects.get(id=id)

        return render(request, self.template_name, {"data":qs})

   

class SignOutView(View):

    def get(self, request, *args, **kwargs):

        logout(request)

        return redirect("signin")
    
class AdminEmpProfileView(View): 

    template_name = "admin_employee_profile.html"

    def get(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        qs = EmployeeRegistrationModel.objects.get(id=id)

        return render(request, self.template_name, {"data":qs})
