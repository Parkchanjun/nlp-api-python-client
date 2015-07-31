#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import src
import src.configuration

class LidApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        src.configuration.load_api_key(api_key_file)
        self.api_client = src.ApiClient()
        self.lid_api = src.LidApi(self.api_client)

    def test_lid_document(self):
        input = "Bodies from the MH17 crash are being kept on this train, as Natalia Antelava reports Pro-Russian rebels have allowed Dutch investigators to examine bodies from the crashed Malaysia Airlines plane at a railway station in eastern Ukraine."
        result = self.lid_api.nlp_lid_detect_language_document_get(input=input)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_lid_document_with_file(self):
        input_file = os.path.join(os.path.dirname(__file__), "", "lid_document.txt")
        result = self.lid_api.nlp_lid_detect_language_document_get(input_file=input_file)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_lid_paragraph(self):
        input = "Bodies from the MH17 crash are being kept on this train, as Natalia Antelava reports\n" \
                "Ceci est un test."
        result = self.lid_api.nlp_lid_detect_language_paragraph_get(input=input)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_lid_paragraph_with_file(self):
        input_file = os.path.join(os.path.dirname(__file__), "", "lid_paragraph.txt")
        result = self.lid_api.nlp_lid_detect_language_paragraph_get(input_file=input_file)
        self.assertIsNotNone(result)
        print result.__repr__()

if __name__ == '__main__':
    unittest.main()
