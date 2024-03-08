from django.http import JsonResponse
from .models import Category, Post
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def categories_list(request):
    if request.method == 'GET':
        # GET request to fetch all categories
        categories = Category.objects.all()
        data = {
            'categories': list(categories.values()), 
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        # POST request to create a new category
        try:
            data = json.loads(request.body) 
            name = data.get('name') 
            if name:
                Category.objects.create(name=name) 
                return JsonResponse({'message': 'Category added successfully'}, status=201)
            else:
                return JsonResponse({'error': 'Name is required'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    

@csrf_exempt
def posts_list(request):
    if request.method == 'GET':
        # GET request to fetch all posts
        posts = Post.objects.all()
        data = [
            {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'categories': [{'id': category.id, 'name': category.name} for category in post.categories.all()]
            }
            for post in posts
        ]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        # POST request to create a new post
        try:
            data = json.loads(request.body) 
            title = data.get('title')
            content = data.get('content')
            category_ids = data.get('categories', [])

            if title and content and category_ids:
                categories = Category.objects.filter(id__in=category_ids)
                if len(categories) != len(category_ids):
                    return JsonResponse({'error': 'One or more categories not found'}, status=404)

                post = Post.objects.create(title=title, content=content)
                post.categories.set(categories)
                post.save()

                return JsonResponse({'message': 'Post added successfully', 'post_id': post.id}, status=201)
            else:
                return JsonResponse({'error': 'Title, content, and at least one category are required'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)  
    
    
    
    

@csrf_exempt
def posts_detail(request, pk):
    if request.method == 'GET':
        # GET request to fetch a single post by ID
        try:
            post = Post.objects.get(pk=pk)
            data = {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'category': post.category.name
            }
            return JsonResponse(data)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
    if request.method == 'PUT':
        # PUT request to update a post
        try:
            data = json.loads(request.body)
            title = data.get('title')
            content = data.get('content')
            category_ids = data.get('categories')

            if title and content:
                post = Post.objects.get(pk=pk)
                post.title = title
                post.content = content
                
                # Clear existing categories and add new ones
                post.categories.clear()
                for category_id in category_ids:
                    category = Category.objects.get(id=category_id)
                    post.categories.add(category)

                post.save()
                return JsonResponse({'message': 'Post updated successfully'}, status=200)
            else:
                return JsonResponse({'error': 'Title and content are required'}, status=400)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'One or more categories do not exist'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    elif request.method == 'DELETE':
        # DELETE request to delete a post
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return JsonResponse({'message': 'Post deleted successfully'}, status=204)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)      
    
    


def home(request):
    # Home view, just returning a welcome message
    return JsonResponse({'message': 'Welcome to the Blog API!'})    