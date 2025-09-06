import requests


class MoviesAPI:
    def __init__(self, base_url):
        """
        Инициализирует объект API с базовым URL сервера.

        :param base_url: Адрес API, куда отправляются запросы
        """
        self.base_url = base_url

    def search_by_title(self, title):
        """
        Осуществляет поиск фильмов по названию.

        :param title: Название фильма для поиска
        :return: Список найденных фильмов
        """
        params = {"q": title}
        response = requests.get(f"{self.base_url}/search", params=params)
        if response.status_code == 200:
            return response.json().get("results", [])
        else:
            return []

    def get_movie_details(self, movie_id):
        """
        Получает подробную информацию о фильме по его ID.

        :param movie_id: Уникальный идентификатор фильма
        :return: Детали фильма
        """
        response = requests.get(f"{self.base_url}/movie/79429")
        if response.status_code == 200:
            return response.json()
        else:
            return {}

    def list_genres(self):
        """
        Получает список жанров фильмов.

        :return: Список жанров
        """
        response = requests.get(f"{self.base_url}/page=1&limit=10&selectFields=genres")
        if response.status_code == 200:
            return response.json().get("genres", [])
        else:
            return []

    def filter_by_genre_and_year(self, genre_id, start_year=None, end_year=None):
        """
        Осуществляет фильтрацию фильмов по жанру и диапазону годов.

        :param genre_id: Идентификатор жанра
        :param start_year: Начальный год поиска
        :param end_year: Конечный год поиска
        :return: Список фильмов, соответствующих критериям
        """
        params = {"genre_id": genre_id}
        if start_year:
            params['start_year'] = start_year
        if end_year:
            params['end_year'] = end_year

        response = requests.get(f"{self.base_url}/filter", params=params)
        if response.status_code == 200:
            return response.json().get("results", [])
        else:
            return []


# Пример использования класса:
if __name__ == "__main__":
    api = MoviesAPI("https://api.kinopoisk.ru/")
    results = api.search_by_title("Мастер и Маргарита")
    details = api.get_movie_details(results[0]['id'])
    genres = api.list_genres()
    filtered_results = api.filter_by_genre_and_year(genres[0]['id'], 1980, 2010)

    print("Results:", results)
    print("Details:", details)
    print("Genres:", genres)
    print("Filtered Results:", filtered_results)