from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls.static import static
from django.contrib import messages
from django.contrib.auth.models import User, auth
from home.models import profileinfo,contact_us,Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.http.response import JsonResponse
import json
from datetime import date



# Create your views here.


def index(request):
    context ={}
    ch = profileinfo.objects.filter(user__id=request.user.id)

    if len(ch)>0:
        data = profileinfo.objects.get(user__id=request.user.id)
        context ={'data':data,'range':range(18,60)}
        return render(request, 'home/index.html',context)
    return render(request, 'home/index.html')
    


def home(request):
    context ={}
    ch = profileinfo.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = profileinfo.objects.get(user__id=request.user.id)
        context ={'data':data,'range':range(18,60)}
        return render(request, 'home/home.html', context)
    return render(request, 'home/home.html')

def facebook(request):
    return HttpResponse('facebook')

def help(request):
    context ={}
    ch = profileinfo.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = profileinfo.objects.get(user__id=request.user.id)
        context["data"]=data
        messages.success(request,'Thank You For Contacting Us')

        return render(request, 'home/help.html', context)
    return render(request, 'home/help.html')

def contact(request):
    context ={}
    ch = profileinfo.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = profileinfo.objects.get(user__id=request.user.id)
        context = {'data':data}
        if request.method =='POST':
            name = request.POST['name']
            email = request.POST['email']
            mo_no = request.POST['contact_no']
            msg = request.POST['content']
            # print(request.POST)

            msgData = contact_us()
            msgData.name = name
            msgData.email = email
            msgData.mo_no = mo_no
            msgData.msg = msg
            msgData.save()
            messages.success(request,'Thank You For Contacting Us')
        
            return render(request, 'home/contact.html', context)
    return render(request, 'home/contact.html', context)


def sign_up(request):
    if request.method=="POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        uname = request.POST["uname"]
        email = request.POST["email"]
        pwd1 = request.POST["pass1"]
        pwd2 = request.POST["pass2"]
        mo_no = request.POST["mobile-no"]
        gender = request.POST["gender"]
        if pwd1 == pwd2:
            if User.objects.filter(username=uname).exists():
                messages.error(request, "Username already exists")
                return redirect('/')
            else:    
                usr = User.objects.create_user(uname,email,pwd1)
                usr.first_name = fname
                usr.last_name = lname
                usr.save()
                userId= usr.id
                newId= "JB00" + str(userId)
                proinfo = profileinfo(user=usr, conttact_no=mo_no, gender=gender,pro_Id=newId)
                proinfo.save()
                messages.success(request, "Account Created successffully")
                return redirect('/')

        else:
            messages.success(request, "Password didnt match")
            return redirect('/')  

    return redirect('/')

def user_login(request):
    if request.method=='POST':
        un = request.POST['user-id']
        pwd = request.POST['password_login']

        user = authenticate(username=un, password=pwd)
        if user is not None:
            auth.login(request, user)
            data = profileinfo.objects.get(user__id=request.user.id)
            if data.gender == "Male":
                 messages.success(request, f'Welcome Mr. {user.first_name}')
            else:
                 messages.success(request, f'Welcome Mrs. {user.first_name}')

           
            context ={}
            context ={'data':data,'range':range(18,60)}
            return render(request, 'home/home.html',context)

        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'home/index.html')

        
    else:
        return HttpResponse("no user")

