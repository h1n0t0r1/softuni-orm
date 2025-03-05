import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Author, Book, Review

# Create and check models
from main_app.models import Author, Book, Review

# Run and print your queries
def find_books_by_genre_and_language(genre, language):
    books = Book.objects.filter(genre=genre, language=language)
    return books

def find_authors_nationalities():
    result = []
    authors = Author.objects.exclude(nationality__isnull=True)
    for a in authors:
        result.append(f"{a.first_name} {a.last_name} is {a.nationality}")

    return '\n'.join(result)


def order_books_by_year():
    books = Book.objects.all().order_by('publication_year', 'title')
    return '\n'.join(f'{b.publication_year} year: {b.title} by {b.author}' for b in books)


def delete_review_by_id(id):
    review = Review.objects.get(id=id)
    review.delete()
    return f'Review by {review.reviewer_name} was deleted'


def filter_authors_by_nationalities(nation:str)->str:
    result = []
    authors = Author.objects.filter(nationality=nation).order_by('first_name', 'last_name')
    for a in authors:
        result.append(a.biography) if a.biography is not None else result.append(f'{a.first_name} {a.last_name}')

    return '\n'.join(result)


def filter_authors_by_birth_year(start_year, end_year):
    result = []
    authors = Author.objects.filter(birth_date__month__range=(start_year, end_year)).order_by('-birth_date')
    for a in authors:
        result.append(f"{a.birth_date}: {a.first_name} {a.last_name}")

    return '\n'.join(result)

def change_reviewer_name(oldname, new_name):
    Review.objects.filter(reviewer_name=oldname).update(reviewer_name=new_name)
    return Review.objects.all()