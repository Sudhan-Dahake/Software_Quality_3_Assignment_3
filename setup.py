"""
Setup script for the Hand Digit Recognition project.
This script uses setuptools to package and distribute the project.
"""

from setuptools import setup, find_packages

setup(
    name='Hand digit recognition',
    version='0.1',
    packages=find_packages(
        where='.',
    ),
    include_package_data=True,
    package_data={
        '': ['static/*', 'templates/*', 'test_images/*', '*.py', '*.md', '*.txt', '*.html'],
    },
)
