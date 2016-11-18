from populate import base
from article.models import Book
import random
import datetime

def populate():
    print('Populating Article and Comment...', end='')
    titles = ['如何像電腦科學家一樣思考', '10 分鐘內學好 Python', '簡單學習 Django',
              '如何像電腦科學家一樣思考2', '10 分鐘內學好 Python2', '簡單學習 Django2',
              '如何像電腦科學家一樣思考3', '10 分鐘內學好 Python3', '簡單學習 Django3',
              '如何像電腦科學家一樣思考4', '10 分鐘內學好 Python4', '簡單學習 Django4']
    authors = ['張三','李四','王五','趙六']
    
    for title in titles:
        n = random.randint(0, len(authors)-1)
        book = Book()
        book.title = title
        book.author = authors[n]
        book.publisher = book.author
        book.pubDate = datetime.datetime.today()
        book.version = '1'
        book.price = 3000
        book.save()
    print('done')
    
    
if __name__ == '__main__':
    populate()