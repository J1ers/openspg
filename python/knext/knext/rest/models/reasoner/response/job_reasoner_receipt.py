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


class JobReasonerReceipt(object):
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
        "reasoner_job_info_id": "int",
        "reasoner_job_inst_id": "int",
        "receipt_type": "str",
    }

    attribute_map = {
        "reasoner_job_info_id": "reasonerJobInfoId",
        "reasoner_job_inst_id": "reasonerJobInstId",
        "receipt_type": "receiptType",
    }

    def __init__(
        self,
        reasoner_job_info_id=None,
        reasoner_job_inst_id=None,
        receipt_type="JOB",
        local_vars_configuration=None,
    ):  # noqa: E501
        """JobReasonerReceipt - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._reasoner_job_info_id = None
        self._reasoner_job_inst_id = None
        self._receipt_type = None
        self.discriminator = receipt_type

        if reasoner_job_info_id is not None:
            self.reasoner_job_info_id = reasoner_job_info_id
        if reasoner_job_inst_id is not None:
            self.reasoner_job_inst_id = reasoner_job_inst_id
        self.receipt_type = receipt_type

    @property
    def reasoner_job_info_id(self):
        """Gets the reasoner_job_info_id of this JobReasonerReceipt.  # noqa: E501


        :return: The reasoner_job_info_id of this JobReasonerReceipt.  # noqa: E501
        :rtype: int
        """
        return self._reasoner_job_info_id

    @reasoner_job_info_id.setter
    def reasoner_job_info_id(self, reasoner_job_info_id):
        """Sets the reasoner_job_info_id of this JobReasonerReceipt.


        :param reasoner_job_info_id: The reasoner_job_info_id of this JobReasonerReceipt.  # noqa: E501
        :type: int
        """

        self._reasoner_job_info_id = reasoner_job_info_id

    @property
    def reasoner_job_inst_id(self):
        """Gets the reasoner_job_inst_id of this JobReasonerReceipt.  # noqa: E501


        :return: The reasoner_job_inst_id of this JobReasonerReceipt.  # noqa: E501
        :rtype: int
        """
        return self._reasoner_job_inst_id

    @reasoner_job_inst_id.setter
    def reasoner_job_inst_id(self, reasoner_job_inst_id):
        """Sets the reasoner_job_inst_id of this JobReasonerReceipt.


        :param reasoner_job_inst_id: The reasoner_job_inst_id of this JobReasonerReceipt.  # noqa: E501
        :type: int
        """

        self._reasoner_job_inst_id = reasoner_job_inst_id

    @property
    def receipt_type(self):
        """Gets the receipt_type of this JobReasonerReceipt.  # noqa: E501


        :return: The receipt_type of this JobReasonerReceipt.  # noqa: E501
        :rtype: str
        """
        return self._receipt_type

    @receipt_type.setter
    def receipt_type(self, receipt_type):
        """Sets the receipt_type of this JobReasonerReceipt.


        :param receipt_type: The receipt_type of this JobReasonerReceipt.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and receipt_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `receipt_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["TABLE", "JOB"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and receipt_type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `receipt_type` ({0}), must be one of {1}".format(  # noqa: E501
                    receipt_type, allowed_values
                )
            )

        self._receipt_type = receipt_type

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
        if not isinstance(other, JobReasonerReceipt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobReasonerReceipt):
            return True

        return self.to_dict() != other.to_dict()
