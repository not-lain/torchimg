import pathlib
from setuptools import find_packages, setup


def get_version() -> str:
    rel_path = "src/torchimg/__init__.py"
    with open(rel_path, "r") as fp:
        for line in fp.read().splitlines():
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name="torchimg",
    version=get_version(),
    description="a python package for illustrating pytorch models",
    long_description=pathlib.Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    Homepage="https://github.com/not-lain/torchimg",
    url="https://github.com/not-lain/torchimg",
    Issues="https://github.com/not-lain/torchimg/issues",
    authors=[{"name": "hafedh hichri", "email": "hhichri60@gmail.com"}],
    author_email="hhichri60@gmail.com",
    license="Apache 2.0 License",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    classifiers=["Topic :: Utilities", "Programming Language :: Python :: 3.9"],
    requires=["setuptools", "wheel", "typing", "torch"],
)
