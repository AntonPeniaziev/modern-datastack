from setuptools import find_packages, setup

setup(
    name="jaffle",
    packages=find_packages(exclude=["jaffle_tests"]),
    install_requires=[
        "dagster",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
