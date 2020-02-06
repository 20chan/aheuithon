from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib

with open("Readme.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    liccense = f.read()

setup(
    name="aheuithon",
    version="0.0.1",
    description="Write inline aheui function",
    long_description=readme,
    author="20chan",
    author_email="2@0chan.dev",
    url="https://github.com/20chan/aheuithon",
    liccense=license,
    packages=find_packages(exclude=()),
    install_requires=["parso"],
)