from setuptools import find_packages , setup

def get_requirements(file_path):
    with open(file_path) as file_obj:
        requirements=file_obj.read().splitlines()
    return [req for req in requirements if req!="-e ."]


setup(
    name="Apporval-Matrix",
    version="0.0.1",
    author="Kartik Bhardwaj",
    author_email="kartiksb911@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)