

import frappe

def set_name_for_services(doc,method=None):

    if doc.project_name:
        doc.name = doc.project_name
        
