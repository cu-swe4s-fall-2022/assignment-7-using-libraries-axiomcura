"""Sets up DataProc package in your environment
"""
from setuptools import find_packages, setup

setup(
    name="DataProc",
    version="0.0.1",
    author="Erik Serrano",
    description="Processes tabular dataset",
    packages=find_packages(),
    scripts=["plotter.py"]
)
