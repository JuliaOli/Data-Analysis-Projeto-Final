# Data-Analysis Class Final Project: Web Application 
### Following the Tutorial

This repository is a reproduction of a tutorial that meant to demonstrate the use of Flask and Angular to build a simple,web application which can be used for POCs. Read the corresponding Medium article [here](https://medium.com/@dvelsner/deploying-a-simple-machine-learning-model-in-a-modern-web-application-flask-angular-docker-a657db075280).

## Clone/Fork repository

First fork or clone this repo:

e.g. `git clone https://github.com/delsner/flask-angular-data-science.git`
 

## Build images and run containers with docker-compose

After cloning the repository go inside the project folder:

`cd Data-Analysis-Projeto-Final`

Run `docker-compose up` which will start a Flask web application for the backend API (default port `8081`) and an Angular frontend served through a webpack development web server (default port `4200`).


## Access your app

In your browser navigate to: `http://localhost:4200` (or whatever port you defined for the frontend in `docker-compose.yml`).

For testing your backend API I recommend using [Postman](https://www.getpostman.com/).
  
## KNN (K Nearest Neighbors) and implementation on Iris data set
This project was build using K Nearest Neighbors wilhe the original project was build using a SVM. The model seems to present a overfitting, and need some adjustments to the fitting part.

The theorical part was from this article: [K Nearest Neighbors and implementation on Iris data set](https://medium.com/@avulurivenkatasaireddy/k-nearest-neighbors-and-implementation-on-iris-data-set-f5817dd33711).
