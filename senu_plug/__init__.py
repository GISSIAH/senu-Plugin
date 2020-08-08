# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Senu
                                 A QGIS plugin
 connects to postgres db
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-08-06
        copyright            : (C) 2020 by ATTIC GIS Solutions
        email                : malunje69@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Senu class from file Senu.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .senu_plug import Senu
    return Senu(iface)
