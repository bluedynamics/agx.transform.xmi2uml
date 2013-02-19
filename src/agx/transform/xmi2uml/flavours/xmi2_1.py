from zope.interface import implementer
from agx.transform.xmi2uml.interfaces import IXMIFlavour


@implementer(IXMIFlavour)
class XMI2_1(object):
    PROFILE = '{http://www.eclipse.org/uml2/3.0.0/UML}Profile'
    PROFILES=[PROFILE,'{http://www.eclipse.org/uml2/4.0.0/UML}Profile'] #alternatives
    PACKAGED_ELEMENT = 'packagedElement'
    IMPORTED_ELEMENT = 'importedElement'
    OWNED_ATTRIBUTE = 'ownedAttribute'
    OWNED_OPERATION = 'ownedOperation'
    OWNED_PARAMETER = 'ownedParameter'
    OWNED_END = 'ownedEnd'
    GENERALIZATION = 'generalization'
    INTERFACE_REALIZATION = 'interfaceRealization'

    @classmethod
    def is_profile(self, tag):
        """checks wether a tag name represents an UML profile"""
        for prof in self.PROFILES:
            if tag.endswith(prof):
                return True
        
        return False
