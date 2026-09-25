# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="standard-color-palette",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["standard_color_palette", "palette"],
    package_data={
        "": ["*.json", "*.css", "*.md", "charts/*"]
    },
    include_package_data=True,
    install_requires=[
        "matplotlib>=3.3.0"
    ],
    author="xair330",
    description="Civil Aviation Statistical Analysis Standard Color Palette Library",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xair330/standard-color-palette",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Visualization",
    ]
)
