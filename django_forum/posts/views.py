# Import necessary modules and classes from Django
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.

# VIEW FOR DISPLAYING ALL POSTS AND ADDING NEW POSTS
def index(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance using POST data
        form = PostForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # If the form is valid, save the data to the database
            form.save()
            # Redirect to the homepage
            return HttpResponseRedirect('/')
        else:
            # If the form is not valid, redirect and show errors in JSON format
            return HttpResponseRedirect(form.errors.as_json())

    # Retrieve the latest 20 posts from the database
    posts = Post.objects.all()[:20]

    # Render the 'posts.html' template with the list of posts
    return render(request, 'posts.html', {'posts': posts})

# DELETE FUNCTION
def delete(request, post_id):
    # Get the post with the given 'post_id' from the database
    post = Post.objects.get(id=post_id)
    
    # Delete the post
    post.delete()
    
    # Redirect to the homepage
    return HttpResponseRedirect('/')

# EDIT FUNCTION
def edit(request, post_id):
    # Retrieve the post with the given 'post_id' from the database
    posts = Post.objects.get(id=post_id)

    # Check if the request method is POST (usually for form submissions)
    if request.method == 'POST':
        # Create a form instance for editing the post
        form = PostForm(request.POST, request.FILES, instance=posts)

        # Check if the form data is valid
        if form.is_valid():
            # If the form is valid, save the changes to the post in the database
            form.save()
            
            # Redirect the user to the homepage after successful editing
            return HttpResponseRedirect('/')
        else:
            # If the form is not valid, return a response indicating that it's not valid
            return HttpResponseRedirect("not valid")

    # If the request method is not POST (e.g., a GET request), or if the form is not submitted,
    # render an 'edit.html' template with the post information for editing
    return render(request, 'edit.html', {'posts': posts})
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        #If the form is valid
        if form.is_valid():
            #Yes, Save
            form.save()
            #Redirect to home
            return HttpResponseRedirect('/')
        else:
            #No, Show Error
            return HttpResponseRedirect(form.erras.as_json())

    # Get all posts, limit = 20
    posts =Post.objects.all()[:20]

    # Show/Render Pages
    return render(request, 'posts.html',
                    {'posts': posts})
#DELETE-FUNCTION--------------------------------------------------
def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')
#EDIT-FUNCTION----------------------------------------------------

# This function handles an HTTP request to edit a post, identified by its 'post_id'.

def edit(request, post_id):
    # Retrieve the post with the given 'post_id' from the database.
    posts = Post.objects.get(id=post_id)

    # Check if the request method is POST (usually for form submissions).
    if request.method == 'POST':
        # Create a form instance, presumably for editing the post, 
        # and populate it with data from the request (both form data and uploaded files).
        form = PostForm(request.POST, request.FILES, instance=posts)

        # Check if the form data is valid.
        if form.is_valid():
            # If the form is valid, save the changes to the post in the database.
            form.save()

            # Redirect the user to the homepage after successful editing.
            return HttpResponseRedirect('/')
        else:
            # If the form is not valid, return a response indicating that it's not valid.
            return HttpResponseRedirect("not valid")

    # If the request method is not POST (e.g., a GET request), or if the form is not submitted,
    # render an 'edit.html' template with the post information for editing.
    return render(request, 'edit.html', {'posts': posts})
