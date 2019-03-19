from setuptools import setup, find_packages

setup(
    name='newpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='My EDSA python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Khaleec/newpackage',
    author='Khaleec',
    author_email='dieketsengmd@gmail.com'
)
