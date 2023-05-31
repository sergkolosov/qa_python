# qa_python
| Тест                                                                    | Описание                                                                          |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| 1. test_add_new_book_add_three_books_count                              | проверяем, что добавилось именно три книги и получение словаря с рейтингами книг  |
| 2. test_add_new_book_add_three_books_value                              | проверяем, что книга добавилась                                                   |
| 3. test_add_new_book_add_impossible_add_book_twice                      | нельзя добавить одну и ту же книгу дважды                                         |
| 4. test_set_book_rating_boundary_values                                 | проверяем добавление книге рейтингов с граничными значениями                      |
| 5. test_set_book_rating_impossible_set_rating_book_not_in_list          | нельзя выставить рейтинг книге, которой нет в списке                              |
| 6. test_set_book_rating_impossible_set_rating_book_less_than_one        | нельзя выставить рейтинг меньше 1                                                 |
| 7. test_set_book_rating_impossible_set_rating_book_more_than_ten        | нельзя выставить рейтинг больше 10                                                |
| 8. test_set_book_rating_book_that_was_not_added_has_no_rating           | у не добавленной книги нет рейтинга                                               |
| 9. test_get_books_with_specific_list_rating_five_count                  | проверяем количество книг с рейтингом 5                                           |                                           
| 10. test_get_books_with_specific_list_rating_five_value                 | проверяем список книг с рейтингом 5                                               |                                         
| 11. test_add_book_in_favorites_two_books_count                          | проверяем добавление в список избранных именно двух книг                          |
| 12. test_add_book_in_favorites_two_books_value                          | проверяем добавление в список избранных двух книг и получение списка избранных    |                        
| 13. test_add_book_in_favorites_cannot_add_book_is_not_in_the_dictionary | нельзя добавить книгу в избранное, если её нет в словаре books_rating             |
| 14. test_delete_book_from_favorites_one_book                            | проверяем что при удалении книги из списка избранных она пропадает из списка      |                     
| 15. test_delete_book_from_favorites_one_book_value                      | проверяем удаление книги из списка избранных и получение списка избранных         |                  
