from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="LES",
    version="1.0.0",
    author="Lenz Byahurwa",
    author_email="lenzbyahurwa@gmail.com",
    description="Lenz Encryption Standard (LES) implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LenzB1987/LES",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
    ],
    python_requires=">=3.6",
    keywords="encryption cryptography security",
    project_urls={
        "Bug Reports": "https://github.com/LenzB1987/LES/issues",
        "Source": "https://github.com/LenzB1987/LES",
    },
)