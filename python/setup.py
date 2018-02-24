from setuptools import setup, find_packages

setup(name="chucknorris",
      version="0.1",
      description="chucknorris python bindings",
      author="Dimitri Merejkowsky",
      packages=find_packages(),
      include_package_data=True,
      setup_requires=["cffi"],
      cffi_modules=["build_chucknorris.py:ffibuilder"],
      install_requires=["cffi"],
      )
