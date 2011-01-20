
XML to UML Transform
====================

lookup Transform and read source and target.

  >>> import os
  >>> modelpath = os.path.sep.join([datadir, 'examplegg.uml'])
  >>> profilepath = os.path.sep.join([datadir, 'pyegg.profile.uml'])

  >>> from agx.core.interfaces import ITransform
  >>> from zope.component import getUtility
  >>> transform = getUtility(ITransform, name="xmi2uml")
  >>> xmi = transform.source([modelpath, profilepath])
  >>> xmi
  <XMINode object '...' at ...>
  
  >>> xmi.values()
  [<XMLNode object '.../examplegg.uml' at ...>, 
  <XMLNode object '.../pyegg.profile.uml' at ...>]
  
  >>> xmlmodel = xmi.values()[0].values()[0]
  >>> xmlmodel
  <XMLNode object '...:{http://schema.omg.org/spec/XMI/2.1}XMI' at ...>
  
  >>> xmi.values()[0]['XMI']
  <XMLNode object '...:{http://schema.omg.org/spec/XMI/2.1}XMI' at ...>
  
  >>> xmlprofile = xmi.values()[1].values()[0]
  >>> xmlprofile
  <XMLNode object '...:{http://www.eclipse.org/uml2/3.0.0/UML}Profile' at ...>
  
  >>> from agx.core import Processor
  >>> processor = Processor('xmi2uml')
  >>> processor(xmi, transform.target('Model'))
  <Model object 'Model' at ...>