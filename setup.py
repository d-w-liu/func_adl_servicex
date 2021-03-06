# setuptools loads some plugins necessary for use here.
from setuptools import find_packages  # noqa: F401
from distutils.core import setup

# Use the readme as the long description.
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="func_adl_servicex",
      version='1.0.0a1',
      packages=['func_adl_servicex'],
      scripts=[],
      description="Submit Functional Queries to a ServiceX endpoint.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="G. Watts (IRIS-HEP/UW Seattle)",
      author_email="gwatts@uw.edu",
      maintainer="Gordon Watts (IRIS-HEP/UW Seattle)",
      maintainer_email="gwatts@uw.edu",
      url="https://github.com/iris-hep/func_adl_servicex",
      license="TBD",
      test_suite="tests",
      install_requires=[
          "func_adl>=1.1b10",
          "qastle==0.8",
          "servicex>=2.0"
      ],
      extras_require={
          'test': [
              'pytest>=3.9',
              'pytest-asyncio',
              'pytest-mock',
              'pytest-cov',
              'coverage',
              'flake8',
              'codecov',
              'autopep8',
              'twine',
              'testfixtures',
              'wheel',
              'asyncmock'
          ],
      },
      classifiers=[
          # "Development Status :: 3 - Alpha",
          "Development Status :: 4 - Beta",
          # "Development Status :: 5 - Production/Stable",
          # "Development Status :: 6 - Mature",
          "Intended Audience :: Developers",
          "Intended Audience :: Information Technology",
          "Programming Language :: Python",
          "Topic :: Software Development",
          "Topic :: Utilities",
      ],
      package_data={
          'func_adl_xAOD/backend': ['R21Code/*'],
      },
      platforms="Any",
      )
