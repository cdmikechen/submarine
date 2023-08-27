# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Submarine API

    The Submarine REST API allows you to access Submarine resources such as,  experiments, environments and notebooks. The  API is hosted under the /v1 path on the Submarine server. For example,  to list experiments on a server hosted at http://localhost:8080, access http://localhost:8080/api/v1/experiment/  # noqa: E501

    The version of the OpenAPI document: 0.8.0-RC0
    Contact: dev@submarine.apache.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from submarine.client.configuration import Configuration


class RegisteredModelEntity(object):
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
        'creation_time': 'datetime',
        'description': 'str',
        'last_updated_time': 'datetime',
        'model_id': 'int',
        'name': 'str',
        'tags': 'list[str]',
    }

    attribute_map = {
        'creation_time': 'creationTime',
        'description': 'description',
        'last_updated_time': 'lastUpdatedTime',
        'model_id': 'modelId',
        'name': 'name',
        'tags': 'tags',
    }

    def __init__(
        self,
        creation_time=None,
        description=None,
        last_updated_time=None,
        model_id=None,
        name=None,
        tags=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """RegisteredModelEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._creation_time = None
        self._description = None
        self._last_updated_time = None
        self._model_id = None
        self._name = None
        self._tags = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if last_updated_time is not None:
            self.last_updated_time = last_updated_time
        if model_id is not None:
            self.model_id = model_id
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags

    @property
    def creation_time(self):
        """Gets the creation_time of this RegisteredModelEntity.  # noqa: E501


        :return: The creation_time of this RegisteredModelEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this RegisteredModelEntity.


        :param creation_time: The creation_time of this RegisteredModelEntity.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this RegisteredModelEntity.  # noqa: E501


        :return: The description of this RegisteredModelEntity.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RegisteredModelEntity.


        :param description: The description of this RegisteredModelEntity.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def last_updated_time(self):
        """Gets the last_updated_time of this RegisteredModelEntity.  # noqa: E501


        :return: The last_updated_time of this RegisteredModelEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time):
        """Sets the last_updated_time of this RegisteredModelEntity.


        :param last_updated_time: The last_updated_time of this RegisteredModelEntity.  # noqa: E501
        :type: datetime
        """

        self._last_updated_time = last_updated_time

    @property
    def model_id(self):
        """Gets the model_id of this RegisteredModelEntity.  # noqa: E501


        :return: The model_id of this RegisteredModelEntity.  # noqa: E501
        :rtype: int
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this RegisteredModelEntity.


        :param model_id: The model_id of this RegisteredModelEntity.  # noqa: E501
        :type: int
        """

        self._model_id = model_id

    @property
    def name(self):
        """Gets the name of this RegisteredModelEntity.  # noqa: E501


        :return: The name of this RegisteredModelEntity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RegisteredModelEntity.


        :param name: The name of this RegisteredModelEntity.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this RegisteredModelEntity.  # noqa: E501


        :return: The tags of this RegisteredModelEntity.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RegisteredModelEntity.


        :param tags: The tags of this RegisteredModelEntity.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
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
        if not isinstance(other, RegisteredModelEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegisteredModelEntity):
            return True

        return self.to_dict() != other.to_dict()
