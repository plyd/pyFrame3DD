# setup.py
# only if building in place: ``python setup.py build_ext --inplace``

from setuptools import setup
from distutils.core import setup, Extension
import os
# from numpy.distutils.core import setup, Extension



if os.name == 'nt':  # Windows.
#    extra_compile_args = ['/TC', '/D', 'ANSI'] # for msvs (we use mingw (gcc) now by default)
    extra_compile_args = ''
else:
    extra_compile_args = ''


setup(
    name='pyFrame3DD',
    version='1.0.0',
    description='Python bindings to Frame3DD',
    author='S. Andrew Ning',
    author_email='andrew.ning@nrel.gov',
    package_dir={'': 'src'},
    py_modules=['frame3dd'],
    license='Apache License, Version 2.0',
    ext_modules=[Extension('_pyframe3dd', ['src/pyframe3dd/py_main.c', 'src/pyframe3dd/py_io.c',
                                           'src/pyframe3dd/frame3dd.c', 'src/pyframe3dd/HPGmatrix.c', 'src/pyframe3dd/coordtrans.c',
                                           'src/pyframe3dd/eig.c', 'src/pyframe3dd/HPGutil.c', 'src/pyframe3dd/NRutil.c'],
                 extra_compile_args=extra_compile_args)]
)
