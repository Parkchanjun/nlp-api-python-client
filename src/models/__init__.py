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

# import models into model package
from .ner_entity import NerEntity
from .ner_extract_entities_response import NerExtractEntitiesResponse
from .ner_entity_annotation import NerEntityAnnotation
from .ner_segment_annotation import NerSegmentAnnotation
from .ner_extract_annotations_response import NerExtractAnnotationsResponse
from .lid_detected_language import LidDetectedLanguage
from .lid_document_response import LidDocumentResponse
from .lid_paragraph import LidParagraph
from .lid_paragraph_response import LidParagraphResponse
from .segmentation_segment_response import SegmentationSegmentResponse
from .segmentation_token import SegmentationToken
from .segmentation_tokenized_segment import SegmentationTokenizedSegment
from .segmentation_segment_and_tokenize_response import SegmentationSegmentAndTokenizeResponse
from .segmentation_tokenize_response import SegmentationTokenizeResponse
from .profile import Profile
from .supported_language import SupportedLanguage
from .supported_languages_response import SupportedLanguagesResponse
from .supported_language_pair import SupportedLanguagePair
from .transcription_supported_languages_response import TranscriptionSupportedLanguagesResponse

