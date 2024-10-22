# Suomenlinna-Traffic-Predictor

Project for the Introduction to Data Science (5cr) course at University of Helsinki. <br/>
Authors: Chris Netto, Jing Cheng, Gabriela Kakol.

## Structure

This repository contains the following sections:

1. data - contains all the data used in the project, including weather data and Suomenlinna HSL ferry data. Also
   includes finalized data used in the machine learning model, as well as the predictions made by the model.
2. src - contains the code for the machine learning model and its predictions, as well as the code for the
   creation of the map for our website.
3. The code for application
4. The final HSL Suomenlinna planner report

## Instalation of the Program

Run the following commands in `~/Suomenlinna-Traffic-Predictor`

1. Install dependencies with the command:

```
poetry install
```

2. Initialize the project with the command:

```
poetry run invoke build
```

3. Start the program with the command:

```
poetry run invoke start
```
