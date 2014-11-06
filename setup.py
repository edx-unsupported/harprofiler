import os
from distutils.core import setup


this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.rst')) as f:
    LONG_DESCRIPTION = '\n' + f.read()

requirements = os.path.join(this_dir, 'requirements.txt')
REQUIREMENTS = filter(None, open(requirements).read().splitlines())


setup(
    name='harprofiler',
    version='0.1.0',
    py_modules=['harprofiler'],
    install_requires=REQUIREMENTS,
    author='edX Test Engineering Team',
    author_email='cgoldberg _at_ gmail.com',
    description='Automated web page profiler',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/edx/harprofiler',
    keywords='web profiler automation har'.split(),
    license='Apache2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ]
)
