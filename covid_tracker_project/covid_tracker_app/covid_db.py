from django.db import models

class DataEntry(models.Model):
    date = models.DateField()
    country = models.CharField(max_length=100)
    c_cases = models.PositiveIntegerField()
    c_deaths = models.PositiveIntegerField()

    def __str__(self):
        return self.country

    def set_date(self, date):
        self.date = date

    def set_country(self, country):
        self.country = country

    def set_cases(self, c_cases):
        self.c_cases = c_cases

    def set_deaths(self, c_deaths):
        self.c_deaths = c_deaths

    def get_date(self):
        return self.date

    def get_country(self):
        return self.country

    def get_cases(self):
        return self.c_cases

    def get_deaths(self):
        return self.c_deaths

class CovidDb:
    def __init__(self):
        self.dataTable = [[] for _ in range(17)]
        self.tableSize = 17

    def hash(self, country, size):
        sum = 0
        for i, c in enumerate(country):
            sum += (i + 1) * ord(c)
        return sum % size

    def add_entry(date, country_name, c_cases, c_deaths):
        country, created = DataEntry.objects.get_or_create(country=country_name)

        if created:
            country.date = date
            country.c_cases = c_cases
            country.c_deaths = c_deaths
        else:
            if compare_date(country.date, date):
                country.date = date
                country.c_cases += c_cases
                country.c_deaths += c_deaths

        country.save()

    def display_all_entries():
        return DataEntry.objects.all()

    def remove_entry(country_name):
        try:
            country = DataEntry.objects.get(country=country_name)
            country.delete()
        except DataEntry.DoesNotExist:
            pass


    def calculate(self, date, country, cases, deaths):
        entries = self.dataTable[self.hash(country, self.tableSize)]
        for i, entry in enumerate(entries):
            if entry.get_country() == country:
                new_entry = DataEntry(date, country, entry.get_cases() + cases, entry.get_deaths() + deaths)
                entries[i] = new_entry
                return
        new_entry = DataEntry(date, country, cases, deaths)
        entries.append(new_entry)

    def get_entry(country_name):
        try:
            return DataEntry.objects.get(country=country_name)
        except DataEntry.DoesNotExist:
            return None


    def compare_date(self, date1, date2):
        month1, day1, year1 = map(int, date1.split('/'))
        month2, day2, year2 = map(int, date2.split('/'))
        
        if year1 < year2 or (year1 == year2 and (month1 < month2 or (month1 == month2 and day1 < day2))):
            return True
        return False

    def find_next_prime(self, num):
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        num += 1
        while not is_prime(num):
            num += 1
        return num

    def rehash(self, new_size):
        new_table = [[] for _ in range(new_size)]
        for entries in self.dataTable:
            for entry in entries:
                index = self.hash(entry.get_country(), new_size)
                new_table[index].append(entry)
        self.dataTable = new_table
        self.tableSize = new_size

    def rehash_table(self):
        new_size = self.find_next_prime(self.tableSize * 2)
        self.rehash(new_size)
