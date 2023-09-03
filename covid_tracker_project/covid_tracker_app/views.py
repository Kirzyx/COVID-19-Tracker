from django.shortcuts import render, redirect
from .models import DataEntry
from django.db.models import Sum
from django.urls import reverse
from django.contrib import messages
from datetime import datetime



from datetime import datetime

def add_entry(request):
    if request.method == "POST":
        country_name = request.POST.get('country')
        date_str = request.POST.get('date')
        c_cases = int(request.POST.get('c_cases', 0))
        c_deaths = int(request.POST.get('c_deaths', 0))

        # Convert string date to datetime.date object
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        # Try to get the entry for the given country
        entry, created = DataEntry.objects.get_or_create(
            country=country_name, 
            defaults={'date': date, 'c_cases': c_cases, 'c_deaths': c_deaths}
        )
        
        if not created:
            if entry.date <= date:  # Only update if it's a newer or same date
                entry.date = date
                entry.c_cases += c_cases  # Add the new cases to the existing total
                entry.c_deaths += c_deaths  # Add the new deaths to the existing total
                entry.save()
        
        return redirect('index')  # Redirect to the display page after adding

    return render(request, 'covid_tracker_app/add_entry.html')


def display_all_entries(request):
    entries = DataEntry.objects.all()
    return render(request, 'display.html', {'entries': entries})

def remove_entry_page(request):
    if request.method == 'POST':
        country_name = request.POST.get('country_name')
        if country_name:
            DataEntry.objects.filter(country=country_name).delete()
            messages.success(request, 'Data entry successfully deleted.')
            return redirect('index')  # Redirect to the display page after deletion
    return render(request, 'covid_tracker_app/remove_entry.html')


def get_entry_page(request):
    if request.method == "POST":
        country_name = request.POST.get('country_name')
        return redirect(reverse('display_country_details', args=[country_name]))

    return render(request, 'covid_tracker_app/get_entry.html')

def display_country_details(request, country_name):
    # Check if the country name is passed correctly
    print(f"Country Name: {country_name}")

    # Filter data for the specified country
    country_data = DataEntry.objects.filter(country__iexact=country_name)


    # Print the QuerySet
    print(country_data)

    # Aggregate data for the specified country
    summary = country_data.aggregate(
        total_cases=Sum('c_cases'),
        total_deaths=Sum('c_deaths')
    )

    # Print the summary
    print(summary)

    # If no data is found for the country, raise an exception
    if not summary['total_cases'] and not summary['total_deaths']:
        return render(request, 'covid_tracker_app/display_country.html', {'error_message': f"No data available for {country_name}."})
    else:
        return render(request, 'covid_tracker_app/display_country.html', {'country_name': country_name, 'summary': summary})

def index(request):
    entries = DataEntry.objects.all()
    context = {'entries': entries}
    return render(request, 'covid_tracker_app/index.html', context)

def display_country_summary(request):
    summary = DataEntry.objects.values('country').annotate(
        total_cases=Sum('c_cases'),
        total_deaths=Sum('c_deaths')
    ).order_by('country')
    return render(request, 'covid_tracker_app/country_summary.html', {'summary': summary})
