from zope.component import provideUtility
from agx.core.interfaces import IScope
from agx.core.metaconfigure import _chkregistered
from scope import (
    XMIScope,
    StereotypeScope,
)


def registerXMIScope(name, transform, tags, type, class_=XMIScope):
    name = '%s.%s' % (transform, name)
    _chkregistered(IScope, name=name)
    scope = class_(name, tags, type)
    provideUtility(scope, provides=IScope, name=name)


def registerStereotypeScope(name, transform, class_=StereotypeScope):
    name = '%s.%s' % (transform, name)
    _chkregistered(IScope, name=name)
    scope = class_()
    provideUtility(scope, provides=IScope, name=name)
