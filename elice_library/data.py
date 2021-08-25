# book_name, publisher, author, publication_date, pages, isbn, description, link(img_url)
import csv
import datetime
from app import create_app, db
from models import Book

app = create_app()
app.app_context().push()


def push_data():
    if Book.query.first() is None:
        with app.app_context():
            with open('library.csv', 'r', encoding='UTF-8') as data:
                reader = csv.DictReader(data)
                for lines in reader:
                    id = lines['id']
                    img_url = f"images/{id}"
                    try:
                        # png로 열리면 img_url 은 ".png"
                        open(f"static/images/{id}.png")
                        img_url += ".png"
                    except:
                        img_url += ".jpg"

                    # print(img_url)
                    # print(lines['book_name'])

                    publication_date = datetime.datetime.strptime(
                        lines['publication_date'], '%Y-%m-%d')
                    book = Book(book_name=lines['book_name'], publisher=lines['publisher'], author=lines['author'], publicated_at=publication_date, pages=int(
                        lines['pages']), img_url=img_url, isbn=int(lines['isbn']), description=lines['description'], link=lines['link'], stock=10, rating=0)
                    db.session.add(book)
                    db.session.commit()
                db.create_all(app=app)


push_data()
