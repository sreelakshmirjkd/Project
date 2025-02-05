"""
URL configuration for ProjectNearby project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employeesapp import views

from django.conf import settings # image display
from django.conf.urls.static import static # image display

urlpatterns = [

    path('admin/', admin.site.urls),

    path('nearby/employee_registration/', views.EmployeeRegistrationView.as_view(), name="emp_reg"),

    path('nearby/employee/info/', views.CompleteDataView.as_view(), name="emp_com_info"),

    path('nearby/employee/<int:pk>/more_info/', views.DetailedDataView.as_view(), name="emp_more_info"),

    path('nearby/employee/<int:pk>/update_info/', views.UpdateDataView.as_view(), name="emp_update_info"),

    path('nearby/employee/<int:pk>/delete_info/', views.DeleteDataView.as_view(), name="emp_delete_info"),

    path('nearby/employee/personal_info/', views.PersonalInfoView.as_view(), name="emp_p_info"),

    path('nearby/employee/job_info/', views.JobInfoView.as_view(), name="emp_j_info"),

    path('nearby/employee/bankac_info/', views.BankacInfoView.as_view(), name="emp_bac_info"),

    path('nearby/employee/basic_info/', views.BasicInfoView.as_view(), name="emp_basic_info"),

    path('nearby/employee/signin/', views.SignInView.as_view(), name="emp_sign_in"),

    path('nearby/employee/signup/', views.SignUpView.as_view(), name="emp_sign_up"),

    path('nearby/employee/signout/', views.SignOutView.as_view(), name="emp_sign_out"),

    path('nearby/employee/profile/', views.EmpProfileView.as_view(), name="emp_profile"),

    path('nearby/employee/<int:pk>/profile/', views.AdminEmpProfileView.as_view(), name="admin_emp_profile"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # image display
