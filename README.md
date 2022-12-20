# Introduction

The goal of this project was to make a simple, yet effective e-commerce site for users to buy and sell products. I'll be outlining the steps I took, technology used and share unsolved problems and future state of this project in the following readme. At the current moment, this application more or less resemlbes that of a "window-shopping" app; as this application currently does not have any purchasing functioanlity, however those next steps will be discussed in the "unsolvoed problems/future features" section. 

## Approach Taken
Started out by thinking of a project that was relatively simple but required could be plussed to work quickly and efficiently. I decided on an e-commerce site because there were a lot of great examples out there to use. I named my project CongoB, as in Congo Basin, taking its name from a famous rainforest - similar to another famous site that has done the exact same thing.

After creating my user stories, I created my ERD which ended up being quite straight forward until later in my project’s development. After completing those two steps, I moved on to spinning up a quick wireframe for my web-app, again I wanted to focus on simplicity and reliability. 

After getting the basics needed for the applications routing and index and show pages, after meeting the technical requirements of the project, I started researching more complicated functionality to add to my project. One focus area consumed a majority of my time and I unfortunately was not able to complete the feature - that feature was cart and purchase functionality. I tried several different approaches and in two separate iterations, ended up nuking a lot of functionality in my application. This required me to roll back the project's progress a few times. Because of this misstep I was unable to solve two other problems that I’ve outlined below. My plan is to add these features soon after familiarizing myself with the new documentation I found that I believe would allow me to add these features. See below and attached documentation. 

### Unsolved Problems/Future Features
1. Search by category functionality (documentation: https://docs.djangoproject.com/en/4.1/topics/db/search/) 
2. Upload and store functionality (documentation: https://www.geeksforgeeks.org/python-uploading-images-in-django/) 
3. Chart and store functionality (documentation: https://www.geeksforgeeks.org/e-commerce-website-using-django/) - this one nuked my project and made me roll back a bunch of changes   

# Technologies Used
This web application was built using Django (V4.1.3), utilizing the built in user authentication functionality to, #1 allow users to authenticate and #2 protect certain routes in order to lock pages behind user specific ownership. The relational database used was Postgresql. And finally, Bootstrap was used to customize several index and show pages throughout the application. No additional libraries were used, but in future iterations I plan to use two separate libraries to manage photo uploads and payment processing (libraries are still to be determined, see documentation under “unsolved problems.”)

# Project Overview
### User Stories
1. As a user, I want the ability to search for all products and seach for products by category (index pages and search functionality)
2. As a user, I want the aiblity to sell products to the general community on this site 
3. As a user, I expect an ability to use a cart like feature where I can add multiple products then checkout and purchase
4. As a user, I'm hoping to see a minamilist design that works efficiently 

### Application Home Page  <br  />
![Alt text](e_commerce_app/static/images/home_screen.png?raw=true "Title")

### Wire Frame
![Alt text](e_commerce_app/static/images/wireframe.png?raw=true "Title")


### ERD 
![Alt text](e_commerce_app/static/images/erd.png?raw=true "ERD")

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/ijritchey/my_e_commerce.git
    $ cd `my_e_commerce`
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
Then simply apply the migrations:

    $ python manage.py migrate

Then create a `.env` folder at the project directory level and create a 'SECRET_KEY' variable. You'll need to ensure this secret key is being used within your project's `settings.py` file. To get this to work you may need to install the `python-dotenv` library. 
	$ pip(3) install python-dotenv

Within your `settings.py` file you’ll want to import the following from the dotenv library:
	`from dotenv import load_dotenv, dotenv_values`

You can now run the development server:

    $ python manage.py runserver
