// Copyright (c) 2019, 9t9it and contributors
// For license information, please see license.txt

frappe.listview_settings['Planned Meeting'] = {
  get_indicator: function({ status }) {
    if (status === 'Pending') {
      return [__('Pending'), 'orange', 'status,=,Pending'];
    }
    if (status === 'Completed') {
      return [__('Completed'), 'green', 'status,=,Completed'];
    }
  },
};
