from setuptools import setup

setup(
    name='awsclient',
    version='0.0.1',
    description='Tools to access a variety of the services offered by AWS',
    url='https://github.com/dangoodman5425/services/awsclient',
    author='Dan Goodman',
    author_email='danielgoodman5425@github.com',
    packages=[
        'awsclient',
    ],
    install_requires=[
        'boto3==1.7.70',
        'boto==2.48.0',
        'botocore==1.10.70',
        'simplejson==3.15.0',
    ],
    zip_safe=False,
)
