
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cpkg",
    version="0.0.1",
    author="xiongts",
    author_email="Mr_Xiongts@163.com",
    description=".",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seoul2k/cpkg",
    project_urls={'Bug Tracker': 'https://github.com/seoul2k/cpkg/issues'},
    classifiers=['Development Status :: 4 - Beta', 'Operating System :: OS Independent', 'Intended Audience :: Developers', 'License :: OSI Approved :: BSD License', 'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: Implementation', 'Programming Language  :: Python :: 3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.8', 'Topic :: Software Development :: Libraries'],
    packages=["cpkg/"],
    python_requires=">=3",
    install_requires = [],
    entry_points=""
        )