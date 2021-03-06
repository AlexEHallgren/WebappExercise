You can run this exercise with Docker or use virtualenv to set it up.

#### Running With Docker

To build and run the project as a Docker container execute these terminal commands:

```
docker build . -t webapp-exercise
docker run -it -p 127.0.0.1:8000:8000 webapp-exercise 
```

Or by using the convenience shell script `run-docker.sh`.

#### Running with virtualenv

The project is built using python `3.8.0`. After setting up the virtualenv and installing requirements, start the Django server by running the following command in the top directory:

```
python app/manage.py runserver 127.0.0.1:8000
```

## Notes

* **Caching:** I used the in-memory cache provided by Django to simplify the exercise. This is not recommended for production and should be swapped out for something like Memcached. Depending on how critical the cached data is you could go further and have a separate caching layer hosted outside the server.
* **Configuration:** I used a library to pull some config data from environment variables, but I didn't do it for the config data that wasn't directly used for the exercise. In a real project all config data should be in the config file. The variables and secrets are provided during the CI/CD process.
* **Debug Mode:** I use the config data to determine whether to run in Debug mode, with True as default. To run the exercise in production mode, the environment variable `APP_ENV` should be set to `prd`. With Docker this can be done by adding the flag `-e APP_ENV=prd` to the `run` command.
* **Development Server:** This exercise is running on the Django development server. In a production environment this should be changed to something like NGINX.
* **Logging:** The logging of data is minimal in the exercise. Ideally things like HTTP requests and errors would be logged to a standard location and then exported to some logging DB.
* **Error handling:** I let Django respond with its default error page. This could be improved by a nicer error page, or displaying older cached data with a warning that it is stale.

The files inside the top `app` directory are mostly autogenerated by Django. The ones I worked on are:

```
app/
    app/
        config.py
        settings.py
        urls.py
    ghibli/
        models.py
        urls.py
        utility.py
        views.py
        tests/
            test_models.py
            test_views.py
        templates/
            ghibli/
                film_list.html    
```
