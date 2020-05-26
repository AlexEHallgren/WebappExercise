## Running the app

#### Running With Docker

To build and run the container execute these terminal commands:

```
docker build . -t webapp-exercise
docker run -it -p 127.0.0.1:8000:8000 webapp-exercise 
```

## Notes

* **Caching:** I used the in-memory cache provided by Django to simplify the exercise. This is not recommended for production and should be swapped out for something like Memcached. Depending on how critical the cached data is you could go further and have a separate caching layer hosted outside the server.
* **Configuration:** I used a library to pull some config data from environment variables, but I didn't do it for the config data that wasn't directly used for the exercise. In a real project all config data should be in the config file. The variables and secrets are provided during the CI/CD process.
* **Debug Mode:** I use the config data to determine whether to run in Debug mode, with True as default. To run the exercise in production mode, the environment variable `APP_ENV` should be set to `prd`. With Docker this can be done by adding the flag `-e APP_ENV=prd` to the `run` command.
* **Development Server:** This exercise is running on the Django development server. In a production environment this should be changed to something like NGINX.
* **Logging:** The logging of data is minimal in the exercise.
* **Error handling:** I let Django respond with its default error page.

