from django.shortcuts import render, redirect
from .models import DataEntry

def add_entry(request):
    if request.method == "POST":
        country_name = request.POST.get('country')
        date = request.POST.get('date')
        c_cases = int(request.POST.get('c_cases', 0))
        c_deaths = int(request.POST.get('c_deaths', 0))
        
        # Update or create the entry
        entry, created = DataEntry.objects.get_or_create(country=country_name)
        if created or (not created and entry.date <= date):  # Only update if it's a newer date
            entry.date = date
            entry.c_cases = c_cases
            entry.c_deaths = c_deaths
            entry.save()
        
        return redirect('display_entries')  # Redirect to the display page after adding

    return render(request, 'covidtracker/add_entry.html')

def display_all_entries(request):
    entries = DataEntry.objects.all()
    return render(request, 'covidtracker/display.html', {'entries': entries})

def remove_entry(request, country_name):
    def remove_entry(request, country_name):
        DataEntry.objects.filter(country=country_name).delete()
        return redirect('display_entries')  # Redirect to the display page after deletion


def get_entry(request, country_name):
    def get_entry(request, country_name):
        try:
            entry = DataEntry.objects.get(country=country_name)
        except DataEntry.DoesNotExist:
            entry = None
        return render(request, 'covidtracker/get_entry.html', {'entry': entry})

