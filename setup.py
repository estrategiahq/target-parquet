#!/usr/bin/env python

from setuptools import setup

setup(
    name="target-parquet",
    version="0.2.2",
    description="Singer.io target for writing into parquet files",
    author="Rafael 'Auyer' Passos",
    url="https://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["target_parquet"],
    install_requires=[
        "jsonschema==2.6.0",
        "singer-python==5.12.1",
        "pyarrow==4.0.1",
        "psutil==5.8",
    ],
    extras_require={
        'dev': [
            'pytest==6.2.4',
            'pandas==1.2.4'
        ]
    },
    entry_points="""
          [console_scripts]
          target-parquet=target_parquet:main
      """,
    packages=["target_parquet"],
)
