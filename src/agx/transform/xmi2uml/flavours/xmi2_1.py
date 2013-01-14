from zope.interface import implementer
from agx.transform.xmi2uml.interfaces import IXMIFlavour


@implementer(IXMIFlavour)
class XMI2_1(object):
    PROFILE = '{http://www.eclipse.org/uml2/3.0.0/UML}Profile'
    PACKAGED_ELEMENT = 'packagedElement'
    IMPORTED_ELEMENT = 'importedElement'
    OWNED_ATTRIBUTE = 'ownedAttribute'
    OWNED_OPERATION = 'ownedOperation'
    OWNED_PARAMETER = 'ownedParameter'
    OWNED_END = 'ownedEnd'
    GENERALIZATION = 'generalization'
    INTERFACE_REALIZATION = 'interfaceRealization'
