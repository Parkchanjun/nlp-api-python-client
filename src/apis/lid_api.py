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

class LidApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('https://platformapi-stag.systran.net:8904')
            self.api_client = configuration.api_client
    
    
    def nlp_lid_detect_language_document_get(self, **kwargs):
        """
        Document language detection\n
        Global language detection on document.\n

        :param File input_file: input text\n\n**Either `input` or `inputFile` is required**\n 
        :param str input: input text\n\n**Either `input` or `inputFile` is required**\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: LidDocumentResponse
        """
        
        all_params = ['input_file', 'input', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method nlp_lid_detect_language_document_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/nlp/lid/detectLanguage/document'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'input' in params:
            query_params['input'] = params['input']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'input_file' in params:
            files['inputFile'] = params['input_file']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data', 'application/x-www-form-urlencoded', '*/*'])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='LidDocumentResponse', auth_settings=auth_settings)
        
        return response
        
    def nlp_lid_detect_language_paragraph_get(self, **kwargs):
        """
        Paragraph language detection\n
        Language detection for each paragraph in a document.\n

        :param File input_file: input text\n\n**Either `input` or `inputFile` is required**\n 
        :param str input: input text\n\n**Either `input` or `inputFile` is required**\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: LidParagraphResponse
        """
        
        all_params = ['input_file', 'input', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method nlp_lid_detect_language_paragraph_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/nlp/lid/detectLanguage/paragraph'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'input' in params:
            query_params['input'] = params['input']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'input_file' in params:
            files['inputFile'] = params['input_file']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data', 'application/x-www-form-urlencoded', '*/*'])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='LidParagraphResponse', auth_settings=auth_settings)
        
        return response
        









