from setuptools import setup

setup(name="chucknorris",
      version="0.1",
      description="chucknorris python bindings",
      author="Dimitri Merejkowsky",
      py_modules=["chucknorris"],
      setup_requires=["cffi", "path.py"],
      cffi_modules=["build_chucknorris.py:ffibuilder"],
      install_requires=["cffi"],
      )
