from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max
from django.contrib.auth.models import User,auth


# Create your views here.

def index(request):
    return render(request,'./myapp/index.html')


########### ADMIN SECTION #########################

#----------------------------Admin Login Page--------------------------------------------

from .models import login
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_list =login.objects.filter(username=username,password=password,u_type='admin')
        if len(user_list) ==1:
            request.session['user_id'] = user_list[0].id
            request.session['user_name'] = user_list[0].username

            return render(request,'./myapp/admin_home.html')
        else:
            msg ="Invalid Login"
            context ={'msg':msg}
            return render(request,'./myapp/admin_login.html',context)
    else:
        return render(request, './myapp/admin_login.html')
#-----------------------------------------------------------------------------------


#------------------------Admin home page--------------------------------------------

def admin_home(request):
    return render(request,'./myapp/admin_home.html')


# Here admin can add student details------------------------------------------------------------

def admin_student_add(request):
    if request.method == 'POST':
        s_name = request.POST.get('s_name')
        s_class = request.POST.get('s_class')
        age = request.POST.get('age')
        email = request.POST.get('email')


        cd = student(s_name=s_name, s_class=s_class,age=age,email=email)
        cd.save()
        context = {'msg':'Student Added'}
        return render(request,'./myapp/admin_student_add.html',context)
    else:

        return render(request,'./myapp/admin_student_add.html')


#Here admin can view student details

def admin_student_view(request):
    student_list = student.objects.all()
    context = {'student_list':student_list}
    return render(request,'./myapp/admin_student_view.html',context)




#Here admin can add faculty details

def admin_faculty_add(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        subject = request.POST.get('subject')
        age = request.POST.get('age')
        department= request.POST.get('department')
        email = request.POST.get('email')


        cd = faculty(f_name=f_name, subject=subject,age=age,department=department,email=email)
        cd.save()
        context = {'msg':'Faculty Added'}
        return render(request,'./myapp/admin_faculty_add.html',context)
    else:

        return render(request,'./myapp/admin_faculty_add.html')

#here admin can view faculty details

def admin_faculty_view(request):
    faculty_list = faculty.objects.all()
    context = {'faculty_list':faculty_list}
    return render(request,'./myapp/admin_faculty_view.html',context)



#------------------------Admin logout------------------------------------------------

def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

#---------------------------------------------------------------------------------------




#--------------------- Faculty Section-----------------------------------------------------------

def faculty_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_list = login.objects.filter(username=username, password=password, u_type='faculty')
        if len(user_list) == 1:
            request.session['user_id'] = user_list[0].id
            request.session['user_name'] = user_list[0].username

            return render(request, './myapp/faculty_home.html')
        else:
            msg = "Invalid Login"
            context = {'msg': msg}
            return render(request, './myapp/faculty_login.html', context)
    else:
        return render(request, './myapp/faculty_login.html')

#-----------------------------------------------------------------------



#----------------Faculty Home------------------------------------------

def faculty_home(request):
    return render(request,'./myapp/faculty_home.html')

#-----------------------------------------------------------------------


 #faculty Register

from .models import faculty
def faculty_register(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        age = request.POST.get('age')
        subject = request.POST.get('subject')
        department =  request.POST.get('department')
        email = request.POST.get('email')
        username=email
        password= request.POST.get("password")
        ul = login(username=username, password=password, u_type='faculty')
        ul.save()
        id = login.objects.all().aggregate(Max('id'))['id__max']

        fd = faculty(id=id,f_name=f_name, age=age,subject=subject,department=department,email=email)
        fd.save()

        msg="User Registered"
        context = {'msg':msg}
        return render(request,'./myapp/faculty_login.html',context)
    else:
        return render(request,'./myapp/faculty_register.html')


#---Here faculty can add student details --------------------------------------------------------

def faculty_student_add(request):
    if request.method == 'POST':
        s_name = request.POST.get('s_name')
        s_class = request.POST.get('s_class')
        age = request.POST.get('age')
        email = request.POST.get('email')


        cd = student(s_name=s_name, s_class=s_class,age=age,email=email)
        cd.save()
        context = {'msg':'Student Added'}
        return render(request,'./myapp/faculty_student_add.html',context)
    else:

        return render(request,'./myapp/faculty_student_add.html')


#Here faculty can view student details

def faculty_student_view(request):
    student_list = student.objects.all()
    context = {'student_list':student_list}
    return render(request,'./myapp/faculty_student_view.html',context)




#Faculty logout
def faculty_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return faculty_login(request)
    else:
        return faculty_login(request)



########## Student Section #########################

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_list = login.objects.filter(username=username, password=password, u_type='student')
        if len(user_list) == 1:
            request.session['user_id'] = user_list[0].id
            request.session['user_name'] = user_list[0].username

            return render(request, './myapp/student_home.html')
        else:
            msg = "Invalid Login"
            context = {'msg': msg}
            return render(request, './myapp/student_login.html', context)
    else:
        return render(request, './myapp/student_login.html')


#==============Student HOMEPAGE=============================================================================


def student_home(request):
    return render(request,'./myapp/student_home.html')

#==========Student Registration===============================================================================

from .models import student
def student_register(request):
    if request.method == 'POST':
        s_name = request.POST.get('s_name')
        age = request.POST.get('age')
        s_class = request.POST.get('s_class')
        email = request.POST.get('email')
        username=email
        password= request.POST.get("password")
        ul = login(username=username, password=password, u_type='student')
        ul.save()
        id = login.objects.all().aggregate(Max('id'))['id__max']

        fd = student(id=id,s_name=s_name, age=age,s_class=s_class,email=email)
        fd.save()

        msg="User Registered"
        context = {'msg':msg}
        return render(request,'./myapp/student_login.html',context)
    else:
        return render(request,'./myapp/student_register.html')

#Here student can view student details
def student_student_view(request):
    student_list = student.objects.all()
    context = {'student_list':student_list}
    return render(request,'./myapp/student_student_view.html',context)


# Here student can view the faculty details
def student_faculty_view(request):
    faculty_list = faculty.objects.all()
    context = {'faculty_list':faculty_list}
    return render(request,'./myapp/student_faculty_view.html',context)


#student logout
def student_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return student_login(request)
    else:
        return student_login(request)