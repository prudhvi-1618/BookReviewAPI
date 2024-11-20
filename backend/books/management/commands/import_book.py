import pandas as pd
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = "Import books from a CSV file using Pandas"

    def add_arguments(self, parser):
        parser.add_argument('data.csv', type=str, help="Path to the CSV file to import")

    def handle(self, *args, **kwargs):
        csv_file = kwargs['data.csv']
        try:
            # Load the CSV file
            df = pd.read_csv(csv_file)

            # Iterate through DataFrame rows
            for index, row in df.iterrows():
                book, created = Book.objects.get_or_create(
                    isbn=row['isbn13'],
                    defaults={
                        'title': row['title'],
                        'author': row['authors'],
                        'genre': row['categories'],
                        'cover_image_url': row['thumbnail'],
                    }
                )
                if created:
                    self.stdout.write(f"Added: {book.title}")
                else:
                    self.stdout.write(f"Skipped (already exists): {book.title}")
            self.stdout.write("Import completed successfully!")
        except Exception as e:
            self.stderr.write(f"Error: {str(e)}")

