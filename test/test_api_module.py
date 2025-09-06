import pytest
import requests
from conf import base_url, HEADERS

@pytest.fixture
def session():
    return requests.Session()

def test_search_by_title(session): """Тест: поиск фильма по названию"""


response = session.get("{BASE_URL}/search/movies?page=1&limit=10&query=%D0%9C%D0%B0%D1%81%D1%82%D0%B5%D1%80, headers=HEADERS")
assert response.status_code == 200
data = response.json()
assert len(data["results"]) > 0
for movie in data["results"]:
    assert "Мастер и Маргарита" in movie["name"]


def test_search_by_year(session):
    """Тест: поиск фильмов по году выпуска"""


response = session.get("{BASE_URL}/search/movies?year=2021,headers=HEADERS")
assert response.status_code == 200
data = response.json()
assert len(data["results"]) > 0
for movie in data["results"]:
    assert movie["year"] == 2021


def test_search_by_rating(session):
    """Тест: поиск фильмов по рейтингу"""


response = session.get("{BASE_URL}/search/movies?rating.gte=8.5, headers=HEADERS")
assert response.status_code == 200
data = response.json()
assert len(data["results"]) > 0
for movie in data["results"]:
    assert float(movie["rating"]["kp"]) >= 8.5


def test_negative_search_result(session):
    """Негативный тест: фильм с несуществующим названием"""


response = session.get("{BASE_URL}/search/movies?q=nonexistent_movie_12345, headers=HEADERS")
assert response.status_code == 200
data = response.json()
assert len(data["results"]) == 0


def test_unauthorized_request(session):
    """Негативный тест: попытка сделать запрос без авторизации"""


response = session.get("{BASE_URL}/search/movies?page=1&limit=10&query=Мастер, headers={}")
assert (response.status_code == 401
        or response.status_code == 403)
