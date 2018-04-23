import setuptools

import Cython.Distutils
import numpy as np

import ann_solo


DISTNAME = 'ann-solo'
VERSION = ann_solo.__version__
DESCRIPTION = 'Spectral library search engine optimized for fast open ' \
              'modification searching'
with open('README.md') as f_in:
    LONG_DESCRIPTION = f_in.read()
AUTHOR = 'Wout Bittremieux'
AUTHOR_EMAIL = 'wout.bittremieux@uantwerpen.be'
URL = 'https://github.com/bittremieux/ANN-SoLo'
LICENSE = 'Apache 2.0'


compile_args = ['-O3', '-march=native', '-ffast-math',
                '-fno-associative-math', '-std=c++14']
ext_module = setuptools.Extension(
        'ann_solo.spectrum_match',
        ['ann_solo/spectrum_match.pyx', 'ann_solo/SpectrumMatch.cpp'],
        language='c++', extra_compile_args=compile_args,
        extra_link_args=compile_args, include_dirs=[np.get_include()])

setuptools.setup(
        name=DISTNAME,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        url=URL,
        license=LICENSE,
        platforms=['any'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: MacOS',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: Unix',
            'Programming Language :: C++',
            'Programming Language :: Cython',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3 :: Only',
            'Topic :: Scientific/Engineering :: Bio-Informatics'],
        packages=['ann_solo'],
        entry_points={
            'console_scripts': ['ann-solo = ann_solo.ann_solo:main']},
        cmdclass={
            'build_ext': Cython.Distutils.build_ext},
        install_requires=[
            'annoy',
            'ConfigArgParse',
            'Cython',
            'joblib',
            'numexpr',
            'numpy',
            'pandas',
            'pyteomics',
            'scipy',
            'tqdm'],
        setup_requires=[
            'Cython',
            'numpy'],
        ext_modules=[ext_module],
)