@login_required(login_url='/')
def logout_user(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('/')

@login_required(login_url='/')
def editprofile(request):
    context ={}
    ch = profileinfo.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = profileinfo.objects.get(user__id=request.user.id)
        d_down = profileinfo.matrimonyProfileFor_choices 
        g_down = profileinfo.gender_choices
        b_group = profileinfo.blood_group_choices
        h_choices = profileinfo.height_choices
        state_choices = profileinfo.state_choices
        edu_choices = profileinfo.education_choices

        context={'data':data,'range':range(0,100),
            'range2':range(18,60),'range3':(d_down),'gen_down':(g_down),
            'b_group':b_group,'h_choices':h_choices, 'state_choices':state_choices,'edu_choices':edu_choices,
        }

        if request.method =="POST":
      
            fn = request.POST['fname']
            mn = request.POST['mname']
            ln = request.POST['lname']
            email = request.POST['email']
            mno = request.POST['mobile']
            dob = request.POST['dob']
            gen = request.POST['gender']
            height = request.POST['height']
            occp = request.POST['occupation']
            adrs = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            pcode = request.POST['pcode']
            country = request.POST['country']
            d_status = request.POST['disability-status']
            if d_status == "Yes":
                d_type = request.POST['disability-type']
                d_cent = request.POST['disab_cent']
            
            abt = request.POST['about']
            religion = request.POST['religion']

            # family info
            f_occ = request.POST['f_occ'] 
            m_occ = request.POST['m_occ']
            no_sis = request.POST['no_sis']
            no_bros = request.POST['no_bros']
            marital_status = request.POST['marital_status']
            B_type = request.POST['B_type']
            pro_created = request.POST['pro_created']
            drink = request.POST['drink']
            caste = request.POST['caste']
            s_caste = request.POST['s_caste']
            pob = request.POST['pob']
            # birthtime = request.POST['birthtime']


            # other info
            m_Tounge = request.POST['m_Tounge']
            smoke = request.POST['smoke']
            weight = request.POST['weight']
            b_Group = request.POST['b_Group']
            diet = request.POST['diet']
            rashi = request.POST['rashi']
            complexion = request.POST['complexion']

            # educational info
            education = request.POST['education']
            education_detail = request.POST['education_detail']
            occupation_detail = request.POST['occupation_detail']
            annual_income = request.POST['annual_income']
            current_location = request.POST['current_location']  

            #  partner preference
            p_age_min = request.POST['p_age_min']  
            p_age_max = request.POST['p_age_max']  
            p_Marital_Status = request.POST['p_Marital_Status']  
            p_Body_Type = request.POST['p_Body_Type']  
            p_Complexion = request.POST['p_Complexion']  
            p_Height = request.POST['p_Height']  
            p_Diet = request.POST['p_Diet']  
            p_Manglik = request.POST['p_Manglik']  
            p_Religion = request.POST['p_Religion']  
            p_Caste = request.POST['p_Caste']  
            p_Mother_Tongue = request.POST['p_Mother_Tongue']  
            p_Education = request.POST['p_Education']  
            p_Country_Of_Residence = request.POST['p_Country_Of_Residence']  
            p_State = request.POST['p_State']  
            p_Occupation = request.POST['p_Occupation']

            usr = User.objects.get(id=request.user.id)
            usr.first_name = fn
            usr.last_name = ln
            usr.email = email
            usr.save()

            
            data.conttact_no = mno
            data.dob = dob
            # data.age = age
            data.address = adrs
            data.city = city
            data.middlename = mn
            data.state = state
            data.country = country
            data.occupation = occp
            data.pincode = pcode
            data.height = height
            data.gender = gen
            data.disability = d_status
            if data.disab_type == "Yes":
                data.disab_type = d_type
                data.disab_percentage = d_cent
            data.about = abt
            data.religion = religion
            data.complexion = complexion
            # data.birth_time = birthtime


            # family info
            data.f_occ = f_occ
            data.m_occ = m_occ
            data.no_sis = no_sis
            data.no_bros = no_bros
            data.marital_status = marital_status
            data.B_type = B_type
            data.pro_created = pro_created
            data.drink = drink
            data.caste = caste
            data.s_caste = s_caste
            data.pob = pob
            data.rashi = rashi

            # other details
            data.m_Tounge = m_Tounge
            data.smoke = smoke
            data.weight = weight
            data.b_Group = b_Group
            data.diet = diet

            # educational details 
            data.education = education
            data.education_detail = education_detail 
            data.occupation_detail = occupation_detail 
            data.annual_income = annual_income 
            data.current_location = current_location 

            # partner preference
            data.p_age_min = p_age_min
            data.p_age_max = p_age_max 
            data.p_Marital_Status = p_Marital_Status 
            data.p_Body_Type = p_Body_Type 
            data.p_Complexion = p_Complexion
            data.p_Height = p_Height
            data.p_Diet = p_Diet
            data.p_Manglik = p_Manglik
            data.p_Religion = p_Religion
            data.p_Caste = p_Caste
            data.p_Mother_Tongue = p_Mother_Tongue
            data.p_Education = p_Education
            data.p_Country_Of_Residence = p_Country_Of_Residence
            data.p_State = p_State
           
            data.save()

            db = profileinfo.objects.get(user__id=request.user.id)
            today = date.today()
            age = today.year - db.dob.year - ((today.month, today.day) < (db.dob.month, db.dob.day))
            data.age = age
            data.save()
            # print(age)

            if "profile-pic" in request.FILES:
                img = request.FILES["profile-pic"]
                data.pro_pic = img
                data.save()
            data = profileinfo.objects.get(user__id=request.user.id)
            d_down = profileinfo.matrimonyProfileFor_choices 
            g_down = profileinfo.gender_choices
            b_group = profileinfo.blood_group_choices
            edu_choices = profileinfo.education_choices


            context={'data':data,'range':range(0,100),'range2':range(18,60),'range3':(d_down),'gen_down':(g_down),'b_group':b_group,'h_choices':h_choices,'state_choices':state_choices,
                        'edu_choices':edu_choices,
                        }

            messages.success(request,'Profile Updated Successfully')
        return render(request, 'home/editprofile.html',context)

    return render(request, 'home/editprofile.html',context)




@login_required(login_url='/')
def search(request):
    h_choices = profileinfo.height_choices
    edu_choices = profileinfo.education_choices

    context ={}
    ch = profileinfo.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = profileinfo.objects.get(user__id=request.user.id)
        search = profileinfo.objects.all().exclude(user__id=request.user.id)
        context = {'data':data, 'search':search,'range2':range(18,60),'range':range(0,120),'h_choices':h_choices,'edu_choices':edu_choices}
        

        if request.method == "POST":
            mn_age = request.POST["min_age"]
            mx_age = request.POST["max_age"]
            gen = request.POST["gender"]
            religion = request.POST["religion"]
            # print(gen)
            search2 = profileinfo.objects.filter(Q(gender=gen)&Q(age__gte=mn_age)&Q(age__lt=mx_age)&Q(religion=religion))
            search2 =search2.filter().exclude(user__id=request.user.id)

            context = {'data':data, 'search':search, 'search2':search2,'range2':range(18,60),'range':range(0,120),'h_choices':h_choices,'edu_choices':edu_choices}

        return render(request, 'home/search.html', context)

    return render(request, 'home/search.html')

    
@login_required(login_url='/')
def adv_search(request):
    h_choices = profileinfo.height_choices
    edu_choices = profileinfo.education_choices

    context ={}
    ch = profileinfo.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = profileinfo.objects.get(user__id=request.user.id)
        search = profileinfo.objects.all().exclude(user__id=request.user.id)
        context = {'data':data, 'search':search,'range2':range(18,60),'range':range(0,120),'h_choices':h_choices,'edu_choices':edu_choices}
        if request.method == "POST":
            look_for = request.POST["looking_for"]
            mn_age = request.POST["age_from"]
            mx_age = request.POST["age_to"]
            m_status = request.POST["marital_status"]
            religion = request.POST["religion"]
            height_from = request.POST["ht_from"]
            ht_to = request.POST["height_to"]
            pro_with_disab = request.POST["disab_profile"]
            complexion = request.POST["complexion"]
            edu = request.POST["education"]
            manglik = request.POST["manglik"]
            # print(ht_to)
            search2 = profileinfo.objects.filter(Q(gender=look_for)&Q(age__gte=mn_age)&Q(age__lt=mx_age)&Q(religion=religion)&Q(height__gte=height_from)
                    &Q(height__lte=ht_to)&Q(disability=str(pro_with_disab))&Q(complexion=complexion)&Q(education=edu))
            search2 =search2.filter().exclude(user__id=request.user.id)

            context = {'data':data, 'search':search, 'search2':search2,'range2':range(18,60),'range':range(0,120),'h_choices':h_choices,'edu_choices':edu_choices}

        return render(request, 'home/search.html', context)

    return render(request, 'home/search.html',context)

@login_required(login_url='/')
def view_profile(request):
    context={}
    ch = profileinfo.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        is_favourite = bool
        data = profileinfo.objects.get(user__id=request.user.id)
        

        if request.method=="GET":
            id = request.GET['pid']
            # id2 = request.GET['fid']
            obj = profileinfo.objects.get(user__id=id)
            # other_user = User.objects.get(id=id)

            q1 = obj.gender
            q2 = obj.age
            q3 = obj.religion
            if obj.favourites.filter(id=request.user.id).exists():
                is_favourite = True

            # messagess = Message.objects.filter(Q(receiver=request.user, sender=other_user))
            # messagess.update(seen=True)
            # messagess = messagess | Message.objects.filter(Q(receiver=other_user, sender=request.user) )
            search2 = profileinfo.objects.filter(Q(gender=q1)&Q(religion=q3))
            search2 =search2.filter().exclude(user__id=request.user.id)
            search2 = search2.filter().exclude(id=id)
            context={'profile':obj, 'data':data, 'search3':search2,'is_favourite':is_favourite}
            return render(request, 'home/view_profile.html', context)

@login_required(login_url='/')
def view_self_profile(request):

    context={}
    ch = profileinfo.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        is_favourite = bool
        data = profileinfo.objects.get(user__id=request.user.id)
        

        if request.method=="GET":
            id = request.GET['pid']
            obj = profileinfo.objects.get(user__id=id)
            q1 = obj.gender
            q2 = obj.age
            q3 = obj.religion
            if obj.favourites.filter(id=request.user.id).exists():
                is_favourite = True
            search2 = profileinfo.objects.filter(Q(gender=q1)&Q(religion=q3))
            search2 =search2.filter().exclude(user__id=request.user.id)
            search2 = search2.filter().exclude(id=id)
            context={'profile':obj, 'data':data, 'search3':search2,'is_favourite':is_favourite}
    return render(request, 'home/view_self_profile.html', context)
        
@login_required(login_url='/')
def search_by_id(request):
    context = {}
    ch = profileinfo.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        is_favourite = bool

        data = profileinfo.objects.get(user__id=request.user.id)
        if request.method == "GET":
            qry = request.GET["search_by_id"]
            result1 = profileinfo.objects.filter(pro_Id__icontains=qry)
            
            if len(result1)== 0:
                return HttpResponse('<h2>Profile Id does not exists</h2>')
            elif len(result1)== 6:
                return HttpResponse('<h2>Profile Id does not exists</h2>')
            else:
                obj = profileinfo.objects.get(pro_Id__icontains=qry)
                
                id2 = obj.id
                if obj.favourites.filter(id=request.user.id).exists():
                    is_favourite = True
                q1 = obj.gender
                q2 = obj.age
                q3 = obj.religion
                q4 = obj.pro_Id
                

                search2 = profileinfo.objects.filter(Q(gender=q1)&Q(religion=q3))
                search2 =search2.filter().exclude(user__id=request.user.id)
                
                context={'profile':obj, 'data':data,'search3':search2,'is_favourite':is_favourite}
            return render(request, 'home/view_profile.html', context)



@login_required(login_url='/')
def add_favourite(request):
    id = request.GET['fid']
    is_favourite = bool
    result = ''
    obj = profileinfo.objects.get(id=id)
    # data = profileinfo.objects.get(user__id=request.user.id)

    if obj.favourites.filter(id=request.user.id).exists():
        obj.favourites.remove(request.user)
    else:
        obj.favourites.add(request.user)
    if obj.favourites.filter(id=request.user.id).exists():
        is_favourite = True
    else:
        is_favourite = False


    return HttpResponse(is_favourite)

       
@login_required(login_url='/')
def fav_list(request):
    context={}
    ch = profileinfo.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = profileinfo.objects.get(user__id=request.user.id)
        data2 = profileinfo.objects.filter(favourites=request.user)
        # fav_list = data.favourites.all()
        context = {
            'search2': data2,
            'data':data,
        }

        return render(request, 'home/my_fav.html', context)

@login_required(login_url='/')
def chatroom(request):
    context={}
    ch = profileinfo.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        # is_favourite = bool
        data = profileinfo.objects.get(user__id=request.user.id)
        if request.method =="GET":
            id = request.GET['pk']
            other_user = User.objects.get(id=id)
            other_user_dp = profileinfo.objects.get(user__id=id)
            obj = profileinfo.objects.filter(user__id=request.user.id)

        # other_user = get_object_or_404(User, pk=pk)
            # print(owner_dp)
            # print(other_user_dp)
            messagess = Message.objects.filter(Q(receiver=request.user, sender=other_user))
            messagess.update(seen=True)
            messagess = messagess | Message.objects.filter(Q(receiver=other_user, sender=request.user) )
            context={'profile':obj, 'data':data,"other_user": other_user, "messagess": messagess,"other_user_dp": other_user_dp, "messagess": messagess}

            return render(request, "home/chatroom2.html", context)



@login_required(login_url='/')
def ajax_load_messages(request, pk):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(seen=False).filter(
        Q(receiver=request.user, sender=other_user)
    )
    message_list = [{
        "sender": message.sender.username,
        "message": message.message,
        "sent": message.sender == request.user,
        "time": message.date_created,
    } for message in messages]
    messages.update(seen=True)
    
    if request.method == "POST":
        message = json.loads(request.body)
        m = Message.objects.create(receiver=other_user, sender=request.user, message=message)
        message_list.append({
            "sender": request.user.username,
            "message": m.message,
            "sent": True,
            "time":m.date_created,
        })
    return JsonResponse(message_list, safe=False)

