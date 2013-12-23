"""Setup script for adjspecies. Use `pip install .` in this directory."""

from setuptools import setup
import adjspecies


setup(
    name='adjspecies',
    version=0.1,
    description=adjspecies.__doc__,
    long_description=(open('README.rst').read()),
    url='http://github.com/hipikat/adjspecies/',
    license='BSD 2-Clause',
    author='Adam Wright',
    author_email='adam@hipikat.org',
    packages=['adjspecies'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'adjspecies = adjspecies:main',
        ],
    }
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
