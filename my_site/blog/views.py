from django.shortcuts import render
from  datetime import date
# Create your views here.
all_posts = [
    {
        
        "slug" :"in_the_mountainous" ,
        "image" : "mountains.jpg",
        "title" : "mountain hiking",
        "text" : "Mountain hiking embodies what hiking is all about: breathtaking views, fresh air, and a good workout. Here are the insider tips to be safe and have fun.",
        "date" : date(2021,11,29)
    }
,
    {
        "slug" :"hard-coding",
        "image" :"code.jpg",
        "title" :"coding evil",
        "text" : """
         a constant is hard coded and
        remains the same throughout the execution of the program. (2) Programming code that solves a problem but offers less flexibility for future changes.
        """,
        "date" : date(2021,11,25)
    }

]

def get_key(post):
    return post['date']



def starting_page(request):
    last_posts = sorted(all_posts,key=get_key)
    best_posts = last_posts[-3:]
    return render(request,'blog/index.html',{
        "post" : best_posts
    })

def posts(request):
    return render(request,"blog/all-posts.html",
        {"posts" :all_posts})

def full_post(request,slug):
    identified_one = next(post for post in all_posts if post['slug'] == slug)
    return render(request,"blog/post_detail.html",{
       "post": identified_one
    })