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
    * [Code](#Code)
    * [Testing ](#Testing)
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
I am using a Database linked to the front-end of the website so I can store previous cobinations and show the last 5 sets of data made. 

![Image showing the database used](https://i.imgur.com/KnRbJpR.png?1)

Nginx:
Nginx is being used as a load balancer for this project. A load balancer is a system which decides where traffic show going depending on a set of parameters. This is normally done to reduces stress on a individul service and evenly distripute the load between the connected services.

Ansible:
Is being used to install packages onto the vm as well as set up the workers and managers. 

Docker:
docker is used to containerise the 4 services. 
docker-compose is being used to create the images (docker-compose build) and push them (docker-compose push) to a reposortory (DockerHub).
docker swarm is utilised to manage and create a set of nodes (workers and manager).
docker stack is used to run the site.
![Image showing service setup](https://i.imgur.com/JzEF2TH.png?1)

Th figure above shows the interaction between the services as well as the interaction with a database. As see in the figure get requests are sent to the operator random and strat random services and data is recieved. This data is then sent to the points service with a post request recieving the points per kill value these items are then stored in the database and shown on the front end so the user can see it.  
![Image showing swarm setup](https://i.imgur.com/pUfDcvw.png?1)

The figure above shows the set up for the docker swarm as well as engine x. This shows the user interacting with nginx which part of the swarm to send the request to. Requests are then sent between the nodes in the swarm to recieve the necessary data from the services. 

### CI Pipeline 
![Image showing CI pipeline](https://i.imgur.com/GgBqpfT.png?1)

The figure above shows the CI pipeline used for this project. Continuous Integration allows me to automate testing as well as deployment of the website. This increases the speed and precision of the project. In my method, when the code is pushed to Github, Jenkins will fetch and build the repository, it will then run unit tests. This will then send a report to the developer informing them of the result. If all the tests pass then the docker images will be pushed to docker hub. When the push is finished ansible is run to install packages and set up the swarm and nginx. Once this is done a docker stack compand is run which makes the website publicaly accessable. 

### Project Tracking 
I used Trello for project tracking as it is free, light-wieght and easy to use. Below are a few images showing different stages of the sprint. The Trello board can be also found here: https://trello.com/b/TCif27rc
![image showing project tracking start](https://i.imgur.com/nNyukRs.png?1)
![image showing end of sprint 1](https://i.imgur.com/iuq0wIv.png?2)
![image showing start of sprint 2](https://i.imgur.com/khwfKSZ.png?1)
![image showing end of sprint 2](https://i.imgur.com/3KxYdTe.png?1)


### Risk Assessment 
The risk assessment below shows all the risks involved with this project.
![image showing risk assessment](https://i.imgur.com/q7YKYD2.png?1)
All item highlighted in grey were risks added during the project sprint.

## Testing 
All test was run using pytest and Jenkins. Code 1 was used to run the unit tests in Jenkins (found as test.sh).
Code 1:
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
This was carried out to make sure all the webpages and if the services worked as intended. This was also used to run a coverage report. Coverage shows the number of lines the code reads though and ran to completion in pytest it doesn’t identify whether the code has given the intended output only that it had been run. We checked for the intended output by adding assertions to compare the output with a selected item (text, status code, etc).
The code below shows the unit test for the front-end it checks if the webpage works correct status code 200 and mocks the inputs of the other services to check if the data is show on the page. 

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
The code below shows the unit test for the random operator service and checks if the correct reponce is given. 
```
class TestOpp(TestBase):
    def test_operator(self):
        for _ in range(20):
            response = self.client.get(url_for('operator'))
            self.assertEqual({'Sledge':0, 'Thatcher':10, 'Ash':0, 'Thermite':10, 'Montagne':20, 'Twitch':10, 'Blitz':10, 'Fuze':20, 'Glaz':20}[response.json["operator"]],response.json["difficulty"])
```
The code below shows the unit test for the random strat service and checks if the correct reponce is given. 
```
class TestHome(TestBase):
    def test_strat(self):
        for _ in range(20):
            response = self.client.get(url_for('strat'))
            self.assertEqual({'Primary Only':0, 'Secondary Only':20, 'Snail Mode':40, 'Train':20, 'Rush':0}[response.json["strat"]],response.json["difficulty"])
```
The code below shows the unit test for points service where it checks for all inputs that the correct output is given.  
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
![coverage report](https://i.imgur.com/QII6RWN.png?1)
![front-end coverage report](https://i.imgur.com/RlyFAdF.png?1)
![random-operator coverage report](https://i.imgur.com/4zQkPgc.png?1)
![random-strat coverage report](https://i.imgur.com/18h8TJn.png?1)
![points coverage report](https://i.imgur.com/so72elB.png?1)

The figures above shows that I have 100% coverage over the sevices.
![image showing a completed run in jenkins](https://i.imgur.com/45evNm2.png?1)

The figure above shows a completed run in jenkins. 
## Versions 
One of the key items in the project to have a rolling update to the website. This was done creating a version 1 then making changes to all the services and running the docker stack deploy using the version 2 images. 
### Version 1
![webpage version 1](https://i.imgur.com/o5c8dlU.png?3)
The services in version 1:
* front end: shows infomation about operator, strat and points per kill plus the last 5 sets of data (show in the figure above)
* random operator: gets operator (Sledge, Thatcher, Ash, Thermite, Montagne, Twitch, Blitz, Fuze, Glaz) and their difficulity.
* random strat: gets strat (Primary Only, Secondary Only, Snail Mode, Train, Rush) and their difficulity.
* points per kill: uses the difficulity from the random services and gives a points per kill value.
### Version 2
![webpage version 2](https://i.imgur.com/IFT6t0v.png?1)
Changes in service 2 from service 1:
* front end: changes to view of the page show in figure above.
* random operator: added extra operators. 
* random strat: added extra strats.
* points per kill: changes the points values to be multiples of 5. 

## Future Improvements 
### Code
* A button could be implemented to refresh the page to get a new set of data rather then doing manually. 
* Add all the attack operators into the random operator picks.
* Adding a defence option so you can get a defender as well as attacker or one of them if you had a option button.
* Clean up code such as only having needed items in the requirements.txt. 
### Testing 
Integration tests coukd be used to test the pathway a user would use as well as stress test the system(e.g check if x button is pressed (x times) will the website break, how many user would it take to crash the site and if a button is pressed multiple times (quickly) will it give the correct response each time.)
## Author 
David Papworth