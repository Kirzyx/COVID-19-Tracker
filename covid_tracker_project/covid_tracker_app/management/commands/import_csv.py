from django.core.management.base import BaseCommand, CommandError
import csv
from covid_tracker_app.models import DataEntry
from datetime import datetime


class Command(BaseCommand):
    help = 'Import data from a CSV file into the DataEntry model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to import.')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']
        
        with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                date_reported = datetime.strptime(row[0], '%m/%d/%y').strftime('%Y-%m-%d')
                country = row[1]
                new_cases = int(row[2])
                new_deaths = int(row[3])
                
                 # If new_cases is negative, skip this row
                if new_cases < 0 or new_deaths < 0:
                    continue
                # You might want to adjust logic here if you're accumulating cases and deaths
                # For now, this just creates a new entry for each row
                DataEntry.objects.create(date=date_reported, country=country, c_cases=new_cases, c_deaths=new_deaths)

            self.stdout.write(self.style.SUCCESS(f"Data imported from {csv_file_path} successfully!"))
