#!/bin/bash

docker service create --name front_end davidpapworth2/project_front_end
docker service create --name points davidpapworth2/project_points
docker service create --name random_strat davidpapworth2/project_random_strat
docker service create --name random_operator davidpapworth2/project_random_operator
docker service create --name nginx --publish 80:80 nginx:latest