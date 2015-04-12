# coding:utf-8

import gdutAvatar
import unittest
import sys

class GdutFlaskTestCase(unittest.TestCase):

    def setUp(self):
        gdutAvatar.app.config['TESTING'] = True
        self.app = gdutAvatar.app.test_client()

    def tearDown(self):
        pass

    def test_isValidSno(self):
        rv = self.isValidSno('31130263862')
        assert '学号格式不正确' in rv.data
        rv = self.isValidSno('3100006386')
        assert '学号格式不正确' in rv.data
        rv = self.isValidSno('3100026386')
        assert '学号格式不正确' in rv.data
        rv = self.isValidSno('2100026386')
        assert '学号格式不正确' in rv.data
        rv = self.isValidSno('3113006386')
        assert '格式正确' in rv.data

    def isValidSno(self, sno):
        return self.app.post('/', data=dict(
            sno = sno
        ), follow_redirects = True)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    unittest.main()
