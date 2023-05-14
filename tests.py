import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def collector(self):
        # создаем экземпляр (объект) класса BooksCollector
        self.collector = BooksCollector()
        # # добавляем две книги
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        self.collector.add_new_book('Над пропастью во ржи')

        return self.collector

    def test_add_new_book_add_two_books(self):
        # проверяем, что добавилось именно три книги
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 3
        assert len(self.collector.get_books_rating()) == 3
