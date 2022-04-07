import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='django-sweet-autocomplete',
    version='1.0.2',
    package_dir={'': 'src'},
    packages=['sweetautocomplete'],
    license='MIT',
    description='Simplify autocomplete functionalities implementation in your Django project.',
    keywords='django autocomplete',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Klemen Kubelj',
    author_email='klemen.kubelj@gmail.com',
    url='https://github.com/kubeljk/django-sweet-autocomplete',
    install_requires=[
        'django>=2.2',
        'psycopg2',
        'djangorestframework'
    ],
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
