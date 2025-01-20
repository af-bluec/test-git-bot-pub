from setuptools import setup, find_packages

setup(
    name="test-python-repo",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Test Author",
    author_email="test@example.com",
    description="A test Python repository",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/af-bluec/test-git-bot-pub",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
