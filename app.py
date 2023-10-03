from flask import Flask, render_template, request, redirect, url_for, session, flash
import wikipedia
import os

app = Flask(__name__)

# API Key is stored as env. variable
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

# Home
@app.route('/')
def index():
        return render_template("index.html")

# About
@app.route('/about')
def about():
            return render_template("about.html")

# Search
@app.route('search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        keyword = request.form.get('search')
        if keyword:
            session['keyword'] = keyword
            return redirect(url_for('result'))
    return render_template("search.html")

# Result
@app.route('/result')
def result():
    keyword = session.get('keyword')
    if keyword:
        page = get_page(keyword)
        return render_template("result.html", page=page)
    else:
        return "No keyword provided."

# Retrieve Wikipedia page by search term.
def get_page(keyword):
    try:
        page = wikipedia.page(keyword)
    except wikipedia.exceptions.PageError:
        page = wikipedia.page(wikipedia.random())
    except wikipedia.exceptions.DisambiguationError:
        page_titles = wikipedia.search(keyword)
        title = page_titles[0] if page_titles else 'No results found'
        page = wikipedia.page(title)
    return page

# Bookmark
@app.route('/bookmarked')
def bookmarked_pages():
    bookmarked_pages = session.get('bookmarks', [])
    return render_template('bookmarks.html', bookmarked_pages=bookmarked_pages)

@app.route('/clear_bookmark')
def clear_saved():
    session['bookmarks'] = []
    flash('Bookmarks cleared!', 'success')
    return redirect(url_for('bookmarks'))

@app.route('/remove_bookmark/<page_title>', methods=['POST'])
def delete_bookmark(page_title):
    bookmarks = session.get('bookmarks', [])
    for page in bookmarks:
        if page['title'] == page_title:
            bookmarks.remove(page)
            session['bookmarks'] = bookmarks
            flash(f'Page "{page_title}" removed from bookmarks!', 'success')
            break
    return redirect(url_for('bookmarks'))

if __name__ == '__main__':
    app.run()