from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="trading_dashboard_pro",
    version="1.0.0",
    author="SchoolTrad",
    description="Une application dashboard pour gérer et suivre vos configurations de trading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/idhaoss/SchoolTrad",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.28.0",
        "pandas>=1.5.0",
        "pillow>=9.0.0",
        "numpy>=1.21.0",
        "plotly>=5.13.0",
        "watchdog>=3.0.0",
    ],
    include_package_data=True,
)
