# Copyright 2003-2009, BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2

from zope.interface import implements
from agx.transform.xmi2uml.interfaces import IXMIFlavour

class XMI2_1(object):
    
    implements(IXMIFlavour)
    
    PROFILE = '{http://www.eclipse.org/uml2/3.0.0/UML}Profile'
    PACKAGED_ELEMENT = 'packagedElement'
    IMPORTED_ELEMENT = 'importedElement'
    OWNED_ATTRIBUTE = 'ownedAttribute'
    OWNED_OPERATION = 'ownedOperation'
    OWNED_PARAMETER = 'ownedParameter'
    OWNED_END = 'ownedEnd'
    GENERALIZATION = 'generalization'
    INTERFACE_REALIZATION = 'interfaceRealization'
    