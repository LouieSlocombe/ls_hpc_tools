from setuptools import setup, find_packages

setup(
    name='ls_hpc_tools',
    version='0.0.0',
    author='Louie Slocombe',
    author_email='louies@hotmail.co.uk',
    description='A repo containing some tools for running things on a HPC.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/LouieSlocombe/ls_hpc_tools',
    packages=find_packages(include=['ls_hpc_tools', 'ls_hpc_tools.*']),
    package_data={
        'ls_hpc_tools': [
            'data/*',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    install_requires=[
        'numpy',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
        ],
    },
)
