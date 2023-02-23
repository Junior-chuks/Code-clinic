# from distutils.core import setup
from setuptools import setup,find_packages



setup(
    name = "Code Clinic Calendar",
    version = "0.01",
    packages = find_packages(),
    license= "WTC",
    long_description="",
    entry_points ={
        "console_scripts":["code-clinic=code_clinic:commands"]
    }
)