from setuptools import setup, find_packages

setup(
    name='Pypack1',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Victorshab1/Pypack1',
    author='Victorshab1',
    author_email='victorshab@gmail.com'
)
