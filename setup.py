from setuptools import setup, find_packages
import os


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


def get_version():
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "mycli", "version.py"
    )
    g = {}
    with open(path) as fp:
        exec(fp.read(), g)
    return g["__version__"]

setup(
    name="mycli",
    version=get_version(),
    description="cli",
    long_description=get_long_description(),
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "click>=7.1.1",
        "click-default-group-wheel>=1.2.2"
    ],
    entry_points="""
        [console_scripts]
        mycli=mycli.cli:cli
    """
)


