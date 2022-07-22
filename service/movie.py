from typing import Dict, Any, List

from dao.model.movie import Movie

from dao.movie import MovieDAO


class MovieService:
    dao: MovieDAO

    def __init__(self, dao: MovieDAO) -> None:
        self.dao = dao

    def get_one(self, mid: int) -> Movie:
        return self.dao.get_one(mid)

    def get_all(self, filters: Dict[str, Any]) -> List[Movie]:
        if filters.get("director_id") is not None:
            return self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            return self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            return self.dao.get_by_year(filters.get("year"))
        else:
            return self.dao.get_all()

    def create(self, movie_d: Dict[str, Any]) -> Movie:
        movie: Movie = Movie(**movie_d)
        return self.dao.create(movie)

    def update(self, movie_id: int, movie_d: Dict[str, Any]):
        movie_by_id: Movie = self.dao.get_one(movie_id)
        for k, v in movie_d.items():
            setattr(movie_by_id, k, v)
        return self.dao.update(movie_by_id)

    def delete(self, mid: int) -> None:
        self.dao.delete(mid)
