# setup.py

from setuptools import setup, find_packages

setup(
    name="execy",
    version="1.0.0",
    author="hglong16",
    author_email="intihad.vuong@gmail.com",
    description="A package for measuring execution time",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    license="MIT",
)
