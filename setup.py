import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kaputt",
    version="0.0.2",
    author="montoyamoraga",
    author_email="montoyamoraga@gmail.com",
    description="python library for making stuff go kaputt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/montoyamoraga/kaputtpy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
