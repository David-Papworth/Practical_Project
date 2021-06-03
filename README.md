# Practical_Project - R6 Games Night 

## Contents 
* [Introduction](#Intoduction)
    * [Requirements](#Requirements)
    * [My Idea](#My-Idea)
    * [User Stories](#User-Stories)
    * [My Plan](#My-Plan)
    * [CI Pipeline](#CI-Pipeline)
    * [Project Tracking ](#Project-Tracking )
    * [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [Versions](#Versions)
    * [Version 1](#Version-1)
    * [Version 2](#Version-2)
* [Future Improvements](#Future-Improvements)
* [Author](#Author)

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
I am using a Database linked to the front-end of the website so I can store previous cobinations and show the last 5. 

![Image showing the database used](https://i.imgur.com/KnRbJpR.png?1)

Nginx:
Nginx is being used as a load balancer for this project. A load balancer is 

Ansible:
Is being used to install packages onto the vm as well as set up the workers and managers 

Docker:
docker is used to containerise the 4 services. 
docker-compose is being used to create the images (docker-compose build) and push them (docker-compose push) to a reposortory (DockerHub).
docker swarm is utilised to manage and create a set of nodes (workers and manager).
docker stack is used to run the site.

### CI Pipeline 

The figure above shows the CI pipeline used for this project. Continuous Integration allows me to automate testing as well as deployment of the website. This increases the speed and precision of the project. In my method, when the code is pushed to Github, Jenkins will fetch and build the repository, it will then run unit tests as well as integration tests. This will then send a report to the developer informing them of the result.

### Project Tracking 
I used Trello for project tracking as it is free, light-wieght and easy to use. Below are a few images showing different stages of the sprint. The Trello board can be also found here:

### Risk Assessment 


## Testing 
```
#!/bin/bash

sudo apt update 
sudo apt install python3 python3-pip

pip3 install -r requirements.txt
pip3 install requests-mock
export DATABASE_URI
export SECRET_KEY

python3 -m pytest front-end --junitxml=junit/test-results.xml --cov=app --cov-report=xml --cov-report=html
python3 -m pytest operator_random --junitxml=junit/test-results1.xml --cov=app --cov-report=xml --cov-report=html
python3 -m pytest strat_random --junitxml=junit/test-results2.xml --cov=app --cov-report=xml --cov-report=html
python3 -m pytest points --junitxml=junit/test-results3.xml --cov=app --cov-report=xml --cov-report=html
```

```
class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://project_random_operator:5000/operator', json={"operator":'Ash', "difficulty":0})
            mocker.get('http://project_random_strat:5000/strat', json={"strat":'Train', "difficulty":20})
            mocker.post('http://project_points:5000/points', text='35')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Ash', response.data)
            self.assertIn(b'Train', response.data)
            self.assertIn(b'35', response.data)
```

```
class TestOpp(TestBase):
    def test_operator(self):
        for _ in range(20):
            response = self.client.get(url_for('operator'))
            self.assertEqual({'Sledge':0, 'Thatcher':10, 'Ash':0, 'Thermite':10, 'Montagne':20, 'Twitch':10, 'Blitz':10, 'Fuze':20, 'Glaz':20}[response.json["operator"]],response.json["difficulty"])
```

```
class TestHome(TestBase):
    def test_points(self):
        test_cases=[(0,0), (0,20), (0,40), (10,0), (10,20), (10,40), (20,0), (20,20), (20,40)]
        for ops,stra in test_cases:
            response = self.client.post(url_for('points'), json={"difficulty":ops, "difficulty_strat":stra})
            lower = 0 + ops + stra
            upper = 50 + ops + stra
            self.assertIn(int(response.data),range(lower,upper))
```

```
class TestHome(TestBase):
    def test_strat(self):
        for _ in range(20):
            response = self.client.get(url_for('strat'))
            self.assertEqual({'Primary Only':0, 'Secondary Only':20, 'Snail Mode':40, 'Train':20, 'Rush':0}[response.json["strat"]],response.json["difficulty"])
```

## Versions 

### Version 1

### Version 2

## Future Improvements 

## Author 
David Papworth