# coding: utf-8
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.


"""
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from knext.rest.configuration import Configuration


class DefineDynamicTaxonomyRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"concept_type_name": "str", "concept_name": "str", "dsl": "str"}

    attribute_map = {
        "concept_type_name": "conceptTypeName",
        "concept_name": "conceptName",
        "dsl": "dsl",
    }

    def __init__(
        self,
        concept_type_name=None,
        concept_name=None,
        dsl=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """DefineDynamicTaxonomyRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._concept_type_name = None
        self._concept_name = None
        self._dsl = None
        self.discriminator = None

        if concept_type_name is not None:
            self.concept_type_name = concept_type_name
        if concept_name is not None:
            self.concept_name = concept_name
        if dsl is not None:
            self.dsl = dsl

    @property
    def concept_type_name(self):
        """Gets the concept_type_name of this DefineDynamicTaxonomyRequest.  # noqa: E501


        :return: The concept_type_name of this DefineDynamicTaxonomyRequest.  # noqa: E501
        :rtype: str
        """
        return self._concept_type_name

    @concept_type_name.setter
    def concept_type_name(self, concept_type_name):
        """Sets the concept_type_name of this DefineDynamicTaxonomyRequest.


        :param concept_type_name: The concept_type_name of this DefineDynamicTaxonomyRequest.  # noqa: E501
        :type: str
        """

        self._concept_type_name = concept_type_name

    @property
    def concept_name(self):
        """Gets the concept_name of this DefineDynamicTaxonomyRequest.  # noqa: E501


        :return: The concept_name of this DefineDynamicTaxonomyRequest.  # noqa: E501
        :rtype: str
        """
        return self._concept_name

    @concept_name.setter
    def concept_name(self, concept_name):
        """Sets the concept_name of this DefineDynamicTaxonomyRequest.


        :param concept_name: The concept_name of this DefineDynamicTaxonomyRequest.  # noqa: E501
        :type: str
        """

        self._concept_name = concept_name

    @property
    def dsl(self):
        """Gets the dsl of this DefineDynamicTaxonomyRequest.  # noqa: E501


        :return: The dsl of this DefineDynamicTaxonomyRequest.  # noqa: E501
        :rtype: str
        """
        return self._dsl

    @dsl.setter
    def dsl(self, dsl):
        """Sets the dsl of this DefineDynamicTaxonomyRequest.


        :param dsl: The dsl of this DefineDynamicTaxonomyRequest.  # noqa: E501
        :type: str
        """

        self._dsl = dsl

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DefineDynamicTaxonomyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DefineDynamicTaxonomyRequest):
            return True

        return self.to_dict() != other.to_dict()
