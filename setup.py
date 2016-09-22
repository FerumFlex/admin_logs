import os
from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(name='admin_logs',
    version=".".join(map(str, __import__("admin_logs").__version__)),
    description='Admin logs for django like in Google Application Engine',
    long_description=(read('README.rst')),
    author='Anton Pomeschenko',
    license='MIT',
    url='https://github.com/FerumFlex/admin_logs',
    author_email='ferumflex@gmail.com',
    packages=find_packages(exclude=['admin_logs_app']),
    package_data={'admin_logs': ['templates/admin_logs/*.*', 'static/js/admin_logs/*.*',
                                 'static/images/admin_logs/*.*', 'static/css/admin_logs/*.*']},
    install_requires=['django-picklefield', 'celery>=3.1.15', 'django-celery>=3.1.15', 'Django>=1.7'],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Framework :: Django",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
    ],
)