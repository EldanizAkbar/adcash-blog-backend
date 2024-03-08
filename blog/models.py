from django.db import models
from django.db.models.signals import post_migrate

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Function to create default categories when migrations are applied
def create_default_categories(**kwargs):
    Category.objects.get_or_create(name='Sport')
    Category.objects.get_or_create(name='Education')
    Category.objects.get_or_create(name='Science')

# Signal to create default categories after migrations
def create_default_categories_after_migrate(sender, **kwargs):
    if kwargs['app_config'].name == 'blog':
        create_default_categories()

# Connect signal to post_migrate
post_migrate.connect(create_default_categories_after_migrate)

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title
