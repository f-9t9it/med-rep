# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "module_name": "Med Rep",
            "color": "green",
            "icon": "fa fa-medkit",
            "type": "module",
            "label": _("Med Rep"),
        }
    ]
