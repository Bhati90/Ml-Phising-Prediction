from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            requirements = file.readlines()
            for line in requirements:
                requirement = (line.strip())
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
   
    except FileNotFoundError:
        print("requirement.txt was not found.")
    return requirement_lst
setup(
    name='phishing',
    version='0.0.1',
    author='kishan',
    packages= find_packages(),
    install_requires=get_requirements(),
    description='Phishing Detection using Machine Learning'
)