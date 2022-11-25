# Supermarket

This is a Django Supermarket application 

## Domain case

In this case, a supermarket chain is requesting a system for managing cashiers and their shifts, branches, checkouts, articles and their stock.

## Objective

The supermarket's objective is to provide its services to sell supermarket products. 

### Our solution

Our solution proposes to develope a Django server that displays an web page, which through a user registry allows cashiers to register sales and print tickets. It also offers the best-selling products and offers of the moment, available to all customers.

### Installing

Clone the project to a folder: 

```bash
git clone https://github.com/Franco-Ball/ProyectoIntegradorSupermarket.git
```
create a virtual environment with the following command:

```bash
virtualenv 'name'
```
once in the virtual environment, type the command:

```bash
pip install requirements.txt
```
thus installing all the necessary libraries to run the project.

## Using the system

To run the server you must redirect to the folder where the 'manage.py' archive is located, then use the command: 

```bash
./manage.py runserver
```
therefore you must enter the following address ```http://127.0.0.1:8000/```. 
Having already entered the indicated address, cashiers can log in and enter the section to start registering sales.

## Authors

  - Franco Ball
  - Santiago Carranza
  - Franco Morales 

## Collaborators

  - Requirements elicitation: Teodoro Reyna 
  - Technical leader: Nicolas Ledesma
