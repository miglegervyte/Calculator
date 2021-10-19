from setuptools import setup

setup(
   name='Calculator',
   version='1.0',
   description='Calculator that performs basic mathematical operations',
   author='Migle Gervyte',
   author_email='migle.gervyte@gmail.com',
   packages=['Calculator', 'test'],
   licence='MIT',
   url='https://github.com/miglegervyte/Calculator',
   install_requires=['pytest'],  # external packages as dependencies
)
