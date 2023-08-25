COVID-19 Data Tracker
The COVID-19 Data Tracker is a Django web application that allows users to manage and track COVID-19 data worldwide. The application utilizes a hash table data structure to store and manage COVID-19 data entries for different countries.

Features
Add new COVID-19 data entries (cumulative cases and deaths) for various countries.
Retrieve COVID-19 data for a specific country.
Remove COVID-19 data entries for a specific country.
Display the current COVID-19 data hash table.
Setup and Installation
Make sure you have Python installed. This project was developed using Python 3. It's recommended to use a virtual environment for isolation.

Install Django framework:

Copy code
pip install django
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/covid-data-tracker.git
cd covid-data-tracker
Run the migrations to set up the database:

Copy code
python manage.py migrate
Start the development server:

Copy code
python manage.py runserver
Open a web browser and navigate to http://127.0.0.1:8000/ to access the COVID-19 Data Tracker.

Usage
Click on the "Add Entry" link to add a new COVID-19 data entry for a specific country. Make sure to provide the date, country name, cumulative cases, and cumulative deaths.
Use the "Get Entry" link to retrieve the COVID-19 data for a specific country.
To remove a COVID-19 data entry, select the "Remove Entry" option and provide the country name.
Click on the "Display Table" link to view the current state of the hash table.
Contributing
Contributions are welcome! If you find any bugs or want to enhance the application, feel free to submit pull requests.

Acknowledgments
This project was inspired by an assignment for CSCP 2430-02 at Seattle University.
