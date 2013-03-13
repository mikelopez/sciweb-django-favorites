from setuptools import setup, find_packages
import sys, os

setup(
    name='favorites',
    version='0.2',
    description="Basic scalable Favorites module for django",
    long_description=open('README.rst', 'r').read(),
    keywords='python, django, favorites',
    author='Marcos Lopez',
    author_email='dev@scidentify.info',
    url='',
    license='MIT',
    package_dir={'favorites': 'favorites'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: Security",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
    ]
)
