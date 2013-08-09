# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.group.type.announcement',
    version=version,
    description="Support for announcement groups in GroupServer",
    long_description=open("README.txt").read() + "\n" +
                    open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Zope Public License',
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='user, group, page',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://groupserver.org',
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.group', 'gs.group.type', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.cachedescriptors',
        'zope.component',
        'gs.content.js.jquery.base',
        'gs.group.home',
        'gs.group.member.canpost',
        'gs.group.messages.base',
        'gs.group.type.discussion',
        'Products.GSGroup',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
