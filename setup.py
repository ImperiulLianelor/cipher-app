from setuptools import setup, find_packages

setup(
    name='cipher-cli',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'cipher-cli=main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A CLI application for classic cipher encryption and decryption',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
