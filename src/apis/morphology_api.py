#!/usr/bin/env python
# coding: utf-8

"""
Copyright 2015 SYSTRAN Software, Inc. All rights reserved.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from .. import configuration
from ..api_client import ApiClient

class MorphologyApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('https://api-platform.systran.net')
            self.api_client = configuration.api_client
    
    
    def nlp_morphology_extract_lemma_get(self, lang, **kwargs):
        """
        Get lemma
        Get the lemma for elements of an input text.\n

        :param str input: input text\n\n**Either `input` or `inputFile` is required**\n 
        :param File input_file: input text\n\n**Either `input` or `inputFile` is required**\n 
        :param str lang: Language code of the input ([details](#description_langage_code_values)) (required)
        :param int profile: Profile id\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: MorphologyExtractLemmaResponse
        """
        
        # verify the required parameter 'lang' is set
        if lang is None:
            raise ValueError("Missing the required parameter `lang` when calling `nlp_morphology_extract_lemma_get`")
        
        all_params = ['input', 'input_file', 'lang', 'profile', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method nlp_morphology_extract_lemma_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/nlp/morphology/extract/lemma'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'input' in params:
            query_params['input'] = params['input']
        
        if 'lang' in params:
            query_params['lang'] = params['lang']
        
        if 'profile' in params:
            query_params['profile'] = params['profile']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'input_file' in params:
            files['inputFile'] = params['input_file']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data', 'application/x-www-form-urlencoded', '*/*'])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='MorphologyExtractLemmaResponse', auth_settings=auth_settings)
        
        return response
        
    def nlp_morphology_extract_np_get(self, lang, **kwargs):
        """
        Get NP/chunks
        Get Noun-phrases and chunks from an input text.\n

        :param str input: input text\n\n**Either `input` or `inputFile` is required**\n 
        :param File input_file: input text\n\n**Either `input` or `inputFile` is required**\n 
        :param str lang: Language code of the input ([details](#description_langage_code_values)) (required)
        :param int profile: Profile id\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: MorphologyExtractNPResponse
        """
        
        # verify the required parameter 'lang' is set
        if lang is None:
            raise ValueError("Missing the required parameter `lang` when calling `nlp_morphology_extract_np_get`")
        
        all_params = ['input', 'input_file', 'lang', 'profile', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method nlp_morphology_extract_np_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/nlp/morphology/extract/np'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'input' in params:
            query_params['input'] = params['input']
        
        if 'lang' in params:
            query_params['lang'] = params['lang']
        
        if 'profile' in params:
            query_params['profile'] = params['profile']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'input_file' in params:
            files['inputFile'] = params['input_file']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data', 'application/x-www-form-urlencoded', '*/*'])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='MorphologyExtractNPResponse', auth_settings=auth_settings)
        
        return response
        
    def nlp_morphology_extract_pos_get(self, lang, **kwargs):
        """
        Get part of speech
        Get the part of speech for elements of an input text.\n

        :param str input: input text\n\n**Either `input` or `inputFile` is required**\n 
        :param File input_file: input text\n\n**Either `input` or `inputFile` is required**\n 
        :param str lang: Language code of the input ([details](#description_langage_code_values)) (required)
        :param int profile: Profile id\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: MorphologyExtractPosResponse
        """
        
        # verify the required parameter 'lang' is set
        if lang is None:
            raise ValueError("Missing the required parameter `lang` when calling `nlp_morphology_extract_pos_get`")
        
        all_params = ['input', 'input_file', 'lang', 'profile', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method nlp_morphology_extract_pos_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/nlp/morphology/extract/pos'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'input' in params:
            query_params['input'] = params['input']
        
        if 'lang' in params:
            query_params['lang'] = params['lang']
        
        if 'profile' in params:
            query_params['profile'] = params['profile']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'input_file' in params:
            files['inputFile'] = params['input_file']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data', 'application/x-www-form-urlencoded', '*/*'])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='MorphologyExtractPosResponse', auth_settings=auth_settings)
        
        return response
        
    def nlp_morphology_supported_languages_get(self, **kwargs):
        """
        Supported Languages
        List of languages pairs in which Morphological analysis is supported.

        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: SupportedLanguagesResponse
        """
        
        all_params = ['callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method nlp_morphology_supported_languages_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/nlp/morphology/supportedLanguages'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='SupportedLanguagesResponse', auth_settings=auth_settings)
        
        return response
        









