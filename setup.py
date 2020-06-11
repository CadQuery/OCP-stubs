from setuptools import setup
import os


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, '', 1)
            stubs.append(path)
    return dict(package=stubs)


setup(
    name='OCP-stubs',
    maintainer="OCP Developers",
    description="PEP 561 type stubs for OCP",
    version='1.0',
    packages=['OCP-stubs'],
    # PEP 561 requires these
    install_requires=[],
    package_data=find_stubs('OCP-stubs'),
)
