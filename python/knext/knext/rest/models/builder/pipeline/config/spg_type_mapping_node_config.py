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


class SpgTypeMappingNodeConfig(object):
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
    openapi_types = {
        "type": "str",
        "spg_type": "str",
        "mapping_filters": "list[MappingFilter]",
        "mapping_configs": "list[MappingConfig]",
        "subject_fusing_config": "BaseFusingConfig",
    }

    attribute_map = {
        "type": "type",
        "spg_type": "spgType",
        "mapping_filters": "mappingFilters",
        "mapping_configs": "mappingConfigs",
        "subject_fusing_config": "subjectFusingConfig",
    }

    def __init__(
        self,
        type="SPG_TYPE_MAPPING",
        spg_type=None,
        mapping_filters=None,
        mapping_configs=None,
        subject_fusing_config=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """SpgTypeMappingNodeConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._spg_type = None
        self._mapping_filters = None
        self._mapping_configs = None
        self._subject_fusing_config = None
        self.discriminator = type

        self.type = type
        if spg_type is not None:
            self.spg_type = spg_type
        if mapping_filters is not None:
            self.mapping_filters = mapping_filters
        if mapping_configs is not None:
            self.mapping_configs = mapping_configs
        if subject_fusing_config is not None:
            self.subject_fusing_config = subject_fusing_config

    @property
    def type(self):
        """Gets the type of this SpgTypeMappingNodeConfig.  # noqa: E501


        :return: The type of this SpgTypeMappingNodeConfig.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SpgTypeMappingNodeConfig.


        :param type: The type of this SpgTypeMappingNodeConfig.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "CSV_SOURCE",
            "SPG_TYPE_MAPPING",
            "RELATION_MAPPING",
            "SUBGRAPH_MAPPING",
            "USER_DEFINED_EXTRACT",
            "LLM_BASED_EXTRACT",
            "GRAPH_SINK",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def spg_type(self):
        """Gets the spg_type of this SpgTypeMappingNodeConfig.  # noqa: E501


        :return: The spg_type of this SpgTypeMappingNodeConfig.  # noqa: E501
        :rtype: str
        """
        return self._spg_type

    @spg_type.setter
    def spg_type(self, spg_type):
        """Sets the spg_type of this SpgTypeMappingNodeConfig.


        :param spg_type: The spg_type of this SpgTypeMappingNodeConfig.  # noqa: E501
        :type: str
        """

        self._spg_type = spg_type

    @property
    def mapping_filters(self):
        """Gets the mapping_filters of this SpgTypeMappingNodeConfig.  # noqa: E501


        :return: The mapping_filters of this SpgTypeMappingNodeConfig.  # noqa: E501
        :rtype: list[MappingFilter]
        """
        return self._mapping_filters

    @mapping_filters.setter
    def mapping_filters(self, mapping_filters):
        """Sets the mapping_filters of this SpgTypeMappingNodeConfig.


        :param mapping_filters: The mapping_filters of this SpgTypeMappingNodeConfig.  # noqa: E501
        :type: list[MappingFilter]
        """

        self._mapping_filters = mapping_filters

    @property
    def mapping_configs(self):
        """Gets the mapping_configs of this SpgTypeMappingNodeConfig.  # noqa: E501


        :return: The mapping_configs of this SpgTypeMappingNodeConfig.  # noqa: E501
        :rtype: list[MappingConfig]
        """
        return self._mapping_configs

    @mapping_configs.setter
    def mapping_configs(self, mapping_configs):
        """Sets the mapping_configs of this SpgTypeMappingNodeConfig.


        :param mapping_configs: The mapping_configs of this SpgTypeMappingNodeConfig.  # noqa: E501
        :type: list[MappingConfig]
        """

        self._mapping_configs = mapping_configs

    @property
    def subject_fusing_config(self):
        """Gets the subject_fusing_config of this SpgTypeMappingNodeConfig.  # noqa: E501


        :return: The subject_fusing_config of this SpgTypeMappingNodeConfig.  # noqa: E501
        :rtype: BaseFusingConfig
        """
        return self._subject_fusing_config

    @subject_fusing_config.setter
    def subject_fusing_config(self, subject_fusing_config):
        """Sets the subject_fusing_config of this SpgTypeMappingNodeConfig.


        :param subject_fusing_config: The subject_fusing_config of this SpgTypeMappingNodeConfig.  # noqa: E501
        :type: BaseFusingConfig
        """

        self._subject_fusing_config = subject_fusing_config

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
        if not isinstance(other, SpgTypeMappingNodeConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpgTypeMappingNodeConfig):
            return True

        return self.to_dict() != other.to_dict()
