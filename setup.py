from setuptools import setup, find_packages
import re

VERSIONFILE = "clypher/_version.py"
with open(VERSIONFILE) as vf:
    exec(vf.read())

REQUIREMENTS = [l.strip() for l in open("requirements.txt").readlines()]

setup(
    name="Clypher",
    version=__version__,
    packages=find_packages(),
    install_requires=[        
        "Sphinx",
        "typer[all]",
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "clypher = clypher.main:app"
        ]
    }
)
