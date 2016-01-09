from setuptools import setup

import synpy

setup(
    name=synpy.__name__,
    description=synpy.__doc__,
    author=synpy.__author__,
    author_email='mohd.akram@outlook.com',
    url='https://github.com/mohd-akram/synpy',
    packages=['synpy'],
    classifiers=[
        'Programming Language :: Python :: 3.5'
    ],
    zip_safe=False,
)
