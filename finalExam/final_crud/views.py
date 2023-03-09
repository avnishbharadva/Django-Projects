from django.shortcuts import render,redirect
from final_crud.forms import StudentForm
from final_crud.models import Student

# Create your views here.

def home(request):
    return render(request,"index.html")

def insert(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show') 
            except:
                pass
    else:
        form = StudentForm()
    return render(request,'addstudent.html',{'form':form}) 

def show(request):
    data = Student.objects.all()
    return render(request, "show.html", {'data' : data})

def edit(request, id):
    std = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': std})

def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'student': student})