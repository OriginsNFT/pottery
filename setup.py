# --------------------------------------------------------------------------- #
#   setup.py                                                                  #
#                                                                             #
#   Copyright © 2015-2022, Rajiv Bakulesh Shah, original author.              #
#                                                                             #
#   Licensed under the Apache License, Version 2.0 (the "License");           #
#   you may not use this file except in compliance with the License.          #
#   You may obtain a copy of the License at:                                  #
#       http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                             #
#   Unless required by applicable law or agreed to in writing, software       #
#   distributed under the License is distributed on an "AS IS" BASIS,         #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#   See the License for the specific language governing permissions and       #
#   limitations under the License.                                            #
# --------------------------------------------------------------------------- #


import pathlib

from setuptools import find_packages
from setuptools import setup

try:
    import pottery
except ModuleNotFoundError:
    pass

name = 'pottery'
version = '3.1.0rc9'
description = 'pottery'
url = 'https://github.com/brainix/pottery'
author = 'Rajiv Bakulesh Shah'
author_email = 'brainix@gmail.com'
license = 'Apache 2.0'
keywords = 'Redis client persistent storage'
copyright = f'Copyright © 2015-2022, {author}, original author.'

_package_dir = pathlib.Path(__file__).parent
_long_description = (_package_dir / 'README.md').read_text()


setup(
    name=name,
    version=version,
    description=description,
    long_description=_long_description,
    long_description_content_type='text/markdown',
    url=url,
    author=author,
    author_email=author_email,
    license=license,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Development Status :: 4 - Beta',
        'Topic :: Database :: Front-Ends',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: AsyncIO',
        'Typing :: Typed',
    ],
    keywords=keywords,
    python_requires='>=3.9, <4',
    install_requires=('redis==4.5.1, <5', 'mmh3'),
    extras_require={},
    packages=find_packages(exclude=('contrib', 'docs', 'tests*')),
    package_data={'pottery': ('py.typed',)},
    data_files=tuple(),
    entry_points={},
)
