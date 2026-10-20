# Expense Tracker — Python & Flask

A simple, pink-themed expense tracking web application built with Python and Flask. Add expenses, view your spending history, and see how your expenses are distributed across categories.

## Features

- **Add expenses:** Enter an amount, category, and description.
- **Expense history:** View recorded expenses in a table.
- **Total spending:** See the combined amount of recorded expenses.
- **Category-wise summary:** Check spending totals for each category.
- **Pink-themed interface:** A clean, responsive dashboard built with HTML and CSS.

## Tech Stack

- Python
- Flask
- HTML
- CSS
- Jinja2 templates

## Project Structure

```text
expense_tracker_cli/
├── app.py
├── expense_tracker.py
├── requirements.txt
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sanvichopra06/expense-tracker-python.git
cd expense-tracker-python
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open the local address shown in your terminal in your browser.

## Important Note

This version stores expenses in memory. The recorded expenses are not permanently saved and may disappear when the application restarts.

## Future Improvements

- Store expenses in SQLite.
- Add expense editing and deletion.
- Add spending charts and filters.
- Add monthly spending summaries.

---

Built as a Python mini-project while learning Flask and web development.
