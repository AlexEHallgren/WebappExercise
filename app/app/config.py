import environ
import enum


@environ.config(frozen=True)
class AppConfig:
    env = environ.var(default="dev")
    @environ.config(frozen=True)
    class Ghibli:
        films_url = environ.var(default="https://ghibliapi.herokuapp.com/films")
        people_url = environ.var(default="https://ghibliapi.herokuapp.com/people")
        film_data_cache_key = "film_data"
    ghibli = environ.group(Ghibli)


app_config = AppConfig.from_environ()
