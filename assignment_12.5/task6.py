from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Movie:
    movie_id: str
    title: str
    genre: str
    rating: float
    release_year: int


def search_movie_by_id(movies: List[Movie], movie_id: str) -> Optional[Movie]:
    """Return the movie with the given movie_id, or None if not found."""
    for movie in movies:
        if movie.movie_id == movie_id:
            return movie
    return None


def sort_movies(movies: List[Movie], key: str) -> List[Movie]:
    """Return a new list of movies sorted by rating or release_year."""
    if key == 'rating':
        return sorted(movies, key=lambda movie: movie.rating, reverse=True)
    if key == 'release_year':
        return sorted(movies, key=lambda movie: movie.release_year)
    raise ValueError("Sort key must be 'rating' or 'release_year'")


if __name__ == '__main__':
    movies = [
        Movie('M001', 'Epoch', 'Sci-Fi', 8.9, 2024),
        Movie('M002', 'Aster', 'Drama', 7.4, 2021),
        Movie('M003', 'Pulse', 'Thriller', 9.2, 2025),
        Movie('M004', 'Luna', 'Fantasy', 8.0, 2023),
    ]

    print('Search movie M003:')
    print(search_movie_by_id(movies, 'M003'))

    print('\nSort by rating:')
    for movie in sort_movies(movies, 'rating'):
        print(movie)

    print('\nSort by release_year:')
    for movie in sort_movies(movies, 'release_year'):
        print(movie)
