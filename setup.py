from setuptools import find_packages , setup
from typing import List

HYPEN_E_DOT = "-e ." # it is map to setup.py

# file_path: str means the file_path argument is a string that represents the path to the file you want to open.
# List[str] means each item in the list will be a string.
# -> return type hint ,It is purely optional and serves as a type hint to improve code clarity and help with static analysis.

def get_requirements(file_path:str)->List[str]:
    """
    This function will return a list of requirements.
    It reads a requirements file, processes each line, 
    and returns a list of requirements (removes any occurrences of '-e').
    """
    requirements =[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="Apporval-Matrix",
    version="0.0.1",
    author="Kartik Bhardwaj",
    author_email="kartiksb911@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)