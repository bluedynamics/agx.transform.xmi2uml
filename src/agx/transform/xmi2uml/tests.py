import os
import unittest
import doctest
import zope.component
from pprint import pprint
from interlude import interact
from zope.configuration.xmlconfig import XMLConfig
import agx.core
import agx.transform.xmi2uml


optionflags = doctest.NORMALIZE_WHITESPACE | \
              doctest.ELLIPSIS | \
              doctest.REPORT_ONLY_FIRST_FAILURE


TESTFILES = [
    'transform.rst',
]


datadir = os.path.join(os.path.dirname(__file__), 'testing', 'data')


def test_suite():
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('configure.zcml', agx.transform.xmi2uml)()
    return unittest.TestSuite([
        doctest.DocFileSuite(
            file,
            optionflags=optionflags,
            globs={'interact': interact,
                   'pprint': pprint,
                   'datadir': datadir,},
        ) for file in TESTFILES
    ])


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite') 
