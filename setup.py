import setuptools

__version__="0.0.0"

REPO_NAME = 'Wine_project'
AUTHOR_USER_NAME = 'SAMEER'
SRC_REPO = 'mlProject'
AUTHOR_EMAIL = 'Sameerup1996@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for ml app',
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)