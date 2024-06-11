from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login,get_user_model,authenticate
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm,ProfileUpdateForm
import logging
from django.contrib.auth.decorators import login_required

logger=logging.getLogger(__name__)


def homepage(request):
    return render(request,'users/home.html')



def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,f'{user}! Your account has been created successfully')
            user.save()
            login(request,user)
            return redirect('users:dashboard')
        
        else:
            for error in list(form.errors.values()):
                logger.error(f'Registration Error :{error}')
                
    else:
        form=UserRegistrationForm()

    return render(request,"users/register.html",{"form":form})

def profile(request,username):
    if request.method == 'POST':
        user = request.user
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'{username}, Your profile has been updated!')
            
            print(form)

            user=get_user_model().objects.filter(username=username).first()
            if user:
                form = ProfileUpdateForm(instance=user)
                form.fields['description'].widget.attrs={'rows':1}
                return render(request,"users/profile.html",context={'form':form})
                
            return redirect('users:profile', username=user.username)
        

            
        else:
            for error in list(form.errors.values()):
                logger.error(f'Profile Update error :{error}')
    else:
        form=ProfileUpdateForm(instance=request.user)
    return render(request,"users/profile.html",context={'form':form,'username': username})

class CustomLoginView(LoginView):
    template_name='registration/login.html'

    def get(self, request, *args, **kwargs):
        logger.debug('Using CustomLoginView with template: %s', self.template_name)
        return super().get(request, *args, **kwargs)
    
@login_required
def dashboard(request):
    return render(request,'users/dashboard.html',{'username': request.user.username})
    
# Create your views here.
