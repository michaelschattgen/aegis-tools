from setuptools import find_packages, setup

__version__ = "0.0.0"

setup(
    name="aegis-tools",
    version=__version__,
    description="A collection of developer tools for Aegis Authenticator",
    author="Alexander Bakker",
    author_email="github@alexbakker.me",
    url="https://github.com/alexbakker/aegis-tools",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "cairosvg",
        "cryptography",
        "xmltodict"
    ],
    entry_points={
        "console_scripts": [
            "aegis-tools=aegis_tools:main",
        ],
    },
    license="GPLv3"
)
