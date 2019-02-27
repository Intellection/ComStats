from distutils.core import setup

setup(
    # Application name:
    name="ComStats",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Data Science Team @ Zappistore",
    author_email="datascience@zappistore.com",

    # Packages
    packages=[],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/ComStats_v010/",

    # license="LICENSE.txt",
    description="Do combinatorial statistics on numpy ndarrays",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "numpy",
        "scipy",
    ],
)