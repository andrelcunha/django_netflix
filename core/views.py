from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Movie, MovieList

# Create your views here.
@login_required(login_url='login')
def index(request):
    genre_choices = Movie.GENRE_CHOICES
    movies = Movie.objects.all()
    context = {
        'genre_choices': genre_choices,
        'movies': movies
        }
    return render(request, 'index.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # return redirect('login')

                #login user
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

@login_required(login_url='login')
def movie(request, pk):
    movie_details = Movie.objects.get(uu_id=pk)
    context = {
        'movie_details': movie_details
    }
    return render(request, 'movie.html', context)

@login_required(login_url='login')
def my_list(request):
    genre_choices = Movie.GENRE_CHOICES

    my_list = MovieList.objects.filter(user=request.user).order_by('id').select_related('movie')
    movies = [list_item.movie for list_item in my_list]

    context = {
        'genre_choices': genre_choices,
        'movies': movies
        }
    return render(request, 'my_list.html', context) 

@login_required(login_url='login')
def add_to_list(request):
    if request.method == 'POST':
        movie_url = request.POST.get('movie_id')
        movie_id = movie_url.split('/')[-1]
        movie = get_object_or_404(Movie, uu_id=movie_id)
        _, created = MovieList.objects.get_or_create(user=request.user, movie=movie)
        if created:
            response_data = {'status':'success', 'message': 'Added ✓'}
        else:
            response_data = {'status':'info', 'message': 'Movie already in your list'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'status':'error', 'message': 'Invalid request'}, status=400)