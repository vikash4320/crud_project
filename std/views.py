from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def home(request):
    h_obj=Student.objects.all()

    return render(request,'index.html',{'h_obj1':h_obj})

from . models import Student
def stu_data(request):
    if request.method=="POST":
        # Retrive user Response
        stu_name=request.POST.get('name')
        stu_roll=request.POST.get('roll')
        stu_email=request.POST.get('email')
        stu_contact=request.POST.get('contact')
        stu_adress=request.POST.get('adress')


        s=Student()
        s.m_roll=stu_roll
        s.m_name=stu_name
        s.m_email=stu_email
        s.m_adress=stu_adress
        s.m_phone=stu_contact

        s.save()
        return redirect('home')





        print("this is data from web add")

     
    return render(request,'add_student.html')

"""
def del_stu(request,m_roll):
    #sd=Student.objects.all()
    sd=Student.objects.get(m_roll=m_roll)
    sd.delete()
    return redirect('home')
    """
def deleteData(request,id):
    d=Student.objects.get(id=id) 
    d.delete()
    
    return redirect("home")



"""
def update_stu(request,roll):
    sd=Student.objects.all(pk=roll)

    """
def updateData(request,id):
    edit=Student.objects.get(id=id)
    return render(request,'update.html',{'edit':edit})

from django.contrib import messages

def do_updateData(request,id):
    if request.method=="POST":
        s_roll=request.POST.get('roll')
        s_name=request.POST.get('name')
        s_email=request.POST.get('email')
        s_adress=request.POST.get('adress')
        s_phone=request.POST.get('contact')

        upd=Student.objects.get(id=id)
        upd.m_roll=s_roll
        upd.m_name=s_name
        upd.m_email=s_email
        upd.m_adress=s_adress
        upd.m_phone=s_phone
        upd.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect('home')
    
    #d=Student.objects.get(id=id) 
   # context={"d":d}
  #  return render(request,"update.html",context)
     








    
    
