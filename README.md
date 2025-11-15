# Flask ToDo App

A simple ToDo application built using Flask. It lets you create tasks, edit them and mark them as done. This project is good for learning Flask basics like routing, templates, forms and a small database.

## Features
- Add new tasks
- Edit existing tasks
- Mark tasks as completed
- View completed tasks
- Uses SQLite for database
- Simple and clean UI

## Tech Stack
- Python
- Flask
- SQLite
- HTML / CSS (Jinja templates)

## Project Setup

### 1. Create virtual environment
```
python -m venv env
```

### 2. Activate it
Windows:
```
env\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run the application
```
python run.py
```

## Project Structure
```
project/
│── templates/
│   ├── index.html
│   ├── edit.html
│   ├── Done.html
│   └── base.html
│── instance/
│── run.py
│── requirements.txt
│── .gitignore
```

## Future Improvements
- Add user login
- Add due dates
- Add categories for tasks
- Add API endpoints

## License
This project is free to use for learning and personal use.
