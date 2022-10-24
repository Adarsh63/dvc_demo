from setuptools import setup, find_packages # find packeg will find the package from init files
# then call the setup file
setup(
    name ="src", version ="0.0.1", description = "its a wiq package",
    author = "Adarsh",
    packages = find_packages(),
    license ="MIT"
)
# pip install -e . this can help in download the package from the loacal directory this will be we are using after above
# then we can run the command - python setup.py sdist bdist_wheel
