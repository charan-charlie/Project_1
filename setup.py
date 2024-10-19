from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
     

    # This function will return list of get_requirements

    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if(HYPEN_E_DOT in requirements):
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = "ML_Project_1",
    version = "0.0.1",
    author = "Charan",
    author_email = "derangulacharandcharan@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
