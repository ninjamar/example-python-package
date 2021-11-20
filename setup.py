import setuptools

with open("README.md", "r") as h:
  long_description = f.read()

setuptools.setup(
	name='epp',
  version='0.0.1',
  description='Example Python Package',
  author='ninjamar',
  url='https://github.com/ninjamar/example-python-package',
  packages=['epp'],
	long_description=long_description,
	long_description_content_type="text/markdown",
	python_requires='>=3.7',  
)