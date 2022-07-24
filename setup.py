from __future__ import annotations

import setuptools

with open('README.md', encoding='utf-8') as fh:
    long_description = fh.read()

github_repository_url = 'https://github.com/saliy/tinkoff-acquiring-api'

setuptools.setup(
    name='tinkoff_acquiring_api',
    author='Artur Saliy',
    author_email='artur.saliy@gmail.com',
    description='Tinkoff Acquiring API client for Python',
    keywords='tinkoff, tinkoff api, tinkoff acquiring',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=github_repository_url,
    project_urls={
        'Documentation': github_repository_url,
        'Bug Reports':
        github_repository_url + '/issues',
        'Source Code': github_repository_url,
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
)
