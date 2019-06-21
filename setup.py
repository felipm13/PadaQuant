from distutils.core import setup

setup(
    name='PadaQuant',
    version='0.1',
    author='Luis F. Silva',
    author_email='lf.mouradasilva@gmail.com',
    packages=['padaquant'],
    url='https://github.com/felipm13/PadaQuant',
    license='LICENSE',
    description='A framework for quantitative finance In python',
    long_description=open('README.md').read(),
    install_requires=[
        "pandas >= 0.10.0",
        "matplotlib >= 1.1.0",
    ],
)
