
from erpnext.selling.doctype.sales_order.sales_order import SalesOrder
import frappe

class CustomSalesOrder(SalesOrder):

    def validate(self):
        # ALWAYS call parent method
        super().validate()

        # # Custom validation
        # if not self.po_no:
        #     frappe.throw("PO Number is mandatory before submitting Sales Order")

    def before_submit(self):
        if self.grand_total < 500000:
            frappe.throw("Sales Order above 5 Lakhs needs management approval")