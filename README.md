# Interactive Quiz Web App

A simple interactive quiz web application built using Flask, MySQL, and Flask-Login. It allows users to log in, take a quiz, and have their scores stored.

## Features
- **User Authentication**
- **Quiz Timer**
- **Score Tracking**
- **Basic Admin Interface**

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sabbakar/interactive-quiz-app.git
   cd interactive-quiz-app
   ```
2.  **Configure the App**:
   - Edit `flask_app.py` to update MySQL username/password.

3.  **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4.  **Set up MySQL Database**:
   - Install MySQL.
   - Create a database `quiz_app_db`.
   - Run:
     ```bash
     python3 tables.py
     ```

5. **Run the App**:
   ```bash
   python3 flask_app.py
   ```

   Visit `http://localhost:5000/`.

## Usage

- Login (add desired username and password first directly in DB).
- Take quiz.
- View score.
- Logout.

## Directory Structure

```
interactive-quiz-app
├── flask_app.py
├── models.py
├── tables.py
├── static
│   ├── css
│   │   └── main.css
│   └── images
│       ├── background_image1.jpg
│       └── background_image.jpg
├── templates
│   ├── login.html
│   ├── quiz.html
│   └── quiz_completed.html
├── requirements.txt
└── README.md
```

## Future Enhancements
- Better admin panel.
- Leaderboard.
- Email notifications.

## Contact Me

Feel free to reach out if you have any questions, suggestions, or feedback.

- Email: sadeeqsas14@gmail.com
- [Twitter](https://twitter.com/sadiq__abubakar)
