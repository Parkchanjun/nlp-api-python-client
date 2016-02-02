#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import systran_nlp_api
import systran_nlp_api.configuration

class NerApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        systran_nlp_api.configuration.load_api_key(api_key_file)
        self.api_client = systran_nlp_api.ApiClient()
        self.ner_api = systran_nlp_api.NerApi(self.api_client)

    def test_ner_extract_entity(self):
        lang = "en"
        input = "Bodies from the MH17 crash are being kept on this train, as Natalia Antelava reports\n" \
                "Pro-Russian rebels have allowed Dutch investigators to examine bodies from the crashed Malaysia Airlines plane at a railway station in eastern Ukraine.\n" \
                "The three Dutch experts said the train might leave the town of Torez later.\n" \
                "All 298 people on board flight MH17 died when it crashed over the rebel-held area on 17 July. The US and other nations say there is growing evidence of Russian complicity in the crash."
        result = self.ner_api.nlp_ner_extract_entities_get(lang=lang, input=input)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_lid_extract_entity_with_file(self):
        lang = "en"
        input_file = os.path.join(os.path.dirname(__file__), "", "ner_extraction.txt")
        result = self.ner_api.nlp_ner_extract_entities_get(lang=lang, input_file=input_file)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_ner_extract_annotation(self):
        lang = "en"
        input = "Bodies from the MH17 crash are being kept on this train, as Natalia Antelava reports\n" \
                "Pro-Russian rebels have allowed Dutch investigators to examine bodies from the crashed Malaysia Airlines plane at a railway station in eastern Ukraine.\n" \
                "The three Dutch experts said the train might leave the town of Torez later.\n" \
                "All 298 people on board flight MH17 died when it crashed over the rebel-held area on 17 July. The US and other nations say there is growing evidence of Russian complicity in the crash."
        result = self.ner_api.nlp_ner_extract_annotations_get(lang=lang, input=input)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_lid_extract_annotation_with_file(self):
        lang = "en"
        input_file = os.path.join(os.path.dirname(__file__), "", "ner_extraction.txt")
        result = self.ner_api.nlp_ner_extract_annotations_get(lang=lang, input_file=input_file)
        self.assertIsNotNone(result)
        print result.__repr__()

if __name__ == '__main__':
    unittest.main()
