# Dynamic Portfolio with Django

This repository contains the source code for a dynamic portfolio application built with Python and the Django framework. Unlike a static website, this project serves all portfolio content from a database and allows for easy management of projects through the Django admin panel.

---

## Screenshots

<table>
  <tr>
    <td width="50%"><strong>Frontend View</strong></td>
    <td width="50%"><strong>Django Admin Panel</strong></td>
  </tr>
  <tr>
    <td><img src="https://github.com/onurmertanarat/PortfolioApp/blob/main/portfolio_app/docs/images/portfolioapp-screenshot-1.PNG" alt="Portfolio Frontend View"></td>
    <td><img src="https://github.com/onurmertanarat/PortfolioApp/blob/main/portfolio_app/docs/images/portfolioapp-screenshot-3.PNG" alt="Django Admin Panel"></td>
  </tr>
</table>

---

## Features

* **Dynamic Content Management:** All projects are stored in a database and rendered dynamically in the templates. No hardcoded project information.
* **Admin Panel Integration:** Projects can be easily created, updated, and deleted through Django's built-in admin interface without touching the code.
* **Secure Configuration:** Sensitive information such as the `SECRET_KEY` and `DEBUG` settings are kept separate from the source code and managed via environment variables (`.env` file), following security best practices.
* **Media File Handling:** Properly configured to handle user-uploaded images for each portfolio project.

---

## Technology Stack

* **Backend:** Python, Django
* **Database:** SQLite (Default)
* **Frontend:** HTML, CSS, JavaScript
* **Python Libraries:**
    * `Pillow`: For image processing and handling `ImageField`.
    * `python-decouple`: For separating settings from source code.
    * `django-cleanup`: To automatically delete old image files.

---

## Local Setup and Installation

To run this project on your local machine, please follow these steps:

1.  **Clone the Repository**
    ```sh
    git clone [https://github.com/onurmertanarat/PortfolioApp.git](https://github.com/onurmertanarat/PortfolioApp.git)
    cd PortfolioApp
    ```

2.  **Create and Activate a Virtual Environment**
    ```sh
    # Create venv
    python -m venv venv

    # Activate on Windows
    venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Create a `.env` File**
    Create a `.env` file in the root directory and add the following, using your own secret key.
    ```env
    SECRET_KEY='your-own-secret-key-here'
    DEBUG=True
    ```

4.  **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

5.  **Apply Database Migrations**
    ```sh
    python manage.py migrate
    ```

6.  **Create a Superuser**
    This will allow you to log in to the admin panel.
    ```sh
    python manage.py createsuperuser
    ```

7.  **Run the Development Server**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://120.0.0.1:8000/`.
    The admin panel will be at `http://120.0.0.1:8000/admin/`.

---

## Contact

Onur Mert Anarat

[linkedin.com/in/onurmertanarat](https://www.linkedin.com/in/onurmertanarat)
