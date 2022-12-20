import os
import datetime
import shutil


class PathNotFoundError(Exception):
    def __init__(self):
        super()

    def __str__(self):
        return 'The name {} does not meet the specification.'.format(self.name)


class NameNotSpecificationError(Exception):
    def __init__(self, name):
        super()
        self.name = name

    def __str__(self):
        return 'Path is not found.'


class NameNotFoundError(Exception):
    def __init__(self, name):
        super()
        self.name = name

    def __str__(self):
        return '{} is not found.'.format(self.name)


class Create:
    def __init__(self, *new, entry_points='""', **kw):
        self.default(kw, entry_points, new)

    def createFile(self, path, name, value):
        with open(path+name, 'w')as f:
            f.write(value)

    def createDir(self, dirName):
        name = dirName
        if name[len(name)-1] != '/':
            raise NameNotSpecificationError(dirName)
        while True:
            try:
                os.makedirs(name)
                break
            except Exception as e:
                while True:
                    inp = input(
                        '文件夹已存在，是否删除？\nThe dir already exists. Do you want to delete it? (y/N) ')
                    if inp == 'y':
                        shutil.rmtree(name[2:])
                        break
                    elif inp == 'N':
                        quit(repr(e))
                    else:
                        continue

    def default(self, kw, entry_points, new):
        try:
            kw['path']
        except KeyError:
            raise PathNotFoundError()
        lt = ['dirName', 'pkgName', 'author',
              'author_email', 'description', 'url', 'project_urls', 'classifiers', 'python_requires', 'install_requires']
        try:
            dirName = kw["dirName"]
        except KeyError:
            raise NameNotFoundError("dirName")
        try:
            pkgName = kw["pkgName"]
        except KeyError:
            raise NameNotFoundError("pkgName")
        try:
            author = kw["author"]
        except KeyError:
            raise NameNotFoundError("author")
        try:
            author_email = kw["author_email"]
        except KeyError:
            raise NameNotFoundError("author_email")
        try:
            description = kw["description"]
        except KeyError:
            raise NameNotFoundError("description")
        try:
            url = kw["url"]
        except KeyError:
            raise NameNotFoundError("url")
        try:
            project_urls = kw["project_urls"]
        except KeyError:
            raise NameNotFoundError("project_urls")
        try:
            classifiers = kw["classifiers"]
        except KeyError:
            raise NameNotFoundError("classifiers")
        try:
            python_requires = kw["python_requires"]
        except KeyError:
            raise NameNotFoundError("python_requires")
        try:
            install_requires = kw["install_requires"]
        except KeyError:
            raise NameNotFoundError("install_requires")
        self.createDir('./'+dirName+'/')
        self.createFile('./'+dirName+'/', 'LICENSE',
                        '''
MIT License

Copyright (c) [{}] [{}]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.                    
'''.format(datetime.datetime.now().year, pkgName))
        print('INFO[000] create the LICENSE file')
        self.createFile('./'+dirName+'/', 'pyproject.toml',
                        '''
[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"                   
''')
        print('INFO[001] create the pyproject.toml file')
        self.createFile('./'+dirName+'/', 'README.md', '# your project readme')
        print('INFO[001] create the README.md file')
        setup = '''
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{}",
    version="0.0.1",
    author="{}",
    author_email="{}",
    description="{}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{}",
    project_urls={},
    classifiers={},
    packages=["{}"],
    python_requires=">={}",
    install_requires = {},
    entry_points={}
        '''.format(pkgName, author, author_email, description, url, project_urls, classifiers, dirName, python_requires, install_requires, entry_points)
        if new:  # ((key,value),(key1,value1)...)
            for i in new:
                for x in i:
                    setup = setup + ',\n' + x[0]+'='+x[1]
        setup += ')'
        self.createFile('./'+dirName+'/', 'setup.py', setup)
        print('INFO[002] create the setup.py file')
        self.createDir('./'+dirName+'/'+dirName+'/')
        print('INFO[004] create the src dir')
        self.createFile(f'./'+dirName+'/'+dirName+'/', '__init__.py',
                        f'from .{pkgName} import *')
        print('INFO[005] create the __init__.py file')
        self.createFile('./'+dirName+'/'+dirName+'/',
                        f'{pkgName}.py', '# your python file')
        print(f'INFO[006] create the {pkgName}.py file')
        print(f'{pkgName} is success!')
        print(f'''Pleace use:
              cd {pkgName}
              python setup.py sdist''')


Create(
    path='./',
    author='xiongts',
    author_email='Mr_Xiongts@163.com',
    dirName='s',
    pkgName='s',
    description='.',
    url='https://github.com/seoul2k/s',
    project_urls={
        "Bug Tracker": "https://github.com/seoul2k/s/issues",
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation',
        'Programming Language  :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ],
    python_requires=3,
    install_requires=[]
)
