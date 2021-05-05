from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class profileinfo(models.Model):
    state_choices = (
        ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
        ('Andhra Pradesh','Andhra Pradesh'),
        ('Arunachal Pradesh','Arunachal Pradesh'),
        ('Assam','Assam'),
        ('Bihar','Bihar'),
        ('Chandigarh','Chandigarh'),
        ('Chhattisgarh','Chhattisgarh'),
        ('D & N Haveli & Daman & Diu','D & N Haveli & Daman & Diu'),
        ('Delhi','Delhi'),
        ('Gujrat','Gujrat'),
        ('Haryana','Haryana'),
        ('Himachal Pradesh','Himachal Pradesh'),
        ('Jammu & Kashmir','Jammu & Kashmir'),
        ('Jharkhand','Jharkhand'),
        ('Karnataka','Karnataka'),
        ('Kerala','Kerala'),
        ('Ladakh','Ladakh'),
        ('Lakshdweep','Lakshdweep'),
        ('Madhya Pradesh','Madhya Pradesh'),
        ('Maharashtra','Maharashtra'),
        ('Manipur','Manipur'),
        ('Meghalaya','Meghalaya'),
        ('Mizoram','Mizoram'),
        ('Nagaland','Nagaland'),
        ('Odisha','Odisha'),
        ('Puducherry','Puducherry'),
        ('Punjab','Punjab'),
        ('Rajsthan','Rajsthan'),
        ('Sikkim','Sikkim'),
        ('Tamil Nadu','Tamil Nadu'),
        ('Telangana','Telangana'),
        ('Tripura','Tripura'),
        ('Uttar Pradesh','Uttar Pradesh'),
        ('Uttarakhand','Uttarakhand'),
        ('West Bengal','West Bengal'),
      
    )
    height_choices = (
        ('100','3.3ft (100cm)'),('102','3.4ft (102cm)'),('104','3.5ft (104cm)'),('107','3.6ft (107cm)'),
        ('109','3.7ft (109cm)'),('112','3.8ft (112cm)'),('114','3.9ft (114cm)'),('117','3.10ft (117cm)'),('119','3.11ft (119cm)'),('122','4.0ft (122cm)'),('124','4.1ft (124cm)'),('127','4.2ft (127cm)'),
        ('130','4.3ft (130cm)'),('132','4.4ft (132cm)'),('135','4.5ft (135cm)'),
        ('137','4.6ft (137cm)'),('140','4.7ft (140cm)'),('142','4.8ft (142cm)'),('145','4.9ft (145cm)'),('147','4.10ft (147cm)'),('150','4.11ft (150cm)'),
        ('152','5.0ft (152cm)'),
        ('155','5.1ft (155cm)'),('158','5.2ft (158cm)'),('160','5.3ft (160cm)'),('163','5.4ft (163cm)'),('165','5.5ft (165cm)'),('168','5.6ft (168cm)'),('170','5.7ft (170cm)'),('173','5.8ft (173cm)'),('175','5.9ft (175cm)'),('178','5.10ft (178cm)'),('180','5.11ft (180cm)'),('183','6.0ft (183cm)'),
        ('186','6.1ft (186cm)'),('188','6.2ft (188cm)'),('191','6.3ft (191cm)'),('193','6.4ft (193cm)'),('196','6.5ft (196cm)'),('198','6.6ft(198cm)'),('200','6.7ft (200cm)'),('203','6.8ft (203cm)'),('206','6.9ft (206cm)'),('208','6.10ft (208cm)'),('211','6.11ft (211cm)'),('213','7.0ft (213cm)'),('216','7.1ft (216cm)'),('218','7.2ft (218cm)'),
    )
    gender_choices = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    matrimonyProfileFor_choices = (
        ('Self', 'Self'),
        ('Son', 'Son'),
        ('Daughter', 'Daughter'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister'),
    )
    blood_group_choices = (
    ('A +ve', 'A +ve'),
    ('A -ve', 'A -ve'),
    ('B +ve', 'B +ve'),
    ('B -ve', 'B -ve'),
    ('O +ve', 'O +ve'),
    ('O -ve', 'O -ve'),
    ('AB +ve', 'AB +ve'),
    ('AB -ve', 'AB -ve'),
    )
    education_choices = ( ('Bachelors','Bachelors'),('Masters','Masters'),('Doctorate','Doctorate'),('Diploma','Diploma'),('Secondary','Secondary'),
    ('High School','High School'),
    )
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    pro_Id = models.CharField(max_length=10, default='JB')
    conttact_no  = models.IntegerField()
    address = models.CharField(blank=True, max_length=250)
    city = models.CharField(blank=True, max_length=250)
    middlename = models.CharField(blank=True,null=True,default='',max_length=250)
    state = models.CharField(blank=True, max_length=250,choices=state_choices)
    country = models.CharField(blank=True,null=True,default=" ",max_length=250)
    occupation = models.CharField(blank=True,null=True, max_length=250)
    pincode = models.IntegerField(null=True, blank=True, default="0")
    date_joined = models.DateTimeField(auto_now_add=True)
    height = models.IntegerField(null=True,blank=True,default='0', choices=height_choices)
    age = models.IntegerField(null=True, blank=True,default=0)
    # dob = models.DateTimeField('Date of Birth/Time - Format : YYYY-MM-DD HH:MM',null=True,auto_now_add=False, auto_now=False)
    dob = models.DateField(auto_now_add=False, auto_now=False, null=True)
    height = models.FloatField(null=True,blank=True)
    pro_pic = models.FileField(upload_to="profile_pic",null=True, blank=True)
    gender = models.CharField(max_length=20, default="",choices=gender_choices)
    religion = models.CharField(max_length=50, null=True, blank=True)
    disability= models.CharField(max_length=10,blank=True, null=True)
    disab_type= models.CharField(max_length=50,blank=True, null=True)
    disab_percentage= models.CharField(max_length=50,blank=True, null=True)
    about= models.CharField(max_length=500,blank=True, null=True)
    birth_time = models.TimeField(auto_now_add=False,null=True,blank=True)
    complexion = models.CharField(max_length=50,null=True, default='Not Specified')
    favourites = models.ManyToManyField(User,related_name='favourite', blank=True )

    # family details

    f_occ = models.CharField(max_length=70,blank=True, null=True)
    m_occ = models.CharField(max_length=70,blank=True, null=True)
    no_sis = models.CharField(max_length=70,blank=True, null=True)
    no_bros = models.CharField(max_length=70,blank=True, null=True)
    marital_status = models.CharField(max_length=70,blank=True, null=True)
    B_type = models.CharField(max_length=70,blank=True, null=True)
    pro_created = models.CharField(max_length=70,blank=True, null=True)
    drink = models.CharField(max_length=70,blank=True, null=True)
    caste = models.CharField(max_length=70,blank=True, null=True)
    s_caste = models.CharField(max_length=70,blank=True, null=True)
    pob = models.CharField(max_length=70,blank=True, null=True)
    rashi = models.CharField(max_length=70,blank=True, null=True)


    # other details
    m_Tounge = models.CharField(max_length=50,blank=True, null=True)
    smoke = models.CharField(max_length=50,blank=True, null=True)
    weight = models.CharField(max_length=50,blank=True, null=True)
    b_Group = models.CharField(max_length=50,blank=True, null=True,choices=blood_group_choices)
    diet = models.CharField(max_length=50,blank=True, null=True)

     #Education & Career

    education = models.CharField(max_length=50,blank=True, null=True, choices=education_choices)
    education_detail = models.CharField(max_length=50,blank=True, null=True)
    occupation_detail = models.CharField(max_length=100,blank=True, null=True)
    annual_income = models.CharField(max_length=20, default="not specified",blank=True, null=True)
    current_location = models.CharField(max_length=25,blank=True, null=True)


      #partner prefrences

    p_age_min = models.IntegerField(default=0,blank=True)
    p_age_max = models.IntegerField(default=0,blank=True)
    p_Marital_Status = models.CharField(max_length=10,null=True,blank=True)
    p_Body_Type = models.CharField(max_length=25, null=True,blank=True)
    p_Complexion = models.CharField(max_length=25,null=True,blank=True)
    p_Height = models.CharField(max_length=25,null=True,blank=True)

    p_Diet =  models.CharField(max_length=25,null=True,blank=True)
    p_Manglik =  models.CharField(max_length=25,null=True,blank=True)
    p_Religion =  models.CharField(max_length=25,null=True,blank=True)
    p_Caste =  models.CharField(max_length=25,null=True,blank=True)
    p_Mother_Tongue =  models.CharField(max_length=25,null=True,blank=True)
    p_Education =  models.CharField(max_length=25,null=True,blank=True)
    p_Country_Of_Residence =  models.CharField(max_length=25,null=True,blank=True)
    p_State =  models.CharField(max_length=25,null=True,blank=True)
    p_Occupation =  models.CharField(max_length=25,null=True,blank=True)


    def __str__(self):
        return self.user.first_name
    
    class Meta:
        verbose_name_plural ="Profiles"


class contact_us(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    mo_no = models.IntegerField()
    msg = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"



class Message(models.Model):

    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_created",)

