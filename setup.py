from setuptools import setup, find_packages

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
        "cryptography"
    ],
    entry_points={
        "console_scripts": [
            "clypher = clypher.main:main"
        ]
    }
)
