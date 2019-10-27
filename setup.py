from pathlib import Path
from setuptools import setup, find_packages

version = open('VERSION').read()
license = open('LICENSE').read()
long_description = open('README.md').read()

setup(
    name = "searchyt",
    version = version,
    license = license,
    author = "La_Blazer",
    author_email = "blazer@lblzr.com",
    description = "Lightweight Python 3 library for searching youtube videos without API key",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/LaBlazer/searchyt",
    packages=find_packages(),
    install_requires = [
        "requests"
    ],
    zip_safe = True,
    test_suite = "tests",
    python_requires='>=3.6',
    keywords = ["yt", "youtube", "search", "scrape", "videos", "api", "key"],
    classifiers = [
        "Programming Language :: Python :: 3.6", 
        "License :: OSI Approved :: Apache Software License", 
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Multimedia :: Video",
        "Topic :: Utilities",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers"
    ]
)