from django.shortcuts import render
from movie.models import MovieDetall
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    featured_movies = MovieDetall.objects.filter(kind__name='fd')
    top_rating_movies = MovieDetall.objects.filter(kind__name='tr')
    top_viewed_movies = MovieDetall.objects.filter(kind__name='tv')
    rencently_add_movies = MovieDetall.objects.filter(kind__name='ra')

    data = MovieDetall.objects.all().order_by('-id')

    # movie = data[1]
    # return render(request,'index.html',{'jpm':movie,'movies':data})

    return render(request,'index.html',
                  {'movies':data,
                   'fd':featured_movies,
                   'tr':top_rating_movies,
                   'tv':top_viewed_movies,
                   'ra':rencently_add_movies})

def index1(request,movie_id):
    # pramay key
    movie = MovieDetall.objects.filter(pk=movie_id)[0]
    return HttpResponse(movie.title)