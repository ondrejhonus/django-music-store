# Django Music Store

Welcome to the **Django Music Store**! This is a web application built using **Django** and **MySQL**. The project represents an online music store specializing in selling musical instruments, with a particular focus on guitars.

## Requirements

- Python 3.x
- Pip
- Other dependencies listed in `requirements.txt`

## Functions
- Browse the music store
- Search by brand and model name
- Register as a user
- Login / Logout in the user dashboard

**If you have the permissions:**
- Add a new instrument
- Update an existing instrument
- Delete an existing instrument

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ondrejhonus/django-music-store.git
    cd django-music-store
    ```
2. Create a virtual enviroment
- **Linux:**
    ```bash
    python -m venv .venv
    ```
    And activate it
    ```bash
    source .venv/bin/activate
    ```
- **Windows:**
    ```bash
    python -m venv .venv
    ```
    And activate it:
    ```bash
    .venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver <port (optional)>
    ```

6. Access the application at http://127.0.0.1:8000 or `http://127.0.0.1:CUSTOM_PORT`.

## Existing users
#### Admin
- username: **admin**
- password: **admin**

#### Editor
- username: **editor**
- password: **update123**