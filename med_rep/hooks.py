# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__


app_name = "med_rep"
app_version = __version__
app_title = "Med Rep"
app_publisher = "9t9it"
app_description = "ERPNext customization for Medical Rep management"
app_icon = "fa fa-medkit"
app_color = "green"
app_email = "info@9t9it.com"
app_license = "GPL-3.0"

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Lead-med_rep_sec",
                    "Lead-speciality",
                    "Lead-category",
                    "Lead-med_rep_sec_cb",
                ],
            ]
        ],
    },
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/med_rep/css/med_rep.css"
# app_include_js = "/assets/med_rep/js/med_rep.js"

# include js, css files in header of web template
# web_include_css = "/assets/med_rep/css/med_rep.css"
# web_include_js = "/assets/med_rep/js/med_rep.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "med_rep.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "med_rep.install.before_install"
# after_install = "med_rep.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "med_rep.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"med_rep.tasks.all"
# 	],
# 	"daily": [
# 		"med_rep.tasks.daily"
# 	],
# 	"hourly": [
# 		"med_rep.tasks.hourly"
# 	],
# 	"weekly": [
# 		"med_rep.tasks.weekly"
# 	]
# 	"monthly": [
# 		"med_rep.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "med_rep.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "med_rep.event.get_events"
# }
