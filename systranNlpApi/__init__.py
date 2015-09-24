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

# import models into sdk package
from .models.ner_entity import NerEntity
from .models.ner_extract_entities_response import NerExtractEntitiesResponse
from .models.ner_entity_annotation import NerEntityAnnotation
from .models.ner_segment_annotation import NerSegmentAnnotation
from .models.ner_extract_annotations_response import NerExtractAnnotationsResponse
from .models.lid_detected_language import LidDetectedLanguage
from .models.lid_document_response import LidDocumentResponse
from .models.lid_paragraph import LidParagraph
from .models.lid_paragraph_response import LidParagraphResponse
from .models.segmentation_segment_response import SegmentationSegmentResponse
from .models.segmentation_token import SegmentationToken
from .models.segmentation_tokenized_segment import SegmentationTokenizedSegment
from .models.segmentation_segment_and_tokenize_response import SegmentationSegmentAndTokenizeResponse
from .models.segmentation_tokenize_response import SegmentationTokenizeResponse
from .models.profile import Profile
from .models.supported_language import SupportedLanguage
from .models.supported_languages_response import SupportedLanguagesResponse
from .models.supported_language_pair import SupportedLanguagePair
from .models.transcription_supported_languages_response import TranscriptionSupportedLanguagesResponse
from .models.pos_annotation import PosAnnotation
from .models.morphology_extract_pos_response import MorphologyExtractPosResponse
from .models.lemma_annotation import LemmaAnnotation
from .models.morphology_extract_lemma_response import MorphologyExtractLemmaResponse
from .models.chunk_annotation import ChunkAnnotation
from .models.morphology_extract_np_response import MorphologyExtractNPResponse

# import apis into sdk package
from .apis.lid_api import LidApi
from .apis.morphology_api import MorphologyApi
from .apis.segmentation_api import SegmentationApi
from .apis.transcription_api import TranscriptionApi
from .apis.ner_api import NerApi

# import ApiClient
from .api_client import ApiClient
