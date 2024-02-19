import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from blog.models import *

class Command(BaseCommand):
    help = 'Seed data for Blog and Category models'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))

        # Seed categories
        categories_data = [
            {'name': 'Technology', 'description': 'Tech-related category description'},
            {'name': 'Travel', 'description': 'Travel-related category description'},
            {'name': 'Food', 'description': 'Food-related category description'},
            {'name': 'Fashion', 'description': 'Fashion-related category description'},
            {'name': 'Science', 'description': 'Science-related category description'},
        ]

        for category_data in categories_data:
            Category.objects.create(
                name=category_data['name'],
                description=category_data['description']
            )

        # Seed blogs
        blogs_data = [
            {'title': 'Sample Blog 1', 'content': 'Content of sample blog 1', 'pub_date': timezone.now()},
            {'title': 'Sample Blog 2', 'content': 'Content of sample blog 2', 'pub_date': timezone.now()},
            {'title': 'Sample Blog 3', 'content': 'Content of sample blog 3', 'pub_date': timezone.now()},
            {'title': 'Sample Blog 4', 'content': 'Content of sample blog 4', 'pub_date': timezone.now()},
            {'title': 'Sample Blog 5', 'content': 'Content of sample blog 5', 'pub_date': timezone.now()},
        ]

        for blog_data in blogs_data:
            random_category = Category.objects.order_by('?').first()
            Blog.objects.create(
                title=blog_data['title'],
                content=blog_data['content'],
                pub_date=blog_data['pub_date'],
                category=random_category
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
