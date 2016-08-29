# -*- coding: utf-8 -*-

import sys
import json
import unittest
from StringIO import StringIO
from cli import parser

class YAMLParserTestCase(unittest.TestCase):
    def setUp(self):
        # redirect log.error to stringio
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_initialize(self):
        with self.assertRaises(IOError):
            parser.YAMLParser("./unknown_template.yaml")
            self.assertEqual(sys.stdout.getvalue(), 'initialize failed, cause template ./unknown_template.yaml is not found')

        yp = parser.YAMLParser("./tests/data/test.yaml")
        self.assertEqual(yp.template.get("mail-to"), "test@shujutang.com")

    def test_read(self):
        yp = parser.YAMLParser("./tests/data/test.yaml")
        result_as_json = yp.read("./tests/data/test.yaml")
        result = json.loads(result_as_json)
        self.assertEqual(result.get("mail-to"), "test@shujutang.com")
        
