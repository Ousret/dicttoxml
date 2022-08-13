from setuptools import find_packages, setup
from re import search


def get_version():
    with open('dicttoxml2/version.py') as version_file:
        return search(r"""__version__\s+=\s+(['"])(?P<version>.+?)\1""", version_file.read()).group('version')


with open('README.markdown') as readme:
    long_description = readme.read()

setup(
    name='dicttoxml2',
    version=get_version(),
    python_requires=">=3.7, <4",
    description='Converts a Python dictionary or other native data type into a valid XML string. ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ryan McGreal',
    author_email='ryan@quandyfactory.com',
    license='GPL-2.0',
    url='https://github.com/Ousret/dicttoxml',
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
