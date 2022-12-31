from setuptools import setup

setup(
    name='OCP-stubs',
    maintainer="OCP Developers",
    description="PEP 561 type stubs for OCP",
    version='7.7.7',
    packages=['OCP-stubs'],
    # PEP 561 requires these
    install_requires=[],
    include_package_data = True, #see MANIFEST
)
