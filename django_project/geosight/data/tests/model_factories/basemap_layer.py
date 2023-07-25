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

import factory

from geosight.data.models.basemap_layer import (
    BasemapLayer, BasemapLayerParameter
)


class BasemapLayerF(factory.django.DjangoModelFactory):
    """Factory for BasemapLayer."""

    name = factory.Sequence(lambda n: 'Basemap Layer {}'.format(n))

    class Meta:  # noqa: D106
        model = BasemapLayer


class BasemapLayerParameterF(factory.django.DjangoModelFactory):
    """Factory for BasemapLayerParameter."""

    basemap_layer = factory.SubFactory(BasemapLayerF)
    name = factory.Sequence(lambda n: 'Param {}'.format(n))

    class Meta:  # noqa: D106
        model = BasemapLayerParameter
