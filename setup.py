""" required module-docstring for pylint purposes """

# pathlib before setuptools as suggested by pylint
from pathlib import Path
import setuptools

with open("requirements.txt", encoding="utf-8") as f:
    install_requires = f.read().splitlines()

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setuptools.setup(
    name="album-of-the-year-api",
    description="Lightweight Python library that acts as an API for the website albumoftheyear.org",
    version="0.2.7",
    license="GNU",
    author="Jahsias White",
    author_email="jahsias.white@gmail.com",
    packages=["albumoftheyearapi"],
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JahsiasWhite/AlbumOfTheYearWrapper",
)
