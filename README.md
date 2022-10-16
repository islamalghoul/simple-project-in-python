## LAB - Class 06
## Project name: Rhythms Cinema
version: 0.2
## Author: **Mostafa Albelbeisi & Islam Alghoul**
**Links and Resources**
**Setup**
- pip install -r requirements.txt
- pip install requests
- pytest
**How to initialize/run your application (where applicable)**
- git init
- python -m venv .venv
- source .venv/bin/activate
- python3 For_Series/display_info.py
- python3 For_Movies/display_info.py
- python3 Everything/display_All.py
**How to use your library (where applicable)**
- Pytest
## Tests
- **How do you run tests?** pytest
- **Any tests of note?** No
- **The idea**
 of the project is to display movies and series that enter the user name, so that it displays the full name of the mouth, description, evaluation and the number of voters,
Also, the user can see the works related to the movie or series that he searched for.
- **Describe any tests that you did not complete, skipped, etc**
This project contains four folders, each folder contains two files written in Python
### The first folder it's [For_Movies](/home/mostafa/project-in-python1/For_Movies)
**contains two folder**
1. [Movies_class](/home/mostafa/project-in-python1/For_Movies/Movies_class.py):
This file contains two classes
Class movies, through which the data is called from the API through the attributes that have been defined such as title, rating, number of voters, etc., and a funchain is created for each attributes to link the attributes in it in order to take information from the API
Class Movie, this class inherits from the class movies the attributes that were created in it, then a funchain is created for the formats of the attributes that come from the API
2. [display_info](/home/mostafa/project-in-python1/For_Movies/display_info.py):
The file display the results to the user
- This folder is called in the terminal by python3 **For_Movies/display_info.py**
### The second folder it's [For_Series](/home/mostafa/project-in-python1/For_Series)
**This folder contains two file**
1. [Series_class](/home/mostafa/project-in-python1/For_Movies/Movies_class.py):
Just like a movie file --> [Movies_class](/home/mostafa/project-in-python1/For_Movies/Movies_class.py)
2. [display_info](/home/mostafa/project-in-python1/For_Movies/display_info.py):
Just like a movie file --> [display_info](/home/mostafa/project-in-python1/For_Movies/display_info.py)
### The third folder it's [Everything](/home/mostafa/project-in-python1/Everything)
In this folder, we combined the two folders together so that the movie and series file was placed in it, so that the data display was collected in the display all file
### The fourth folder it's [test](/home/mostafa/project-in-python1/test)
**This folder contains two file**
1. [test_Movies_class](/home/mostafa/project-in-python1/test/test_Movies_class.py)
2. [test_Series_class](/home/mostafa/project-in-python1/test/test_Series_class.py)
* Here in these files were created tests for the attributes that were created in movies and series, and the test is performed in the terminal by typing pytest.

# hi