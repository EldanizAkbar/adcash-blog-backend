from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Post
import json

class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()

    # Test for creating a category
    def test_create_category(self):
        url = reverse('categories-list')
        data = {'name': 'Test Category'}
        response = self.client.post(url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Category.objects.filter(name='Test Category').exists())

    # Test for creating a post
    def test_create_post(self):
        category = Category.objects.create(name='Test Category')
        url = reverse('posts-list')
        data = {
            'title': 'Test Post',
            'content': 'This is a test post',
            'categories': [category.id]
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Post.objects.filter(title='Test Post').exists())
        
    # Test for retrieving categories list
    def test_get_categories_list(self):
        url = reverse('categories-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'categories')


    # Test for retrieving posts list
    def test_get_posts_list(self):
        url = reverse('posts-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
    
        data = response.json()
        self.assertIsInstance(data, list)
        for post in data:
            self.assertIn('id', post)
            self.assertIn('title', post)
            self.assertIn('content', post)
            self.assertIn('categories', post)



    # Test for retrieving a specific post
    def test_update_post(self):
        post = Post.objects.create(title='Test Post', content='Old content')
        url = reverse('posts-detail', args=[post.id])
        data = {
            'title': 'Updated Post',
            'content': 'Updated content',
            'categories': []
        }
        response = self.client.put(url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        post.refresh_from_db()
        self.assertEqual(post.title, 'Updated Post')
        self.assertEqual(post.content, 'Updated content')


    # Test for deleting a post
    def test_delete_post(self):
        post = Post.objects.create(title='Test Post', content='To be deleted')
        url = reverse('posts-detail', args=[post.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Post.objects.filter(title='Test Post').exists())
