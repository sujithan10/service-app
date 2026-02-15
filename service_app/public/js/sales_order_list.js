frappe.listview_settings['Sales Order'] = {
    onload: function(listview) {
        frappe.msgprint("suji")
        listview.filter_area.add([
            ["Sales Order", "docstatus", "=", 0]
        ]);
    }
};
