from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,StudentForm
from django.contrib.auth import login,logout,authenticate
from .models import CustomUser,Student
from django.views.generic.base import TemplateView,RedirectView
from django.contrib import messages #import messages

# Create your views here.


def login_request(request):
    login_form=LoginForm()
    if request.method=='POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "Welcome Back" )

                return redirect('/')
            else:
                messages.error(request, "User With Creadentials not found" )
                # print(login_form.cleaned_data,">>>>>>valid")
        else:
            messages.error(request, login_form.errors )
    return render(request,'users/login.html',{'login_form':login_form})

def register_request(request):
    register_form=RegisterForm()
    if request.method=='POST':
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.cleaned_data.pop('confirm_password')
            user=CustomUser(**register_form.cleaned_data)
            user.set_password(user.password)
            user.save()
            messages.success(request,'Register Successfully')

            return redirect('/login')
        else:
            messages.error(request,register_form.errors)
    return render(request,'users/register.html',{'register_form':register_form})


def logout_request(request):
    logout(request)
    messages.info(request,'Logged Out Successfully')
    return redirect('/')


class HomeView(TemplateView):
    template_name='users/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['all_students']=Student.objects.all()
        context['student_form']=StudentForm()
        return context

    def post(self,request):
        student_form=StudentForm(request.POST)
        if student_form.is_valid():
            # print(student_form.cleaned_data)
            student=Student(**student_form.cleaned_data)
            student.save()
            messages.success(request,"Student added" )

            return redirect('/')
        else:
            messages.error(request, student_form.errors )
            return redirect('/')

class UserDeleteView(RedirectView):
    url='/'

    def get_redirect_url(self,*args,**kwargs):
        student=Student.objects.get(id=kwargs['id'])
        student.delete()
        messages.info(self.request,"Student deleted")
        return super().get_redirect_url(self,*args,**kwargs)

class UpdateTemplateView(TemplateView):
    template_name='users/updatestudent.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateTemplateView, self).get_context_data(**kwargs)
        student=Student.objects.get(id=kwargs['id'])
        context['student_form']=StudentForm(instance=student)
        return context

    def post(self,request,**kwargs):
        student_form=StudentForm(request.POST)
        if student_form.is_valid():
            student=Student(id=kwargs['id'],**student_form.cleaned_data)            
            student.save()
            messages.info(request,"Student Updated")
            return redirect('/')
        else:
            print(">><<<<<eerrrors")
            messages.error(request,student_form.errors)
            return redirect('/update/'+str(kwargs['id']))

# def home(request):
#     return render(request,'users/home.html')