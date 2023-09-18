# Covid Tracker Django Project

## 📌 Description

The Covid Tracker is a web application built using Django. It allows users to manage Covid-19 data entries by country, providing a way to add, update, view, and remove data related to Covid-19 cases and deaths.

## 🚀 Features

- **Add/Update Data**: Users can input new data entries or update existing ones by specifying the country, date, number of cases, and number of deaths.
- **View Data**: All added entries can be viewed in a structured table format.
- **Search Data**: Users can view specific data entries by country.
- **Delete Data**: Users have the option to remove data entries by country.

## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kirzyx/COVID-19-Tracker.git
cd COVID-19-Tracker
```

### 2. Setup Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 📖 Usage

1. Navigate to the dashboard to access the core features.
2. Add or update data entries using the provided form.
3. View all data entries or search by country.
4. Remove data entries as needed.

## 🙏 Acknowledgments
- This project was inspired by an assignment for CSCP 2430-02 at Seattle University.
- The project served as a hands-on approach to learning Python and Django.
- Thanks to Django's comprehensive documentation and community.
