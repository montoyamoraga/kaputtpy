import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kaputt",
    version="0.0.3",
    author="montoyamoraga",
    author_email="montoyamoraga@gmail.com",
    description="python library for making stuff go kaputt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/montoyamoraga/kaputtpy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2"
    ),
)
