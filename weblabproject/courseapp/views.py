from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Course
from .forms import CourseForm 
# Create your views here.
def home(request):
    all_courses= Course.objects.all()
    return render(request,'courseapp\index.html',{'courses':all_courses})

def rem(request,id):
    c = Course.objects.get(id=id)
    c.delete()
    return redirect(home)


#10th January:
def addNew(request):
    frm = CourseForm()
    return render(request,'courseapp/addnew.html', {'cform': frm})

def save(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                pass

    return redirect(home)




def edit(request,id):
    crs = Course.objects.get(id=id)
    crs = CourseForm(instance = crs)
    return render(request,'courseapp/update.html', {'form':crs})

def update(request, id): 
    if request.method == "POST":  
        # course = get_object_or_404(Course, pk=id)
        crs = Course.objects.get(id=id)
        form = CourseForm(request.POST, instance = crs)  
        if form.is_valid():  
            form.save()  
            # return HttpResponseRedirect("/courseapp/")
            return redirect(home) 
    else:
        # course = get_object_or_404(Course, pk=id)
        crs = Course.objects.get(id=id)
        form = CourseForm(instance = crs)
        # print(form) #terminal console e ki return kore, dekhar jonno
    return render(request, 'courseapp/update.html', {"form":form})


# def update(request, id): 
#     if request.method == "POST":  
#         # course = get_object_or_404(Course, pk=id)
#         course = Course.objects.get(id=id)
#         form = CourseForm(request.POST, instance = course)  
#         if form.is_valid():  
#             form.save()  
#             # return HttpResponseRedirect("/courseapp/")
#             return redirect(home) 
#     else:
#         # course = get_object_or_404(Course, pk=id)
#         course = Course.objects.get(id=id)
#         form = CourseForm(instance = course)
#         # print(form) #terminal console e ki return kore, dekhar jonno
#     return render(request, 'courseapp/update.html', {"form":form}) 








# def update(request, id):
#     crs = Course.objects.get(id=id)
#     form = Course(request.POST, instance = crs)
#     if request.method == "POST":
#         form = Course(request.POST, instance = crs)
#         if form.is_valid():
#             form.save()
#             return redirect(home)

#     return redirect(home)



