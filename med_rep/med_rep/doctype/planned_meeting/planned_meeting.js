// Copyright (c) 2019, 9t9it and contributors
// For license information, please see license.txt

frappe.ui.form.on('Planned Meeting', {
  user: function(frm) {
    frm.trigger('set_leads_table');
  },
  start_datetime: function(frm) {
    frm.trigger('set_leads_table');
  },
  end_datetime: function(frm) {
    frm.trigger('set_leads_table');
  },
  set_leads_table: async function(frm) {
    const { user, start_datetime, end_datetime } = frm.doc;
    if (user && start_datetime && end_datetime) {
      await frappe.call({
        method: 'set_leads',
        doc: frm.doc,
      });
      frm.refresh_field('leads');
    }
  },
});
