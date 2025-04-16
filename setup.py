from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="trading_dashboard_pro",
    version="1.0.0",
    author="SchoolTrad",
    description="Une application dashboard pour gérer et suivre vos configurations de trading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/votre-username/schooltrad",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "trading_dashboard_pro": [
            "config/*.py",
            "models/*.py",
            "views/*.py",
            "utils/*.py",
        ],
    },
)
