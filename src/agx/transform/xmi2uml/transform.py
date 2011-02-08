# Copyright BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2

import os
from zope.interface import implements
from zope.interface import alsoProvides
from zope.component import getUtility
from zope.component import getUtilitiesFor
from node.interfaces import IRoot
from agx.core.interfaces import ITransform
from agx.core.interfaces import ISource
from agx.core.interfaces import ITarget
from agx.core.interfaces import IProfileLocation
from node.ext.xmi import XMINode
from node.ext.uml.core import Model
import flavours

import logging
log = logging.getLogger('agx.transform.xmi2uml')

class UMLFactory(object):
    
    def __call__(self, paths):
        xmi = XMINode('xmi', paths)
        xmi.xmi = flavours.XMI2_1
        return xmi

class XMI2UML(object):
    """XMI to UML source and target factory.
    """
    
    implements(ITransform)
    
    def __init__(self, name):
        self.name = name
        self.XMI = None
    
    def source(self, path):
        if len(path) == 1:
            locations = [loc for name, loc in getUtilitiesFor(IProfileLocation)]
            profiles = list()
            for location in locations:
                directory = os.path.dirname(location.package.__file__)
                profiles.append('%s/profiles/%s' % (directory, location.name))
            path = profiles + path
        factory = UMLFactory()
        xmi = UMLFactory()(path)
        alsoProvides(xmi, IRoot)
        alsoProvides(xmi, ISource)
        return xmi
    
    def target(self, path):
        uml = Model(name=path)
        alsoProvides(uml, IRoot)
        alsoProvides(uml, ITarget)
        return uml