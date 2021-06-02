#!/bin/bash

scp docker-compose.yaml project-swarm-manager:
ssh project-swarm-manager << EOF 
export DATABASE_URI=${DATABASE_URI}
docker stack deploy --compose-file docker-compose.yaml project 
EOF