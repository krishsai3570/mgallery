from django.shortcuts import render,redirect

from django.views.generic import View
from django.contrib import messages


from myapp.forms import MovieForm

from myapp.models import Movies




class MovieCreateView(View):

    def get(self,request,*args,**kwargs):


        form_instance=MovieForm()

        return render( request,"movie_add.html",{"form":form_instance})
    


    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data
           
            Movies.objects.create(**data)

            messages.success(request,"movie has been added")

            return redirect("movie-list")
        
        else:

            messages.error(request,"failed to add movie")
            return render(request,"movie_add.html",{"form":form_instance})
        





        # listing view

class MovieListView(View):

    def get(self,request,*args,**kwargs):

        qs=Movies.objects.all()

        return render(request,"movie_list.html",{"movies":qs})

            

class MovieDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movies.objects.get(id=id)

        return render(request,"movie_detail.html",{"movie":qs})



class MovieDeleteView(View):
    
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movies.objects.get(id=id).delete()

        messages.success(request,"movie removed")

        # django>shortcut>redirect

        return redirect("movie-list")
    


class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movies.objects.get(id=id)

        dictionary={
            "title":qs.title,
            "genre":qs.genre,
            "language":qs.language,
            "year":qs.year,
            "run_time":qs.run_time,
            "director":qs.director

        }

        form_instance=MovieForm(initial=dictionary)

        
        return render( request,"movie_edit.html",{"form":form_instance})



        
        

    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get("pk")

            qs=Movies.objects.filter(id=id).update(**data) 

            messages.success(request,"movie update")   

            return redirect("movie-list")
        else:
            return render( request,"movie_edit.html",{"form":form_instance})
        

        


    
