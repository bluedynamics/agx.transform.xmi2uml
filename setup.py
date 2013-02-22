import os
from setuptools import (
    setup,
    find_packages,
)


version = '1.0a1'
shortdesc = "AGX XMI to UML Transform"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()


setup(name='agx.transform.xmi2uml',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Programming Language :: Python',    
      ],
      keywords='AGX, Code Generator',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url=u'http://github.com/bluedynamics/agx.transform.xmi2uml',
      license='GNU General Public Licence',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['agx', 'agx.transform'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'agx.core',
          'node.ext.xmi',
          'node.ext.uml',
      ],
      extras_require = dict(
          test=[
            'interlude',
          ]
      ),
      entry_points="""
      # -*- Entry points: -*-
      """)
