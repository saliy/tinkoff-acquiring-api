# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
from __future__ import annotations

import unittest


class ApiTest(unittest.TestCase):
    def test_fake(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
