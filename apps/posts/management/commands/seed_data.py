# yourapp/management/commands/seed_data.py

import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from apps.posts.models import Category, Blog

fake = Faker()

class Command(BaseCommand):
    help = 'Seed data for Blog and Category models'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))

        # Seed categories
        categories = ['Technology', 'Travel', 'Food', 'Fashion', 'Science']
        for category_name in categories:
            Category.objects.create(
                name=category_name,
                description=fake.paragraph()
            )

        # Seed blogs
        for _ in range(5):
            random_category = Category.objects.order_by('?').first()
            Blog.objects.create(
                title=fake.sentence(),
                content=fake.paragraphs(),
                pub_date=timezone.now(),
                category=random_category
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
