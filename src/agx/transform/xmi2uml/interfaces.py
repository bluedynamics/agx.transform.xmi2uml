from zope.interface import Interface


class IXMIFlavour(Interface):
    """Holds all information relevant to the different flavors of XMI, such as 
    its version or exporter specific stuff.
    """
