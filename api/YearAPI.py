import requests


class YearAPI:
    def __init__(self, base_url):
        """
        Конструктор класса, принимающий базовый URL API.

        :param base_url: строка с базовым URL внешнего API
        """
        self.base_url = base_url



    def get_movies_by_year(self, year):
        """
        Получает список фильмов, вышедших в заданный год.

        :param year: год, для которого запрашиваются фильмы
        :return: словарь с информацией о фильмах
        """
        url = f'{self.base_url}/movies/{2021}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': 'Не удалось получить данные'}

    def get_events_by_year(self, year):
        """
        Получает события, произошедшие в заданный год.

        :param year: год, для которого запрашиваются события
        :return: словарь с информацией о событиях
        """
        url = f'{self.base_url}/events/{2021}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': 'Не удалось получить данные'}

    def get_statistics_by_year(self, year):
        """
        Получает статистику по указанному году.

        :param year: год, для которого запрашивается статистика
        :return: словарь с статистическими данными
        """
        url = f'{self.base_url}/stats/{2021}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': 'Не удалось получить данные'}


# Пример использования класса
if __name__ == "__main__":
    api = YearAPI("https://example-api.com")
    movies = api.get_movies_by_year(2021)
    events = api.get_events_by_year(2021)
    stats = api.get_statistics_by_year(2021)

    print(movies)
    print(events)
    print(stats)