import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-message-headers",
    version=__import__("headers").VERSION,
    author="Kiran S",
    author_email="kirsn@yahoo.com",
    description="Constants for IANA message headers (http, mime, mail, etc) ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kirsn/py-message-headers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
