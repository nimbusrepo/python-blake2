from distutils.core import setup, Extension
 
module1 = Extension('blake2',
                sources = ['blake2/blake2module.c','blake2/blake2b-ref.c','blake2/blake2s-ref.c'],
                include_dirs = ['blake2'],
                extra_compile_args = ["-std=c99", "-Wall", "-pedantic"] )

 
setup (name = 'blake2',
        packages=['blake2'],
        version = '0.1.6',
        ext_modules = [module1],
        description = 'blake2 hash function module for python',
        license='Public Domain',
        author='Bae KwonHan',
        author_email='darjeeling@gmail.com',
        maintainer='Bae KwonHan',
        maintainer_email='darjeeling@gmail.com',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
            'Operating System :: POSIX',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: Implementation :: CPython',
            'Topic :: Security :: Cryptography'
          ],
        )
