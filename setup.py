from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="disnake-paginator",
    version="1.0",
    description="A simple Embed Paginator for your projects made with disnake.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=["Paginator"],
    package_dir={'': "src"},
    url="",
    author="AarnoDorian",
    author_email="aarnodorian56@gmail.com",
    classifiers=[
        'License :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ]
)
