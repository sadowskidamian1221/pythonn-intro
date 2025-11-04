# Damian Sadowski


import unittest
import app

class TestApp(unittest.TestCase):
    # Testy funkcji is_valid_email

    def test_is_valid_email_typical(self):                #Sprawdza poprawny adres email z '@' oraz domeną
        self.assertTrue(app.is_valid_email("test@example.com"))

    def test_is_valid_email_wrong_format(self):           #Sprawdza błędny format adresu email (brak '@')
        self.assertFalse(app.is_valid_email("test.example.com"))

    def test_is_valid_email_empty(self):                  #Sprawdza pusty ciąg znaków (niepoprawny adres email)
        self.assertFalse(app.is_valid_email(""))

    # Testy funkcji rectangle_area

    def test_rectangle_area_typical(self):                 #Sprawdza prawidłowe wyliczenie pola prostokąta 3x4
        self.assertEqual(app.rectangle_area(3, 4), 12)

    def test_rectangle_area_zero(self):                    #Sprawdza pole prostokąta gdy jeden z wymiarów to 0
        self.assertEqual(app.rectangle_area(0, 5), 0)

    def test_rectangle_area_negative(self):                #Sprawdza zachowanie funkcji przy ujemnym wymiarze
        self.assertEqual(app.rectangle_area(-2, 5), 0)

    # Testy funkcji filter_positive

    def test_filter_positive_typical(self):                #Filtruje liczby dodatnie z mieszanej listy
        self.assertEqual(app.filter_positive([1, -2, 3, 0, 5, -1]), [1, 3, 5])

    def test_filter_positive_all_negative(self):           #Zwraca pustą listę gdy wejście to same liczby ujemne i 0
        self.assertEqual(app.filter_positive([-3, -1, -7, 0]), [])

    def test_filter_positive_empty(self):                  #Zwraca pustą listę dla pustej listy wejściowej
        self.assertEqual(app.filter_positive([]), [])

    # Testy funkcji parse_date

    def test_parse_date_standard(self):                    #Parsuje poprawną datę w formacie dd-mm-yyyy i sprawdza rok                 
        self.assertEqual(app.parse_date("01-12-2020").year, 2020)

    def test_parse_date_wrong_format(self):                #Sprawdza błąd parsowania dla niepoprawnego formatu daty
        with self.assertRaises(ValueError):
            app.parse_date("2020/12/01")

    def test_parse_date_empty(self):                        #Sprawdza błąd parsowania dla pustego ciągu znaków
        with self.assertRaises(ValueError):
            app.parse_date("")

    # Testy funkcji is_palindrome

    def test_is_palindrome_typical(self):                   #Sprawdza wyraz będący palindromem.
        self.assertTrue(app.is_palindrome("kajak"))

    def test_is_palindrome_not_palindrome(self):            #Sprawdza wyraz niebędący palindromem.

        self.assertFalse(app.is_palindrome("python"))

    def test_is_palindrome_empty(self):                     #Sprawdza zachowanie funkcji dla pustego ciągu znaków (palindrom).
 
        self.assertTrue(app.is_palindrome(""))

if __name__ == '__main__':
    unittest.main()
