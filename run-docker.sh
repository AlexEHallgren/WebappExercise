# Build and run the project as a Docker container. Runs Django in Debug mode.
docker build . -t webapp-exercise
docker run -it -p 127.0.0.1:8000:8000 webapp-exercise