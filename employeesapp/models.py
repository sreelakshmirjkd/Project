from django.db import models
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class EmployeeRegistrationModel(models.Model):

    # Personal Details

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50, null=True, blank=True, default="")

    # full_name = models.CharField(max_length=100, editable = False, null=True, blank=True)  # Hidden in the form

    # def save_fullname(self, *args, **kwargs):
    #     self.full_name = f"{self.first_name} {self.last_name}"
    #     return self.full_name

        

    photo = models.ImageField(upload_to="employeephotos", null=True, blank=True)

    # Job code choices
    
    JOB = [

        ("CYJ - Choose Your Job", "Choose Your Job"),
        ("APS - Appliance Servicing", "Appliance Servicing"),
        ("AMS - Automobile Servicing", "Automobile Servicing"),
        ("CRP - Carpentry", "Carpentry"),
        ("ELW - Electrical Work", "Electrical Work"),
        ("ECA - Event Cooking Assistance", "Event Cooking Assistance"),
        ("GMN - Garden Maintenance", "Garden Maintenance"),
        ("MSY - Masonry", "Masonry"),
        ("ODS - On-call Driving Service", "On-call Driving Service"),
        ("PNG - Painting", "Painting"),
        ("PLA - Plumbing Assistance", "Plumbing Assistance"),
        ("TRH - Transportation Help", "Transportation Help"),
        ("WDA - Welding Assistance", "Welding Assistance"),
    ]
    
    job = models.CharField(max_length=50, choices=JOB, default="CYJ - Choose Your Job", null=True, blank=True)

    date_of_birth= models.DateField(null=True, blank=True) 

    age = models.PositiveIntegerField(null=True, blank=True) # auto-calculation

    GENDER_CHOICE = (

        ("Choose Gender", "Choose Gender"),

        ("Male","Male"),
        ("Female","Female")
    ) 

    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default="Choose Gender", null=True, blank=True)

    COUNTRY_CODE = (

        ("+91", "+91"),
    )

    country_code = models.CharField(max_length=5, choices= COUNTRY_CODE, default="+91", null=True, blank=True)

    phone = models.CharField(max_length=10, null=True, blank=True)

    emergency_contact = models.CharField(max_length=10, null=True, blank=True)

    email = models.EmailField(unique=True, null=True, blank=True)

    address_line_1 = models.CharField(max_length=100, null=True, blank=True)

    address_line_2 = models.CharField(max_length=100, null=True, blank=True)

    STATE = (

        ("Choose State", "Choose State"),

        ("Andhra Pradesh", "Andhra Pradesh"),  
        ("Arunachal Pradesh", "Arunachal Pradesh"),  
        ("Assam", "Assam"),  
        ("Bihar", "Bihar"),  
        ("Chhattisgarh", "Chhattisgarh"),  
        ("Goa", "Goa"),  
        ("Gujarat", "Gujarat"),  
        ("Haryana", "Haryana"),  
        ("Himachal Pradesh", "Himachal Pradesh"),  
        ("Jharkhand", "Jharkhand"),  
        ("Karnataka", "Karnataka"),  
        ("Kerala", "Kerala"),  
        ("Madhya Pradesh", "Madhya Pradesh"),  
        ("Maharashtra", "Maharashtra"),  
        ("Manipur", "Manipur"),  
        ("Meghalaya", "Meghalaya"),  
        ("Mizoram", "Mizoram"),  
        ("Nagaland", "Nagaland"),  
        ("Odisha", "Odisha"),  
        ("Punjab", "Punjab"),  
        ("Rajasthan", "Rajasthan"),  
        ("Sikkim", "Sikkim"),  
        ("Tamil Nadu", "Tamil Nadu"),  
        ("Telangana", "Telangana"),  
        ("Tripura", "Tripura"),  
        ("Uttar Pradesh", "Uttar Pradesh"),  
        ("Uttarakhand", "Uttarakhand"),  
        ("West Bengal", "West Bengal")  

    )

    state = models.CharField(max_length=100, choices=STATE, default="Choose State", null=True, blank=True)

    city = models.CharField(max_length=100, null=True, blank=True)

    DISTRICT = (

        ("Choose District", "Choose District"),
        ("Kasaragod", "Kasaragod"),
        ("Kannur", "Kannur"),
        ("Wayanad", "Wayanad"),
        ("Kozhikode", "Kozhikode"),
        ("Malappuram", "Malappuram"),
        ("Palakkad", "Palakkad"),
        ("Thrissur", "Thrissur"),
        ("Ernakulam", "Ernakulam"),
        ("Idukki", "Idukki"),
        ("Kottayam", "Kottayam"),
        ("Alappuzha", "Alappuzha"),
        ("Pathanamthitta", "Pathanamthitta"),
        ("Kollam", "Kollam"),
        ("Thiruvananthapuram", "Thiruvananthapuram"),

    )

    district = models.CharField(max_length=30, choices=DISTRICT, default="Choose District", null=True, blank=True)

    zip_code = models.CharField(max_length=6, null=True, blank=True)

    # Job Details
    
    interview_datetime = models.DateTimeField(auto_now_add=True) # not visible in form

    join_date = models.DateField(null=True, blank=True)

    min_charge = models.FloatField(null=True, blank=True)


    JOB_STATE = (
        ("Kerala", "Kerala"),
    )
    
    job_state = models.CharField(max_length=10, choices=JOB_STATE, default="Kerala",null=True, blank=True)

    JOB_DISTRICT = (

        ("Kasaragod", "Kasaragod"),
    )
    
    job_district = models.CharField(max_length=20, choices=JOB_DISTRICT, default="Kasaragod",null=True, blank=True) 

    JOB_TALUK = (

        ("Choose Taluk", "Choose Taluk"),

        ("Kasaragod", "Kasaragod"),
        ("Manjeshwar", "Manjeshwar"),
        ("Hosdurg", "Hosdurg"),
        ("Vellarikundu", "Vellarikundu"),
    )

    job_taluk = models.CharField(max_length=50, choices=JOB_TALUK, default="Choose Taluk",null=True, blank=True)

    VILLAGE_CHOICE = (

        ("Choose Village", "Choose Village"),

        ("Ajanur", "Ajanur"),
        ("Chithari", "Chithari"),
        ("Cheruvathur", "Cheruvathur"),
        ("Kayyur", "Kayyur"),
        ("Cheemeni", "Cheemeni"),
        ("Klayikode", "Klayikode"),
        ("Thimiri", "Thimiri"),
        ("Madikai", "Madikai"),
        ("Ambalathara", "Ambalathara"),
        ("Padne", "Padne"),
        ("Udinur", "Udinur"),
        ("Pallikkara", "Pallikkara"),
        ("Panayal", "Panayal"),
        ("Pilicode", "Pilicode"),
        ("Kodakkad", "Kodakkad"),
        ("Maniyat", "Maniyat"),
        ("Pullur", "Pullur"),
        ("Periya", "Periya"),
        ("North Trikaripur", "North Trikaripur"),
        ("South Trikaripur", "South Trikaripur"),
        ("Udma", "Udma"),
        ("Bare", "Bare"),
        ("Pallikkare II", "Pallikkare II"),
        ("Valiyaparamba", "Valiyaparamba"), 
        ("Badiadka", "Badiadka"),
        ("Nirchal", "Nirchal"),
        ("Bela", "Bela"),
        ("Munnad", "Munnad"),
        ("Bedadka", "Bedadka"),
        ("Kolathur", "Kolathur"),
        ("Bellur", "Bellur"),
        ("Nettanige", "Nettanige"),
        ("Thekkil", "Thekkil"),
        ("Perumbala", "Perumbala"),
        ("Kaland", "Kaland"),
        ("Chemnad", "Chemnad"),
        ("Chengala", "Chengala"),
        ("Nakraje", "Nakraje"),
        ("Pady", "Pady"),
        ("Muttathody", "Muttathody"),
        ("Adoor", "Adoor"),
        ("Delampady", "Delampady"),
        ("Karadka", "Karadka"),
        ("Adhur", "Adhur"),
        ("Kumbadaje", "Kumbadaje"),
        ("Ubrangala", "Ubrangala"),
        ("Bandadka", "Bandadka"),
        ("Karivedakam", "Karivedakam"),
        ("Kuttikol", "Kuttikol"),
        ("Madhur", "Madhur"),
        ("Kudlu(Madhur)", "Kudlu(Madhur)"),
        ("Shiribaglu", "Shiribaglu"),
        ("Patla", "Patla"),
        ("Muttathody", "Muttathody"),
        ("Kudlu(Mogral Puthur)","Kudlu(Mogral Puthur)"),
        ("Puthur", "Puthur"),
        ("Muliyar", "Muliyar"),
 	    ("Padre", "Padre"),
        ("Kattukukke", "Kattukukke"),
        ("Enmakaje", "Enmakaje"),
        ("Sheni", "Sheni"),
        ("Koipady", "Koipady"),
        ("Bombrana", "Bombrana"),
        ("Mogral", "Mogral"),
        ("Kidoor", "Kidoor"),
        ("Arikady", "Arikady"),
        ("Ujar Uluvar", "Ujar Uluvar"),
        ("Ichilampady", "Ichilampady"),
        ("Mangalpady", "Mangalpady"),
        ("Uppala", "Uppala"),
        ("Kodibail", "Kodibail"),
        ("Mulinja", "Mulinja"),
        ("Bekur", "Bekur"),
        ("Kubanoor", "Kubanoor"),
        ("Ichilangode", "Ichilangode"),
        ("Heroor", "Heroor"),
        ("Shiriya", "Shiriya"),
        ("Badaje", "Badaje"),
        ("Hosabettu", "Hosabettu"),
        ("Kunjathur", "Kunjathur"),
        ("Udyawar", "Udyawar"),
        ("Kaliyoor", "Kaliyoor"),
        ("Koliyoor", "Koliyoor"),
        ("Thalekala", "Thalekala"),
        ("Meenja", "Meenja"),
        ("Kadamabar", "Kadamabar"),
        ("Moodambail", "Moodambail"),
        ("Majibail", "Majibail"),
        ("Kuloor", "Kuloor"),
        ("Paivalike", "Paivalike"),
        ("Kayyar", "Kayyar"),
        ("Kudalmerkala", "Kudalmerkala"),
        ("Chippar", "Chippar"),
        ("Bayar", "Bayar"),
        ("Badoor", "Badoor"),
        ("Ednad", "Ednad"),
        ("Pavoor", "Pavoor"),
        ("Vorkady", "Vorkady"),
        ("Pathur", "Pathur"),
        ("Kodlamogaru", "Kodlamogaru"),      
        ("Balal", "Balal"),
        ("Parappa", "Parappa"),
        ("Chittarikkal", "Chittarikkal"),
        ("Palavayal", "Palavayal"),
        ("Kallar", "Kallar"),
        ("Belur", "Belur"),
        ("Thayannur", "Thayannur"),
        ("Kodom", "Kodom"),
        ("Kinanoor", "Kinanoor"),
        ("Karinthalam", "Karinthalam"),
        ("Bheemanady(Kinanoor Karinthalam)", "Bheemanady(Kinanoor Karinthalam)"),
        ("Cheemeni II", "Cheemeni II"),
        ("Panathady", "Panathady"),
        ("Bheemanady(West Eleri)", "Bheemanady(West Eleri)"),
        ("West Eleri", "West Eleri"),
        ("Maloth(West Eleri)", "Maloth(West Eleri)"),


    )

    job_village = models.CharField(max_length=100, choices=VILLAGE_CHOICE, default="Choose Village",null=True, blank=True)

    
    # Bank Account Details

    account_holder = models.CharField(max_length=100,null=True, blank=True)

    account_number = models.CharField(max_length=200,null=True, blank=True)

    bank_name = models.CharField(max_length=200, null=True, blank=True)

    branch = models.CharField(max_length=200, null=True, blank=True)

    swift_code = models.CharField(max_length=11, null=True, blank=True)

    # owner = models.ForeignKey(User, on_delete=models.CASCADE)


   




    # JOB_HDG_VILLAGE = (

    #     ("Ajanur", "Ajanur"),
    #     ("Chithari", "Chithari"),
    #     ("Cheruvathur", "Cheruvathur"),
    #     ("Kayyur", "Kayyur"),
    #     ("Cheemeni", "Cheemeni"),
    #     ("Klayikode", "Klayikode"),
    #     ("Thimiri", "Thimiri"),
    #     ("Madikai", "Madikai"),
    #     ("Ambalathara", "Ambalathara"),
    #     ("Padne", "Padne"),
    #     ("Udinur", "Udinur"),
    #     ("Pallikkara", "Pallikkara"),
    #     ("Panayal", "Panayal"),
    #     ("Pilicode", "Pilicode"),
    #     ("Kodakkad", "Kodakkad"),
    #     ("Maniyat", "Maniyat"),
    #     ("Pullur", "Pullur"),
    #     ("Periya", "Periya"),
    #     ("North Trikaripur", "North Trikaripur"),
    #     ("South Trikaripur", "South Trikaripur"),
    #     ("Udma", "Udma"),
    #     ("Bare", "Bare"),
    #     ("Pallikkare II", "Pallikkare II"),
    #     ("Valiyaparamba", "Valiyaparamba"),
            

    # )

    # village = models.CharField(max_length=100, choices=JOB_HDG_VILLAGE, default="Ajanur")

    # JOB_KSD_VILLAGE = (

    #     ("Badiadka", "Badiadka"),
    #     ("Nirchal", "Nirchal"),
    #     ("Bela", "Bela"),
    #     ("Munnad", "Munnad"),
    #     ("Bedadka", "Bedadka"),
    #     ("Kolathur", "Kolathur"),
    #     ("Bellur", "Bellur"),
    #     ("Nettanige", "Nettanige"),
    #     ("Thekkil", "Thekkil"),
    #     ("Perumbala", "Perumbala"),
    #     ("Kaland", "Kaland"),
    #     ("Chemnad", "Chemnad"),
    #     ("Chengala", "Chengala"),
    #     ("Nakraje", "Nakraje"),
    #     ("Pady", "Pady"),
    #     ("Muttathody", "Muttathody"),
    #     ("Adoor", "Adoor"),
    #     ("Delampady", "Delampady"),
    #     ("Karadka", "Karadka"),
    #     ("Adhur", "Adhur"),
    #     ("Kumbadaje", "Kumbadaje"),
    #     ("Ubrangala", "Ubrangala"),
    #     ("Bandadka", "Bandadka"),
    #     ("Karivedakam", "Karivedakam"),
    #     ("Kuttikol", "Kuttikol"),
    #     ("Madhur", "Madhur"),
    #     ("Kudlu(Madhur)", "Kudlu(Madhur)"),
    #     ("Shiribaglu", "Shiribaglu"),
    #     ("Patla", "Patla"),
    #     ("Muttathody", "Muttathody"),
    #     ("Kudlu(Mogral Puthur)","Kudlu(Mogral Puthur)"),
    #     ("Puthur", "Puthur"),
    #     ("Muliyar", "Muliyar"),


    # )

    # village = models.CharField(max_length=100, choices=JOB_KSD_VILLAGE, default="Adhur")

    # JOB_MJR_VILLAGE = (

    #     ("Padre", "Padre"),
    #     ("Kattukukke", "Kattukukke"),
    #     ("Enmakaje", "Enmakaje"),
    #     ("Sheni", "Sheni"),
    #     ("Koipady", "Koipady"),
    #     ("Bombrana", "Bombrana"),
    #     ("Mogral", "Mogral"),
    #     ("Kidoor", "Kidoor"),
    #     ("Arikady", "Arikady"),
    #     ("Ujar Uluvar", "Ujar Uluvar"),
    #     ("Ichilampady", "Ichilampady"),
    #     ("Mangalpady", "Mangalpady"),
    #     ("Uppala", "Uppala"),
    #     ("Kodibail", "Kodibail"),
    #     ("Mulinja", "Mulinja"),
    #     ("Bekur", "Bekur"),
    #     ("Kubanoor", "Kubanoor"),
    #     ("Ichilangode", "Ichilangode"),
    #     ("Heroor", "Heroor"),
    #     ("Shiriya", "Shiriya"),
    #     ("Badaje", "Badaje"),
    #     ("Hosabettu", "Hosabettu"),
    #     ("Kunjathur", "Kunjathur"),
    #     ("Udyawar", "Udyawar"),
    #     ("Kaliyoor", "Kaliyoor"),
    #     ("Koliyoor", "Koliyoor"),
    #     ("Thalekala", "Thalekala"),
    #     ("Meenja", "Meenja"),
    #     ("Kadamabar", "Kadamabar"),
    #     ("Moodambail", "Moodambail"),
    #     ("Majibail", "Majibail"),
    #     ("Kuloor", "Kuloor"),
    #     ("Paivalike", "Paivalike"),
    #     ("Kayyar", "Kayyar"),
    #     ("Kudalmerkala", "Kudalmerkala"),
    #     ("Chippar", "Chippar"),
    #     ("Bayar", "Bayar"),
    #     ("Badoor", "Badoor"),
    #     ("Ednad", "Ednad"),
    #     ("Pavoor", "Pavoor"),
    #     ("Vorkady", "Vorkady"),
    #     ("Pathur", "Pathur"),
    #     ("Kodlamogaru", "Kodlamogaru"),


    # )

    # village = models.CharField(max_length=100, choices=JOB_MJR_VILLAGE, default="Arikady")





    # JOB_VLD_VILLAGE = (

    #     ("Balal", "Balal"),
    #     ("Parappa", "Parappa"),
    #     ("Chittarikkal", "Chittarikkal"),
    #     ("Palavayal", "Palavayal"),
    #     ("Kallar", "Kallar"),
    #     ("Belur", "Belur"),
    #     ("Thayannur", "Thayannur"),
    #     ("Kodom", "Kodom"),
    #     ("Kinanoor", "Kinanoor"),
    #     ("Karinthalam", "Karinthalam"),
    #     ("Bheemanady(Kinanoor Karinthalam)", "Bheemanady(Kinanoor Karinthalam)"),
    #     ("Cheemeni II", "Cheemeni II"),
    #     ("Panathady", "Panathady"),
    #     ("Bheemanady(West Eleri)", "Bheemanady(West Eleri)"),
    #     ("West Eleri", "West Eleri"),
    #     ("Maloth(West Eleri)", "Maloth(West Eleri)"),

        
    # )

    # village = models.CharField(max_length=100, choices=JOB_VLD_VILLAGE, default="Balal")
