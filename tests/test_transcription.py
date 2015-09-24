#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import systranNlpApi
import systranNlpApi.configuration

class TranscriptionApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        systranNlpApi.configuration.load_api_key(api_key_file)
        self.api_client = systranNlpApi.ApiClient()
        self.transcription_api = systranNlpApi.TranscriptionApi(self.api_client)

    def test_transcription_supported_languages(self):
        result = self.transcription_api.nlp_transcription_supported_languages_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_transcription_transcribe(self):
        source = "en"
        target = 'ru'
        input = "Bodies from the MH17 crash are being kept on this train, as Natalia Antelava reports\n" \
                "Ceci est un test."
        result = self.transcription_api.nlp_transcription_transcribe_get(input=input, source=source, target=target)
        self.assertIsNotNone(result)
        output_file = os.path.join(os.path.dirname(__file__), "", "transcribe_output.txt")
        fo = open(output_file, "wb")
        fo.write(result)
        fo.close()
        print result

    def test_transcription_transcribe_with_input_file(self):
        source = "en"
        target = 'ru'
        input_file = os.path.join(os.path.dirname(__file__), "", "transcribe_input.txt")
        result = self.transcription_api.nlp_transcription_transcribe_get(input_file=input_file, source=source, target=target)
        self.assertIsNotNone(result)
        output_file = os.path.join(os.path.dirname(__file__), "", "transcribe_output.txt")
        fo = open(output_file, "wb")
        fo.write(result)
        fo.close()
        print result

if __name__ == '__main__':
    unittest.main()
