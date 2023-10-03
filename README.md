# Flaskpedia

Flaskpedia is a simple demo web application built with Flask that allows users to search for and save Wikipedia articles. It provides a user-friendly interface for searching Wikipedia and saving interesting articles for later reading.

## Features

- Search for Wikipedia articles by keywords.
- View search results and read article summaries.
- Save favorite articles to your personal bookmark.
- Easily remove saved articles or clear your entire bookmarks.

## Getting Started

Follow the instructions below to set up and run Flask-pedia locally.

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/lmashraf/flaskpedia.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-pedia
   ```
3. Create and activate a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Set the SECRET_KEY environment variable. This key is used for session management.

    ```bash
    export SECRET_KEY=your_secret_key
    ```

2. Run the Flask application:
    ```bash
    python app.py
    ```

3. Access the application in your web browser by visiting http://localhost:5000.

### License
This project is licensed under the MIT License.