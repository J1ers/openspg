# -*- coding: utf-8 -*-
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

# ATTENTION!
# This file is generated by Schema automatically, it will be refreshed after schema has been committed
# PLEASE DO NOT MODIFY THIS FILE!!!
#

from knext.common.schema_helper import SPGTypeHelper, PropertyHelper, RelationHelper


class Finance:
    class Indicator(SPGTypeHelper):

        name = PropertyHelper("name")
        id = PropertyHelper("id")
        stdId = PropertyHelper("stdId")
        alias = PropertyHelper("alias")
        description = PropertyHelper("description")

    class IndicatorEvent(SPGTypeHelper):

        name = PropertyHelper("name")
        id = PropertyHelper("id")
        eventTime = PropertyHelper("eventTime")
        value = PropertyHelper("value")
        date = PropertyHelper("date")
        subject = PropertyHelper("subject")
        trend = PropertyHelper("trend")
        description = PropertyHelper("description")

    Indicator = Indicator("Finance.Indicator")
    IndicatorEvent = IndicatorEvent("Finance.IndicatorEvent")

    pass
