# -*- coding: utf-8 -*-
# Copyright (c) 2019, 9t9it and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import get_datetime
from frappe.model.document import Document


class PlannedMeeting(Document):
    def on_submit(self):
        self.status = "Pending"

    def on_update_after_submit(self):
        if self.status == "Completed":
            for lead in self.leads:
                if not lead.result:
                    frappe.throw(_("Please set result in Lead table"))
        before = self.get_doc_before_save()
        if before.status == "Completed":
            frappe.throw(_("Cannot update Completed meetings"))

    def before_cancel(self):
        if self.status == "Completed":
            frappe.throw(_("Cannot cancel Completed meetings"))

    def on_cancel(self):
        frappe.db.set(self, "status", "Cancelled")

    def set_leads(self):
        start_time = get_datetime(self.start_datetime)
        end_time = get_datetime(self.end_datetime)
        if start_time > end_time:
            frappe.throw("Start Date cannot be after End Date")
        self.set("leads", [])
        leads = frappe.db.sql(
            """
                SELECT name AS lead, contact_date, speciality, category, notes
                FROM `tabLead`
                WHERE
                    contact_by = %(user)s AND
                    contact_date BETWEEN %(start_time)s AND %(end_time)s
            """,
            values={"user": self.user, "start_time": start_time, "end_time": end_time},
            as_dict=1,
        )
        for lead in leads:
            self.append("leads", lead)
