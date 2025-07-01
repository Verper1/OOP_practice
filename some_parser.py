import requests
from bs4 import BeautifulSoup


class Parser_USD_and_EUR:
    def __init__(self):
        self.src = None
        self.usd_eur_to_rub = None
        self.numbers = None
        
        self.get_html_page()
        self.get_all_tags()
        self.get_numbers()
        self.print_nums()

    def get_html_page(self):
        st_accept = "text/html"  # говорим веб-серверу, что хотим получить html имитируем подключение через браузер Mozilla на macOS
        st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
        # формируем хеш заголовков
        headers = {
           "Accept": st_accept,
           "User-Agent": st_useragent
        }

        # отправляем запрос с заголовками по нужному адресу
        req = requests.get("https://www.vbr.ru/banki/kurs-valut/cbrf/", headers)
        # считываем текст HTML-документа
        self.src = req.text

    def get_all_tags(self):
        # инициализируем html-код страницы
        soup = BeautifulSoup(self.src, features="html.parser")
        # считываем заголовок страницы
        self.usd_eur_to_rub = soup.find_all('td', class_='rates-val rates-val-inline')
        return self.usd_eur_to_rub

    def get_numbers(self):
        # Список для хранения чисел
        self.numbers = []

        for tag in self.usd_eur_to_rub:
            # Извлекаем текст из тега
            text = tag.get_text(strip=True)  # Получаем текст и убираем лишние пробелы
            number_str = text.split(' ')[0].replace(',', '.')  # Берем только число и заменяем запятую на точку
            number = float(number_str)  # Преобразуем в float
            self.numbers.append(number)
        return self.numbers

    def print_nums(self):
        print(f'Рубль к доллару: {self.numbers[1]}\nРубль к евро: {self.numbers[3]}')


parser1 = Parser_USD_and_EUR()
