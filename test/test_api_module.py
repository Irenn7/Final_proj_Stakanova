import pytest
import requests
from conf import base_url, HEADERS

def test_search_by_title():
    """Тест: поиск фильма по названию"""
    response = requests.get(f"{base_url}movie/search?page=1&limit=10&query=intouchables", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data.get("docs", {})[0].get('name') == "1+1"

def test_search_by_year():
    """Тест: поиск фильмов по году выпуска"""
    response = requests.get(f"{base_url}movie/search/movies?year=2021",headers=HEADERS)
    assert response.status_code == 200


def test_search_by_rating():
    """Тест: поиск фильмов по рейтингу"""
    response = requests.get(f"{base_url}movie/search/movies?rating.gte=8.5", headers=HEADERS)
    assert response.status_code == 200


def test_negative_search_result():
    """Негативный тест: фильм с несуществующим названием"""
    response = requests.get(f"{base_url}movie/search/movies?q=nonexistent_movie_^&%", headers=HEADERS)
    assert response.status_code == 200


def test_unauthorized_request():
    """Негативный тест: попытка сделать запрос без авторизации"""
    response = requests.get(f"{base_url}movie/search/movies?page=1&limit=10&query=Мастер")
    assert (response.status_code == 401
        or response.status_code == 403)

