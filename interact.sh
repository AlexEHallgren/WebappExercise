docker exec -it $(docker ps | grep webapp-exercise | perl -l -ne '/^([0-9a-z]+)\ / && print $1') /bin/bash