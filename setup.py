import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("requirements.txt", "rt", encoding="utf8") as f:
    require = f.readlines()
require = [x.strip() for x in require]

setup(
    name="pylcf",
    version="0.0.1",
    url="https://github.com/RPGToucan/pylcf",
    license="MIT",
    maintainer="RPGToucan team",
    maintainer_email="none@...",
    description="Python library for reading and writing LCF files",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=require,
    extras_require={"test": ["pytest", "coverage"]},
)
