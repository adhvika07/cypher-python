# Vigenère Cipher Django Application

## Overview

This project is a Django web application that implements the Vigenère cipher, a method of encrypting alphabetic text. The application provides a user-friendly interface to encrypt and decrypt messages using a Vigenère cipher, with features to handle both the encryption and decryption processes.

## Features

- **Encryption and Decryption:** Encrypt and decrypt text using a Vigenère cipher with a user-defined key.
- **User Interface:** A clean and responsive web interface built with HTML and CSS for ease of use.
- **Static and Media Files Handling:** Configured to manage and serve static files (CSS, JavaScript) and media files effectively.

## Project Structure

The project is organized as follows:

vigenere_cipher/
    ├── cypher_app/
    │   ├── migrations/
    │   ├── static/
    │   │   └── cypher_app/
    │   │       └── style.css
    │   ├── templates/
    │   │   └── cypher_app/
    │   │       └── index.html
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   └── urls.py
    ├── vigenere_cipher/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── db.sqlite3  # SQLite database file
    └── README.md

## Installation

1. **Clone the Repository:**

   git clone https://github.com/adhvika07/vigenere_cipher.git
   cd vigenere_cipher
   
2. **Set up a Virtual Environment:**

   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. **Install Requirements:**

   pip install -r requirements.txt

4. **Apply Migrations:**

   python manage.py migrate

5. **Run Development Server:**

   python manage.py runserver


## Usage

1. **Navigate to the Application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

2. **Encrypt/Decrypt Text:**
   - Enter the text you want to encrypt in the designated input field.
   - Provide a custom key for the Vigenère cipher.
   - Click the "Encrypt" button to encrypt the text.
   - The encrypted text will be displayed.
   - To decrypt the text, click the "Decrypt" button, and the original message will be shown.

## Configuration

- **Static Files:** Ensure your `STATICFILES_DIRS` in `settings.py` is correctly pointing to the directory where your static files are stored.
- **Media Files:** Configure `MEDIA_URL` and `MEDIA_ROOT` in `settings.py` if handling user-uploaded files.

## Troubleshooting

- **Static Files Not Loading:** Ensure that the `STATICFILES_DIRS` path is correctly configured and that the static directory exists. Clear your browser cache if styles are not updated.
- **Import Errors:** Verify that all app configurations in `settings.py` are correct and that `apps.py` is properly set up.
- **Database Errors:** If you encounter issues with `db.sqlite3`, ensure that the file exists in the project root and that the database migrations are applied.

## Contributing

If you would like to contribute to this project, please follow these steps:
1. **Fork the Repository:** Create a personal copy of the repository on GitHub.
2. **Create a Branch:** Develop your changes in a separate branch.
3. **Make Changes:** Implement your improvements or fixes.
4. **Submit a Pull Request:** Submit a pull request with a clear description of your changes.

Ensure that your code adheres to the existing style and includes appropriate tests. All contributions are appreciated!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions or feedback, please reach out to [iyeradhvika@gmail.com](mailto:iyeradhvika@gmail.com).
