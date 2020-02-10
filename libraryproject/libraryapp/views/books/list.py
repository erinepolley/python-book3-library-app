import sqlite3
from libraryapp.models import Book
from libraryapp.models import model_factory
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from ..connection import Connection
from django.contrib.auth.decorators import login_required

# from views import Connection
# from views.connection import Connection

@login_required
def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Book)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn,
                b.author,
                b.year,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)

            all_books = db_cursor.fetchall()

            # for row in dataset:
            #     book = Book()
            #     book.id = row['id']
            #     book.title = row['title']
            #     book.isbn = row['isbn']
            #     book.author = row['author']
            #     book.year = row['year']
            #     book.librarian_id = row['librarian_id']
            #     book.location_id = row['location_id']

            #     all_books.append(book)
#all books is the list of books objects that the view generates.
        template = 'books/list.html'
        #can call the all_books on the left whatever you want.
        #all_books on the right needs to be the same as in the template. Our template is expecting a dictionary as all_books. So it needs to match and be a dictionary.
        context = {
            'all_books': all_books
        }
#request, template, and context are naming conventions.
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_book
            (
                title, author, isbn,
                year, location_id, librarian_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
#The values thing above is quality control, protection from bad data injection.
            (form_data['title'], form_data['author'],
                form_data['isbn'], form_data['year_published'],
                request.user.librarian.id, form_data["location"]))

        return redirect(reverse('libraryapp:books'))