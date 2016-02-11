from distutils.core import setup

# This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = []

setup(name="crenation-utils",
      version="0.2",
      description="utility software necessary for running a Crenation module",
      author="lto",
      author_email="lorenzo.tomasini@fokus.fraunhofer.de",
      url="",
      packages=['crenation_utils.agents', 'crenation_utils.annotation', 'crenation_utils.model',
                'crenation_utils.utils'],
      package_data={'package': files},
      long_description=open('README.md').read()
      #classifiers = []
) 