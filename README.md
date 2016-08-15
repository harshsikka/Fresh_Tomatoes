# Fresh Tomatoes!
Fresh Tomatoes is a simple website that displays a given list of movies. Visitors to the <br>
site can click any of the given movies and their trailer will popup and begin playing. This <br>
site was completed as part of the Udacity Fullstack Nanodegree program. You can find the <br>
course at [Udacity](https://www.udacity.com/course/programming-foundations-with-python--ud036),
as well as through a nav bar button in the website itself when deployed.

## Setup
To set up the environment for the program, you must download [Python](https://www.python.org/). Make sure it is <br>
version 2.7, as any other version may not be compatible with the code.

Upon installing Python, you can download the program files or clone them to your local <br>
machine using `git clone https://github.com/harshsikka123/Fresh_Tomatoes`

Crack that baby open, and lets begin!

## Files Description

### media.py
This file contains a class _Movie_, which contains an init method with 4 parameters. These<br>
are for the title, description, image, and trailer. There is also a class variable that accounts<br>
for rating of the film.

### entertainment_center.py
This is where the magic happens. This file contains 5 instances of the class _Movie_, where
<br> you can define your own film according to the 4 parameters mentioned above. Adding or<br>
changing a movie is as simple as changing the values or duplicating them.


At the bottom of the program, you can see a list with the movie names. Remember to add any <br>
instances you created. Otherwise they won't be included when fresh_tomatoes.py is used.

### fresh_tomatoes.py
This was a module provided by Udacity. My understanding is that jquery and python were used to <br>
feed the values of the films to an html page that uses Bootstrap. You can fiddle with the css to <br>
customize your site as you see fit.

### .pyc files
I believe that Python automatically compiles your code into the same directory your .py files are in.
That what these two files are, so pay no mind!

## Running
Once you've made all your changes, you can run your program, and a local site should pop up!
