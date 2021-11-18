import os
import sys
from distutils.sysconfig import get_python_lib
from setuptools import setup, find_packages
from xenlib.cli import __version__

overlay_warning = False
if "install" in sys.argv:
    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib/"):
        # We have to try also with an explicit prefix of /usr/local in order to
        # catch Debian's custom user site-packages directory.
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        existing_path = os.path.abspath(os.path.join(lib_path, "xen"))
        if os.path.exists(existing_path):
            # We note the need for the warning here, but present it after the
            # command is run, so it's more likely to be seen.
            overlay_warning = True
            break

setup (
    name='xen',
    version=__version__,
    url='http://xentinel.id',
    author='Xen Client Tools',
    license='MIT',
    packages=find_packages(),
    description=('Xen Client Tools is a developer project management tool'),
    long_description = open('README.rst').read(),
    include_package_data=True,
    scripts=['xen.py'],
    entry_points={'console_scripts': [
        'xen = xenlib.cli:cli',
    ]},
    install_requires=[
       'Werkzeug',
       'itsdangerous',
       'click',
       'Jinja2',
       'GitPython'
	],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

if overlay_warning:
    sys.stderr.write("""
========
WARNING!
========
You have just installed xen over top of an existing
installation, without removing it first. Because of this,
your install may now include extraneous files from a
previous version that have since been removed from
Django. This is known to cause a variety of problems. You
should manually remove the
%(existing_path)s
directory and re-install xen.
""" % {"existing_path": existing_path})
