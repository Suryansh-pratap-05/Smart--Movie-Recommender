from src.recommender import MovieRecommender, get_recommendations


def test_recommender_returns_requested_count():
    recommender = MovieRecommender()
    matched, recommendations = recommender.get_recommendations("Inception", top_n=5)

    assert matched == "Inception"
    assert len(recommendations) == 5
    assert all(movie.title != "Inception" for movie in recommendations)


def test_recommender_handles_close_title_match():
    recommender = MovieRecommender()
    matched, recommendations = recommender.get_recommendations("Interstelar", top_n=3)

    assert matched == "Interstellar"
    assert len(recommendations) == 3


def test_guideline_helper_returns_titles():
    titles = get_recommendations("The Matrix", top_n=4)

    assert len(titles) == 4
    assert all(isinstance(title, str) for title in titles)
