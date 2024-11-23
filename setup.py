from setuptools import setup, find_packages

setup(
    name='Hand digit recognition',
    version='0.1',
    packages=find_packages(
        where='.',
        # Exclude unwanted directories
        exclude=['static', 'templates', 'test_images'],
    ),
)