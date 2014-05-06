from distutils.core import setup

setup(
    name='minifixed',
    version='0.1.0',
    author='Jonas Malaco Filho',
    author_email='jonas@jonasmalaco.com',
    packages=[],
    scripts=['minifixed.py'],
    url='https://github.com/jonasmalacofilho/minifixed',
    license='LICENSE',
    description='Simple fixed-format data reader that guesses offsets.',
    long_description=open('README.md').read(),
    # install_requires=[],
)
