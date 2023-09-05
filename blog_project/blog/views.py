from django.shortcuts import render
from datetime import date

all_posts = [
    {
        'slug': 'learning-django',
        'title': 'django course',
        'author': 'Mohammad Ordookhani',
        'image': 'django.png',
        'date': date(2021, 4, 5),
        'short_description': 'this is django course in toplearn from zero to hero',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad adipisci at aut consectetur debitis deserunt dicta 
            dolor dolores ducimus eius enim error ex fugiat hic ipsum iste minima nisi nobis quae qui reiciendis,
            repellendus rerum sequi tempore unde voluptates voluptatum? 
            """,

    },

    {
        'slug': 'learning-python',
        'title': 'python course',
        'author': 'Mohammad Ordookhani',
        'image': 'python.png',
        'date': date(2021, 6, 3),
        'short_description': 'this is django course in toplearn from zero to hero',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad adipisci at aut consectetur debitis deserunt dicta 
            dolor dolores ducimus eius enim error ex fugiat hic ipsum iste minima nisi nobis quae qui reiciendis,
            repellendus rerum sequi tempore unde voluptates voluptatum? 
            """,

    },
    {
        'slug': 'learning-machine-learning',
        'title': 'ml course',
        'author': 'Mohammad Ordookhani',
        'image': 'ml.png',
        'date': date(2021, 3, 1),
        'short_description': 'this is django course in toplearn from zero to hero',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad adipisci at aut consectetur debitis deserunt dicta 
            dolor dolores ducimus eius enim error ex fugiat hic ipsum iste minima nisi nobis quae qui reiciendis,
            repellendus rerum sequi tempore unde voluptates voluptatum? 
            """,

    }
]

def get_date(post):
    return post['date']

def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request, 'blog/index.html', {
        'latest_posts': latest_posts
    },)

def posts(request):
    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog/all-posts.html', context)

def single_post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': post
    })