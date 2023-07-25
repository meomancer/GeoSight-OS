# coding=utf-8
"""
GeoSight is UNICEF's geospatial web-based business intelligence platform.

Contact : geosight-no-reply@unicef.org

.. note:: This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    (at your option) any later version.

"""
__author__ = 'irwan@kartoza.com'
__date__ = '13/06/2023'
__copyright__ = ('Copyright 2023, Unicef')

from rest_framework import serializers

from geosight.data.models.code import Code, CodeList


class CodeSerializer(serializers.ModelSerializer):
    """Serializer for Code."""

    value = serializers.SerializerMethodField()

    def get_value(self, obj: Code):
        """Return value."""
        return obj.id

    class Meta:  # noqa: D106
        model = Code
        fields = ('id', 'value', 'label', 'code')


class CodeListSerializer(serializers.ModelSerializer):
    """Serializer for Code."""

    codes = serializers.SerializerMethodField()

    def get_codes(self, obj: CodeList):
        """Codes."""
        return obj.codes

    class Meta:  # noqa: D106
        model = CodeList
        fields = '__all__'
