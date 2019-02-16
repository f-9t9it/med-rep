// Copyright (c) 2019, 9t9it and contributors
// For license information, please see license.txt

frappe.ui.form.on('Planned Meeting', {
  refresh: function(frm) {
    frm
      .get_field('leads')
      .grid.toggle_enable('result', frm.doc.status !== 'Completed');
    if (frm.doc.status === 'Pending') {
      frm.add_custom_button('Complete', async function() {
        await frm.set_value('status', 'Completed');
        frm.save('Update');
      });
    }
  },
  user: async function(frm) {
    frm.trigger('set_leads_table');
    if (frm.doc.user) {
      const { message: doc } = await frappe.db.get_value(
        'User',
        frm.doc.user,
        'full_name'
      );
      frm.set_value('user_name', doc.full_name);
    }
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
