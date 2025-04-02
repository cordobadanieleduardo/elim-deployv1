import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from elim.models import Cliente


class Command(BaseCommand):
    help = "Loads cliente data from CSV file"
    print('olee')
    def handle(self, *args, **options):
        datafile = settings.BASE_DIR / 'bases' / 'data' / 'cliente.csv'

        with open(datafile) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Cliente.objects.get_or_create(manufacturer=row[0], country=row[1])
                Cliente.objects.get_or_create(nombre=row[0])