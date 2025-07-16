import csv
import os
from django.core.management.base import BaseCommand
from products.models import Product
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Import products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='Path to CSV file (default: products.csv)')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file'] or 'products.csv'

        if not os.path.exists(file_path):
            self.stderr.write(self.style.ERROR(f"❌ File not found: {file_path}"))
            return

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0

            for row in reader:
                title = row['title'].strip()
                description = row['description'].strip()
                price = float(row['price'])
                image = row['image'].strip()
                slug = row.get('slug') or slugify(title)
                is_featured = row.get('is_featured', 'False').strip().lower() in ['true', '1', 'yes']

                product, created = Product.objects.get_or_create(
                    title=title,
                    defaults={
                        'description': description,
                        'price': price,
                        'image': image,
                        'slug': slug,
                        'is_featured': is_featured
                    }
                )

                if created:
                    count += 1
                    self.stdout.write(self.style.SUCCESS(f"✔ Added: {title}"))
                else:
                    self.stdout.write(f"ℹ Already exists: {title}")

            self.stdout.write(self.style.SUCCESS(f"\n✅ Import complete. {count} new products added."))
