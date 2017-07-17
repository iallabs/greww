# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, Command

class greww_test_p(Command):
    """Runs all "PYTHON" tests under the greww/folder
    """

    description = "run all tests"
    user_options = []  # distutils complains if this is not here.

    def __init__(self, *args):
        self.args = args[0]  # so we can pass it to other classes
        Command.__init__(self, *args)

    def initialize_options(self):  # distutils wants this
        pass

    def finalize_options(self):    # this too
        pass

    def run(self):
        from greww.utils.runtests import run_all_tests
        run_all_tests()

class greww_test_c(Command):
    """Runs all "C++" tests under the greww/folder
    """

    description = "run all tests"
    user_options = []  # distutils complains if this is not here.

    def __init__(self, *args):
        self.args = args[0]  # so we can pass it to other classes
        Command.__init__(self, *args)

    def initialize_options(self):  # distutils wants this
        pass

    def finalize_options(self):    # this too
        pass

    def run(self):
        from greww.utils.runtests import c_run_all_tests
        c_run_all_tests()


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name='Greww',
    version='0.0.1',
    description='Greeeeewwww',
    long_description=readme,
    author='Imp Alpha lab',
    author_email='hilalyamine@gmail.com',
    cmdclass={
        'test' : greww_test_p,
        'ctest' : greww_test_c,
    },
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'experience', 'cgreww'))
)
