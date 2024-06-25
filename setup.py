import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gphoto2-super-fast",
    version="0.0.1",
    author="IArchi",
    author_email="author@example.com",
    description="A new implementation of gphoto2 for Python that goes way faster than existing libraries to avoid lag.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IArchi/py-gphoto2-super-fast/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache-2.0 license",
        "Operating System :: OS Independent",
    ],
)
