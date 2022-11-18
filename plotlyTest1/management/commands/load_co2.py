import csv
from datetime import date
from itertools import islice
from django.conf import settings
from django.core.management.base import BaseCommand
from plotlyTest1.models import CO2

class Command(BaseCommand):
    help = 'Load data from CO2 file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'co2_mm_mlo.csv'

        with open(datafile, 'r') as csvfile:
            reader = csv.DictReader(islice(csvfile,51,None))

            for row in reader:
                dt = date(
                    year=int(row['year']),
                    month=int(row['month']),
                    day=1
                )
                CO2.objects.get_or_create(date=dt, average=row['average'])
                


