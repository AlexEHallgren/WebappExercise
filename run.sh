docker build . -t webapp-exercise
docker run -it -p 127.0.0.1:8000:8000 webapp-exercise