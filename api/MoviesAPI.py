import requests


class MoviesApi:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    def get_all_movies_by_org_id(self, org_id: str) -> dict:
        path = ("https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query=Мастер".
                format(kinopoisk=self.base_url, id=org_id))
        cookie = {"token": self.token}
        resp = requests.get(path, cookies=cookie)
        return resp.json()
