# GYM Management System

Welcome to the GYM Management System! This Django-based web application allows gym visitors, registered users, and administrators to interact with the gym's services, packages, trainers, and more.

## Features

- **Guest Users:**
  - View general information about the gym.
  - Send inquiries through the contact us page.

- **Registered Users:**
  - Apply for gym packages after one-time registration.
  - View booking history and payment details.
  - Update their profiles and change passwords.

- **Admin:**
  - Manage the gym's operations and data.
  - Access an overview of bookings, packages, and more.
  - Add, edit, and delete categories, package types, and packages.
  - Check booking details and update payment information.
  - Generate reports for bookings and registered users.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mi-dexigner/gym-management.git
   cd gym-management 
   
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install project dependencies:
   ```bash
   pip install -r requirements.txt

4. Run database migrations:
   ```bash
   python manage.py migrate
   
5. Start the development server:
   ```bash
   python manage.py runserver

6. Access the development server at http://127.0.0.1:8000/ in your web browser.

