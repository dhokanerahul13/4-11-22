from django.shortcuts import render
from abb.models import visitors
from abb.forms import visitorform
# Create your views here.


def show_data(request):
    form=visitorform()
    if request.method=='POST':
        form=visitorform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            mobile_no=form.cleaned_data['mobile_no']
            feedback=form.cleaned_data['feedback']
            reg=visitors(name=name,mobile_no=mobile_no,feedback=feedback)
            reg.save()
        form=visitorform()    
    return render(request,'abb/home.html',{'form':form})    