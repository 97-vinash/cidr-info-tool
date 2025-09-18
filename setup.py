from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cidr-info-tool",
    version="1.0.0",
    author="Avinash Shankar(97-vinash)",
    author_email="97.vinash@gmail.com",
    description="A CLI tool to get detailed network information from IP addresses in CIDR notation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/97-vinash/cidr-info-tool",
    py_modules=["cidr_info"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: System :: Networking",
        "Topic :: Utilities",
    ],
    keywords="cidr, ip, subnet, network, networking, cli",
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "cidr-info=cidr_info:main",
        ],
    },
)