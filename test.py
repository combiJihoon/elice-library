# book_name, publisher, author, publication_date, pages, isbn, description, link(img_url)
import csv
import datetime


def push_data():
    with open('./library.csv', 'r', encoding='UTF-8') as data:
        reader = csv.DictReader(data)
        for lines in reader:
            id = lines['id']
            img_url = f"./static/images/{id}"
            try:
                # png로 열리면 img_url 은 ".png"
                open(f"./static/images/{id}.png")
                img_url += ".png"
            except:
                img_url += ".jpg"

            print(img_url)
            # print(lines['book_name'])


push_data()
