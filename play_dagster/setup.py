from setuptools import find_packages, setup

setup(
    name="play_dagster",
    packages=find_packages(exclude=["play_dagster_tests"]),
    install_requires=[
        "dagster",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
