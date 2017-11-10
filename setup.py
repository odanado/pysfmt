from setuptools import find_packages
from distutils.core import setup, Extension
from Cython.Build import cythonize

ext_modules = []
ext_modules.append(Extension('pysfmt',
                             sources=['SFMT/SFMT.c', 'pysfmt/pysfmt.pyx'],
                             define_macros=[('SFMT_MEXP', '19937')],
                             include_dirs=['SFMT']))
setup(
    name='pysfmt',
    version='0.0.1',
    description='python wrapper of SIMD-oriented Fast Mersenne Twister',
    author='odanado',
    author_email='odan3240@gmail.com',
    url='https://github.com/odanado/pysfmt',
    license='MIT License',
    packages=find_packages(),
    ext_modules=cythonize(ext_modules, build_dir='build'),
    install_requires=['Cython'],
)
