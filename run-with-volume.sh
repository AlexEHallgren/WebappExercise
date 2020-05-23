docker build . -t webapp-exercise
docker run \
    -it \
    --mount type=bind,source="$(pwd)",target=/exercise \
    -p 127.0.0.1:8000:8000 \
    webapp-exercise