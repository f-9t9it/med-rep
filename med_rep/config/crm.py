# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Sales Pipeline"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Planned Meeting",
                    "label": "Planned Meeting",
                }
            ],
        }
    ]
