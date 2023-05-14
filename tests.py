import pytest

from main import BooksCollector


class TestBooksCollector:

    # навешиваем фикстуру с созданием экземпляра класса, для использования во всех тестах
    @pytest.fixture(autouse=True)
    def collector(self):
        # создаем экземпляр (объект) класса BooksCollector
        self.collector = BooksCollector()
        # определяем переменные для трех книг
        self.book_1 = 'Гордость и предубеждение и зомби'
        self.book_2 = 'Что делать, если ваш кот хочет вас убить'
        self.book_3 = 'Над пропастью во ржи'
        self.book_not_in_dictionary = 'Книга, которой нет в словаре'
        self.not_added_book = 'Не добавленная книга'
        # добавляем три книги
        self.collector.add_new_book(self.book_1)
        self.collector.add_new_book(self.book_2)
        self.collector.add_new_book(self.book_3)

        return self.collector

    # навешиваем фикстуру для тестов с избранными книгами
    @pytest.fixture()
    def favorites(self, collector):
        # добавляем в избранное две книги
        self.collector.add_book_in_favorites(self.book_1)
        self.collector.add_book_in_favorites(self.book_2)

        return self.collector.get_list_of_favorites_books()

    def test_add_new_book_add_three_books_count(self):
        # проверяем, что добавилось именно три книги и получение словаря с рейтингами книг
        assert len(self.collector.get_books_rating()) == 3

    def test_add_new_book_add_three_books_value(self):
        # проверяем, что добавились именно те книги и их исходный рейтинг
        assert self.collector.get_books_rating() == {self.book_1: 1, self.book_2: 1, self.book_3: 1}

    def test_add_new_book_add_impossible_add_book_twice(self):
        # Нельзя добавить одну и ту же книгу дважды (количество книг не меняется)
        self.collector.add_new_book(self.book_1)
        assert len(self.collector.get_books_rating()) == 3

    def test_set_book_rating_ten(self):
        # проверяем добавление книге рейтинга 10 (граничное значение) и получение рейтинга книги по названию
        self.collector.set_book_rating(self.book_1, 10)
        assert self.collector.get_books_rating()[self.book_1] == 10

    def test_set_book_rating_impossible_set_rating_book_not_in_list(self):
        # нельзя выставить рейтинг книге, которой нет в списке (её нет в словаре).
        self.collector.set_book_rating(self.book_not_in_dictionary, 5)
        assert not (self.book_not_in_dictionary in self.collector.get_books_rating())

    def test_set_book_rating_impossible_set_rating_book_less_than_one(self):
        # нельзя выставить рейтинг меньше 1
        self.collector.set_book_rating(self.book_1, 0)
        assert self.collector.get_books_rating()[self.book_1] != 0

    def test_set_book_rating_impossible_set_rating_book_more_than_ten(self):
        # нельзя выставить рейтинг больше 10
        self.collector.set_book_rating(self.book_1, 11)
        assert self.collector.get_books_rating()[self.book_1] != 11

    def test_set_book_rating_book_that_was_not_added_has_no_rating(self):
        # у не добавленной книги нет рейтинга (её нет в словаре).
        assert not (self.not_added_book in self.collector.get_books_rating())

    def test_get_books_with_specific_list_rating_five_count(self):
        # проверяем количество книг с рейтингом 5
        self.collector.set_book_rating(self.book_1, 5)
        self.collector.set_book_rating(self.book_2, 5)

        assert len(self.collector.get_books_with_specific_rating(5)) == 2

    def test_get_books_with_specific_list_rating_five_value(self):
        # проверяем список книг с рейтингом 5
        self.collector.set_book_rating(self.book_1, 5)
        self.collector.set_book_rating(self.book_2, 5)

        assert self.collector.get_books_with_specific_rating(5) == [self.book_1, self.book_2]

    def test_add_book_in_favorites_two_books_count(self, favorites):
        # проверяем добавление в список избранных именно двух книг
        assert len(self.collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_two_books_value(self, favorites):
        # проверяем добавление в список избранных двух книг и получение списка избранных
        assert self.collector.get_list_of_favorites_books() == [self.book_1, self.book_2]

    def test_add_book_in_favorites_cannot_add_book_is_not_in_the_dictionary(self):
        # нельзя добавить книгу в избранное, если её нет в словаре books_rating
        self.collector.add_book_in_favorites(self.book_not_in_dictionary)

        assert not (self.book_not_in_dictionary in self.collector.get_list_of_favorites_books())

    def test_delete_book_from_favorites_one_book_count(self, favorites):
        # проверяем что при удалении книги из списка избранных количество уменьшается на единицу
        quantity_before_deletion = len(self.collector.get_list_of_favorites_books())
        self.collector.delete_book_from_favorites(self.book_1)
        assert len(self.collector.get_list_of_favorites_books()) == quantity_before_deletion - 1

    def test_delete_book_from_favorites_one_book_value(self, favorites):
        # проверяем удаление книги из списка избранных и получение списка избранных
        self.collector.delete_book_from_favorites(self.book_1)
        assert self.collector.get_list_of_favorites_books() == [self.book_2]
