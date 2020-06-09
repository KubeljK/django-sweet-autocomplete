import os
from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='django-sweet-autocomplete',
    version='0.0.3',
    package_dir={'': 'src'},
    packages=['sweetautocomplete'],
    include_package_data=True,
    license='MIT',
    description='Simplify autocomplete functionalities implementation in your Django project.',
    keywords='django autocomplete',
    long_description=README,
    author='Klemen Kubelj',
    author_email='klemen.kubelj@gmail.com',
    url='https://github.com/kubeljk/django-sweet-autocomplete',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: MIT License',
    ],
)
