from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="disnake-paginate",
    version="1.0.1",
    description="A simple Embed Paginator for your projects made with disnake.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=["Paginator"],
    package_dir={'': "src"},
    url="https://github.com/DorianAarno/Paginator",
    author="Aarno Dorian",
    author_email="aarnodorian56@gmail.com",
    download_url = "https://github.com/DorianAarno/Paginator/archive/refs/tags/v1.0.1.tar.gz",
    license = "MIT",
    classifiers=[
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
    ],
      install_requires=[
          'disnake'
      ]
)
