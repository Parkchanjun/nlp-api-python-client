#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import src
import src.configuration

class MorphologyApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        src.configuration.load_api_key(api_key_file)
        self.api_client = src.ApiClient()
        self.morphology_api = src.MorphologyApi(self.api_client)

    def test_morphology_supported_languages_get(self):
        result = self.morphology_api.nlp_morphology_supported_languages_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_morphology_extract_lemma_get(self):
        lang = "en"
        input = "This is a test."
        result = self.morphology_api.nlp_morphology_extract_lemma_get(input=input, lang=lang)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_morphology_extract_lemma_get_with_file(self):
        lang = "en"
        input_file = os.path.join(os.path.dirname(__file__), "", "morphology_input.txt")
        result = self.morphology_api.nlp_morphology_extract_lemma_get(input_file=input_file, lang=lang)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_morphology_extract_np_get(self):
        lang = "en"
        input = "This is a test."
        result = self.morphology_api.nlp_morphology_extract_np_get(input=input, lang=lang)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_morphology_extract_np_get_with_file(self):
        lang = "en"
        input_file = os.path.join(os.path.dirname(__file__), "", "morphology_input.txt")
        result = self.morphology_api.nlp_morphology_extract_np_get(input_file=input_file, lang=lang)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_morphology_extract_pos_get(self):
        lang = "en"
        input = "This is a test."
        result = self.morphology_api.nlp_morphology_extract_pos_get(input=input, lang=lang)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_morphology_extract_pos_get_with_file(self):
        lang = "en"
        input_file = os.path.join(os.path.dirname(__file__), "", "morphology_input.txt")
        result = self.morphology_api.nlp_morphology_extract_pos_get(input_file=input_file, lang=lang)
        self.assertIsNotNone(result)
        print result.__repr__()

if __name__ == '__main__':
    unittest.main()
