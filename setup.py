from setuptools import setup, find_packages
import os


def read(*paths):
    """Read contents of a text file safely
    >>> read("dundie", "Version")
    """
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)

    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    """ Return a list of require form a text file"""

    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', '-'))
    ]


setup(
    name="dundie",
    version="0.1.0",
    description="reward system",
    long_description=("README.md"),
    long_description_content_type="text/markdown",
    author="Regina Celi da Silva",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__: main"
        ]
    },
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements.test.txt"),
        "dev": read_requirements("requirements.dev.txt")
    }
)
