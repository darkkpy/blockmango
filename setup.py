from setuptools import setup
import os

def read_md_files(filenames):
    content = ""
    for filename in filenames:
        if filename == "README.md":
            with open(filename, "r", encoding="utf-8") as file:
                content += file.read() + "\n\n"
        else:
            with open(os.path.join("docs", filename), "r", encoding="utf-8") as file:
                content += file.read() + "\n\n"
    return content

markdown_files = [
    "README.md",
    "friends.md",
    "groupchat.md",
    "user.md",
    "clan.md",
    "decoration.md"
]

long_description = read_md_files(markdown_files)

setup(
    name='blockmango',
    version='1.4.6',
    author='Dark',
    author_email='darkness0777@proton.me',
    description='Blockman Go API package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/darkkpy/blockmango',
    packages=['blockmango'],
    install_requires=['requests'],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Documentation': 'https://github.com/darkkpy/blockmango/tree/main/docs',
        'Source': 'https://github.com/darkkpy/blockmango',
        'Tracker': 'https://github.com/darkkpy/blockmango/issues',
    },
    keywords='blockmango blockman go api wrapper',
    license='MIT',
)
