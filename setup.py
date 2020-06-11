from setuptools import setup
import os


setup(
    name='OCP-stubs',
    maintainer="OCP Developers",
    description="PEP 561 type stubs for OCP",
    version='1.0',
    packages=['OCP-stubs'],
    # PEP 561 requires these
    install_requires=[],
    include_package_data = True, #see MANIFEST
)
