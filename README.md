name: Lucas Welsh
email "lwelsh2@uoregon.edu"

This program is a webpage implementing the ACP brevet control times calulator algorithm, this is an algorithm used to control the speed bikers use during intervals of a race. The algorithm uses a given distance brevet, as well as a maximum and minimum speed to calculate the the opening time based on maximum speed, and a closing time based on minimum speed. The program is used by inputting a distance and a brevet, and is updated to calculate the opening and closing times by the server, brevets are calculated differently based on distances in blocks of km from 0-200 to 1000-3000.

New functionality added includes a Submit and Display button. The submit buttion inserts given control times into a MongoDB database and the Display button fills the page with the stored entries. Tests to ensure this and the previous implmentation work correctly are also included.
