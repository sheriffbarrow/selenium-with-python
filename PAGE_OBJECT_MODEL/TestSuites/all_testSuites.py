from PAGE_OBJECT_MODEL.test.testcasehome import LoginTest

import unittest

login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)


sanity = unittest.TestSuite([login])
unittest.TextTestRunner(verbosity=2).run(sanity)

