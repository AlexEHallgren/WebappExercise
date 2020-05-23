docker build . -t webapp-exercise
docker run -it webapp-exercise --mount type=bind,source="$(pwd)",target=/app