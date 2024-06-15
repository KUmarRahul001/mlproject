from setuptools import find_packages, setup
from typing import List

HYPE_NOT_E = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This fun will return list of requirements
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n"," ")for req in requirements]
        
        if HYPE_NOT_E in requirements:
            requirements.remove(HYPE_NOT_E)
    return requirements

setup(
    name='ML Project',
    version='0.0.1',
    author='Rahul Kumar',
    author_email='Kumarrahulraj468@gmai.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
