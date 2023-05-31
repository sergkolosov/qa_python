import pytest

from main import BooksCollector


class TestBooksCollector:

    """Навешиваем фикстуру с созданием экземпляра класса, для использования во всех тестах."""
    @pytest.fixture(autouse=True)
    def collector(self):
        """
        Создаем экземпляр (объект) класса BooksCollector
        Определяем переменные для трех книг
        Добавляем три книги
        """
        self.collector = BooksCollector()

        self.book_1 = 'Гордость и предубеждение и зомби'
        self.book_2 = 'Что делать, если ваш кот хочет вас убить'
        self.book_3 = 'Над пропастью во ржи'
        self.book_not_in_dictionary = 'Книга, которой нет в словаре'
        self.not_added_book = 'Не добавленная книга'

        self.collector.add_new_book(self.book_1)
        self.collector.add_new_book(self.book_2)
        self.collector.add_new_book(self.book_3)

        return self.collector


    @pytest.fixture()
    def favorites(self, collector):
        """
        Навешиваем фикстуру для тестов с избранными книгами
        Добавляем в избранное две книги
        """
        self.collector.add_book_in_favorites(self.book_1)
        self.collector.add_book_in_favorites(self.book_2)

        return self.collector.get_list_of_favorites_books()

    def test_add_new_book_add_three_books_count(self):
        """Проверяем, что добавилось именно три книги и получение словаря с рейтингами книг"""
        assert len(self.collector.get_books_rating()) == 3

    def test_add_new_book_add_three_books_value(self):
        """Проверяем, что книга добавилась"""
        assert self.book_1 in self.collector.get_books_rating()

    def test_add_new_book_add_impossible_add_book_twice(self):
        """Нельзя добавить одну и ту же книгу дважды"""
        self.collector.add_new_book(self.book_1)
        assert len(self.collector.get_books_rating()) == 3

    @pytest.mark.parametrize('boundary_values', [1, 2, 9, 10])
    def test_set_book_rating_boundary_values(self, boundary_values):
        """Проверяем добавление книге рейтингов с граничными значениями"""
        self.collector.set_book_rating(self.book_1, boundary_values)
        assert self.collector.get_book_rating(self.book_1) == boundary_values

    def test_set_book_rating_impossible_set_rating_book_not_in_list(self):
        """Проверяем, что нельзя выставить рейтинг книге, которой нет в списке."""
        self.collector.set_book_rating(self.book_not_in_dictionary, 5)
        assert self.collector.get_book_rating(self.not_added_book) is None

    def test_set_book_rating_impossible_set_rating_book_less_than_one(self):
        """Проверяем, что нельзя выставить рейтинг меньше 1"""
        self.collector.set_book_rating(self.book_1, 0)
        assert self.collector.get_book_rating(self.book_1) == 1

    def test_set_book_rating_impossible_set_rating_book_more_than_ten(self):
        """Проверяем, что нельзя выставить рейтинг больше 10"""
        self.collector.set_book_rating(self.book_1, 11)
        assert self.collector.get_book_rating(self.book_1) == 1

    def test_set_book_rating_book_that_was_not_added_has_no_rating(self):
        """Проверяем, что у не добавленной книги нет рейтинга"""
        assert self.collector.get_book_rating(self.not_added_book) is None

    def test_get_books_with_specific_list_rating_five_count(self):
        """Проверяем количество книг с рейтингом 5"""
        self.collector.set_book_rating(self.book_1, 5)
        self.collector.set_book_rating(self.book_2, 5)

        assert len(self.collector.get_books_with_specific_rating(5)) == 2

    def test_get_books_with_specific_list_rating_five_value(self):
        """Проверяем список книг с рейтингом 5"""
        self.collector.set_book_rating(self.book_1, 5)
        self.collector.set_book_rating(self.book_2, 5)

        assert self.collector.get_books_with_specific_rating(5) == [self.book_1, self.book_2]

    def test_add_book_in_favorites_two_books_count(self, favorites):
        """Проверяем добавление в список избранных именно двух книг"""
        assert len(self.collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_two_books_value(self, favorites):
        """Проверяем добавление в список избранных двух книг и получение списка избранных"""
        assert self.collector.get_list_of_favorites_books() == [self.book_1, self.book_2]

    def test_add_book_in_favorites_cannot_add_book_is_not_in_the_dictionary(self):
        """Проверяем, что нельзя добавить книгу в избранное, если её нет в словаре books_rating"""
        self.collector.add_book_in_favorites(self.book_not_in_dictionary)
        assert self.book_not_in_dictionary not in self.collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_one_book(self, favorites):
        """Проверяем что при удалении книги из списка избранных она пропадает из списка"""
        self.collector.delete_book_from_favorites(self.book_1)
        assert self.book_1 not in self.collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_one_book_value(self, favorites):
        """Проверяем удаление книги из списка избранных и получение списка избранных"""
        self.collector.delete_book_from_favorites(self.book_1)
        assert self.collector.get_list_of_favorites_books() == [self.book_2]

