# Practical_Project - R6 Games Night 

## Contents 

## Intoduction
The object of the project was to create 'a service-orientated architecture for your application, this application must be composed of at least 4 services that work together'. 
These services include service 1 which is the front-end of the webpage, service 2 and 3 which are randomsizers and service 4 which take values from service 2 and 3 and creates a reponce depending on those values. This all needs to be presented to the user on service 1 using a database to store the infoamtion. 

### Requirements 
* A Trello board
* A detailed risk assessment. 
* 4 containerised services
* A working front-end website using Flask
* Integration into a Version Control System (Github) 
* Jenkins Testing and deployment
* Automation using Webhooks
* Docker swarm containing 1 manager and 2 workers 
* Automated installation using ansible  

### My Idea
My idea for the project was to create a program which would give you a random operator and strategie for the game random which seige as well as a points per kill you successful achieved using these parameters. This would mean you could complete with friends to see who would achieve the highest store in a given number of rounds.  

### User Stories
The first step was to create user stories to plan what was required, as well as getting a better perspective of the project.
* As a customer, I want to get a random operator, so I know which operator to play.
* As a customer, I want to get a random strat, so I know what I need to do.
* As a customer, I want to get a point value of each kill, so know how much is kill is worth in our points table. 

### My Plan 
* Create the front-end container
    * Creating the app.py 
    * Creating the docker file  
    * Creating the html file 
* Create the random operator container
    * Creating the app.py 
    * Creating the docker file  
* Create the random strategie container
    * Creating the app.py 
    * Creating the docker file  
* Create the points container
    * Creating the app.py 
    * Creating the docker file  
* Create a docker compose file 
* Create unit tests for all containers 
* Create Jenkins file to runs test via Jenkins
* Create docker images and push to docker hub
* Create ansible files to install docker on managers and workers as well as set them up 
* Deploy the site on the managers using xginx and a load balancer.

Database:

Nginx:

Ansible:

Docker:
### CI Pipeline 

### Project Tracking 

### Risk Assessment 

## Testing 

## Versions 

### Version 1

### Version 2

## Future Improvements 

## Author 