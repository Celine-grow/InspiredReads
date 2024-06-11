from django.shortcuts import render,redirect,get_object_or_404
from  django.contrib.auth.decorators import login_required
from .models import Writing
from .forms import WritingForm,SelectNovelForm
from django.urls import reverse


@login_required
def create_novel(request):
    if request.method == 'POST':
        form=WritingForm(request.POST,request.FILES)
        if form.is_valid:
            writing=form.save(commit=False)
            writing.user=request.user
            writing.save()
            return redirect(reverse('users:dashboard'))
    else:
        form=WritingForm()
    return render(request,'Novelwrite/create_novel.html',{'form':form})

def edit_novel(request,pk):
    writing=get_object_or_404(Writing,pk=pk,user=request.user)
    if request.method == 'POST':
        form=WritingForm(request.POST,request.FILES)
        if form.is_valid:
            form.save(commit=False)
            return redirect(reverse('users:dashboard'))
    else:
        form=WritingForm(instance=writing)
    return render(request,'Novelwrite/edit_novel.html',{'form':form})
     
@login_required
def select_novel(request):
    if request.method == 'POST':
        form = SelectNovelForm(request.user, request.POST)
        if form.is_valid():
            novel_id = form.cleaned_data['novel']
            return redirect('Novelwrite:edit_novel', pk=novel_id)
    else:
        form = SelectNovelForm(request.user)
    return render(request, 'Novelwrite/selectNovel.html', {'form': form})
             
# Create your views here.
