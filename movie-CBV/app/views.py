from django.shortcuts import render
from django.http import HttpResponse
from app.models import Movie
from app.forms import movieform
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     m=Movie.objects.all()
#     return render(request,'home.html',{'movie_list':m})

class Movielist(ListView):      #ListView displays all objects/records retrieving from a model.
    model=Movie
    template_name = "home.html"
    context_object_name = "movie_list"


# def one(request,p):                                     #view specific movie details
#     b=Movie.objects.get(name=p)
#     return render(request,'1.html',{'b':b})

class Movieview(DetailView):    # DetailView displays a particular object retrieving from a model.
    model = Movie
    template_name = '1.html'
    context_object_name = 'b'

# def add(request):
#     if (request.method=="POST"):
#         form=movieform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     form=movieform()
#     return render(request,'add.html',{'form':form})

class Movieadd(CreateView):
    model=Movie
    template_name = 'add.html'
    fields = '__all__'
    success_url = reverse_lazy('app:home')

# def edit(request,p):
#     b=Movie.objects.get(name=p)
#     if(request.method=="POST"):
#         form=movieform(request.POST,request.FILES,instance=b)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     else:
#         form=movieform(instance=b)
#         return render(request,'edit.html',{'form':form})

class Movieupdate(UpdateView):
    model = Movie
    template_name = 'edit.html'
    fields = '__all__'
    success_url = reverse_lazy('app:home')

# def delete(request,p):
#     b=Movie.objects.get(name=p)
#     b.delete()
#     return home(request)

class Moviedelete(DeleteView):
    model = Movie
    template_name = 'delete.html'
    success_url = reverse_lazy('app:home')
