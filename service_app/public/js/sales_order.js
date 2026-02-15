frappe.ui.form.on('Sales Order',{
    customer : function(frm)
    {
        if(frm.doc.delivery_date){

        frm.set_value("po_no",500)
        }
    }
});