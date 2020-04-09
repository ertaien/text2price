import unittest

from app import parser_amount


class TextAmountParser(unittest.TestCase):

    def test_amount_tg(self):
        self.assertEqual(parser_amount("Cатамын, 150000 тг"), 150000)
        self.assertEqual(parser_amount("Cатамын, 4567 тг"), 4567)
        self.assertEqual(parser_amount("Cатамын, 1 354 99 тг"), 135499)
        self.assertEqual(parser_amount("Cатамын, 1 500 000 тг"), 1500000)
        self.assertEqual(parser_amount("Cатамын, 1 450 000 тг"), 1450000)
        self.assertEqual(parser_amount("Бағасы 3 200 000 тг."), 3200000)

    def test_amount_tenge(self):
        self.assertEqual(parser_amount("Cатамын, 500 теңге"), 500)
        self.assertEqual(parser_amount("Cатамын, 1500 теңге"), 1500)
        self.assertEqual(parser_amount("Cатамын, 3500 теңге"), 3500)

    def test_amount_tenge2(self):
        self.assertEqual(parser_amount("Cатамын, 500 тенге"), 500)
        self.assertEqual(parser_amount("Cатамын, 1500 тенге"), 1500)
        self.assertEqual(parser_amount("Cатамын, 3500 тенге"), 3500)

    def test_amount_lower_case(self):
        self.assertEqual(parser_amount("Cатамын, 500 ТЕНГЕ"), 500)
        self.assertEqual(parser_amount("Cатамын, 1500 ТГ"), 1500)

    def test_amount_symbols_number(self):
        self.assertEqual(parser_amount("Комбинезон және шапка, куртка - 10,000 тг."), 10000)
        self.assertEqual(parser_amount("Комбинезон және 234 шапка, куртка - 10.00.0 тг."), 10000)
        self.assertEqual(parser_amount("Комбинезон және 342 шапка, куртка - 10.00.0 тг."), 10000)
        self.assertEqual(parser_amount("Комбинезон және 345 шапка, куртка - 100.0.0 тг."), 10000)

    def test_amount_none(self):
        self.assertIsNone(parser_amount("Жылқы сатылады. ға берем."))
        self.assertIsNone(parser_amount("Жылқы сатылады. 300 000 ға берем."))

    def test_amount_mln(self):
        self.assertEqual(parser_amount("Комбинезон және шапка, куртка - 1 млн ға берем тг."), 1000000)
        self.assertEqual(parser_amount("Комбинезон және шапка, куртка - 99 миллионға ға берем тг."), 99000000)
        self.assertEqual(parser_amount("Комбинезон және шапка, куртка - 25 миллионға ға берем тг."), 25000000)
        self.assertEqual(parser_amount("Комбинезон және шапка, куртка - 350 миллионға ға берем тг."), 350000000)

    def test_amount_tis(self):
        self.assertEqual(parser_amount("Комбинезон және шапка, куртка - 30 мың ға берем"), 30000)
        self.assertEqual(parser_amount("Комбинезон және шапка, куртка - 99 мың ға берем"), 99000)
        self.assertEqual(parser_amount("Комбинезон және шапка, куртка - 25 мын ға берем"), 25000)
        self.assertEqual(parser_amount("Комбинезон және шапка, куртка - 25 тыс ға берем"), 25000)
        self.assertEqual(parser_amount("Комбинезон және шапка, куртка - 25 мыңға ға берем"), 25000)


if __name__ == "__main__":
    unittest.main()
