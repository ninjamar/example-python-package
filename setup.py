import setuptools

with open("README.md", "r") as f:
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
	license_files = ("LICENSE",),
	python_requires='>=3.7',  
)
