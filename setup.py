from setuptools import setup
from typing import List, Dict


#declaring variables for the setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR_NAME = "Abhishek"
DESCRIPTION = "This is a first FSDS Nov natch machine learning project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirement_list()->List[str]:
    """
    Description: This fucntion is going to return list of requirement mention in the 
    requirements.txt file
    
    this fucntion is going to return a list which contain name of libraries mentioned in the 
    requirements.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requries=get_requirement_list()
)




