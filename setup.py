import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="sort_my_downloads",
    version="0.0.6",
    description="Sort your downloaded files into categorised folders.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/TebzaTheMan/sort_my_downloads",
    author="Tebogo Nomnqa",
    author_email="tebzax2@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sort_my_downloads = sort_my_downloads.sort_my_downloads:main'
        ]
    },
    include_package_data=True,
    install_requires=["watchdog"],
)
