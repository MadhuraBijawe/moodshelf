from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Mood, Book, MoodGenreMap, Favorite
from django.contrib.auth.decorators import login_required
from .models import MoodLog
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.db import IntegrityError
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Favorite
from django.shortcuts import get_object_or_404, redirect

# ✅ Home Page
def index(request):
    moods = Mood.objects.all()
    return render(request, 'index.html', {'moods': moods})

# ✅ Book Suggestions based on Mood
def get_books_by_mood(request):
    mood_id = request.GET.get('mood_id')
    if not mood_id:
        return JsonResponse({'error': 'Mood ID not provided'}, status=400)

    genres = MoodGenreMap.objects.filter(mood_id=mood_id).values_list('genre', flat=True)
    books = Book.objects.filter(genre__in=genres)
    books_data = list(books.values('id', 'title', 'author', 'genre', 'description', 'image_url'))[:5]
    return JsonResponse({'books': books_data})

# ✅ Login Page
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profile")  # ✅ make sure this view exists in urls.py
        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")

# ✅ Register Page
def register_view(request):
    moods = Mood.objects.all()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        email = request.POST.get("email")
        mood = request.POST.get("mood")

        if not all([username, password, confirm_password, email, mood]):
            return render(request, "register.html", {
                "error": "All fields are required.",
                "moods": moods
            })

        if password != confirm_password:
            return render(request, "register.html", {
                "error": "Passwords do not match.",
                "moods": moods
            })

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists.",
                "moods": moods
            })

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # ✅ Send Welcome Email
            subject = "Welcome to MoodShelf 🎉"
            html_content = render_to_string("email/welcome_email.html", {
                "username": username,
                "mood": mood
            })
            email_message = EmailMultiAlternatives(subject, "", to=[email])
            email_message.attach_alternative(html_content, "text/html")
            email_message.send()

            messages.success(request, "Account created! Please login.")
            return redirect("login")

        except Exception as e:
            print("❌ Error during registration:", e)
            messages.error(request, f"Something went wrong: {e}")
            return render(request, "register.html", {
                "error": "Something went wrong. Try again.",
                "moods": moods
            })

    return render(request, "register.html", {"moods": moods})



# ✅ same here
def explore_view(request):
    return render(request, 'explore.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')
@login_required
def profile_view(request):
    mood_history = MoodLog.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'profile.html', {'mood_history': mood_history})
@login_required
def favorites_view(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('book')
    return render(request, 'favorites.html', {'favorites': favorites})


# ✅ Add to Favorites
@login_required
def add_favorite(request, book_id):
    book = Book.objects.get(id=book_id)
    Favorite.objects.get_or_create(user=request.user, book=book)
    return JsonResponse({'message': 'Book added to favorites'})

# ✅ Show Favorites
@login_required
def list_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('book')
    books = [
        {
            'title': fav.book.title,
            'author': fav.book.author,
            'genre': fav.book.genre,
            'description': fav.book.description,
            'image_url': fav.book.image_url
        } for fav in favorites
    ]
    return JsonResponse({'favorites': books})


@login_required
def remove_favorite(request, book_id):
    fav = get_object_or_404(Favorite, user=request.user, book_id=book_id)
    fav.delete()
    return redirect('favorites')
