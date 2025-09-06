import requests


class RatingAPI:
    def __init__(self, base_url, auth_token=None):
        """
        Инициализирует API с базовым URL и токеном авторизации (если необходимо).

        :param base_url: базовый URL API
        :param auth_token: токен авторизации (опционально)
        """
        self.base_url = base_url
        self.auth_token = auth_token
        self.headers = {'Authorization': f'Token {auth_token}'} if auth_token else None

    def get_average_rating(self, content_id):
        """
        Получает средний рейтинг контента по его идентификатору.

        :param content_id: уникальный идентификатор контента
        :return: среднее значение рейтинга
        """
        url = f"{self.base_url}/content/{content_id}/average-rating/"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()['average']
        else:
            return None

    def get_reviews(self, content_id):
        """
        Получает список отзывов по данному контенту.

        :param content_id: уникальный идентификатор контента
        :return: список отзывов
        """
        url = f"{self.base_url}/content/{content_id}/reviews/"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()['reviews']
        else:
            return []

    def send_review(self, content_id, rating, comment=''):
        """
        Отправляет отзыв и оценку контента.

        :param content_id: уникальный идентификатор контента
        :param rating: оценка (число)
        :param comment: необязательный комментарий к оценке
        :return: True, если отзыв отправлен успешно, False в противном случае
        """
        url = f"{self.base_url}/content/{content_id}/send-review/"
        payload = {'rating': rating, 'comment': comment}
        response = requests.post(url, json=payload, headers=self.headers)
        return response.status_code == 201


# Пример использования класса:
if __name__ == '__main__':
    api = RatingAPI('https://example-rating-service.com', auth_token='YOUR_AUTH_TOKEN_HERE')

    average_rating = api.get_average_rating(content_id=79429)
    reviews = api.get_reviews(content_id=79429)

    sent_successfully = api.send_review(content_id=79429, rating=5, comment='Отличный фильм!')