# Copyright (c) 2026, sujithanagireddy@gmail.com and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {"label": "Task", "fieldtype": "Link", "options": "Project Task", "fieldname": "task_link", "width": 140},
        {"label": "Project", "fieldtype": "Link", "options": "Project Data", "fieldname": "project", "width": 140},
        {"label": "Resource", "fieldtype": "Link", "options": "Resource", "fieldname": "resource", "width": 140},
        {"label": "Date", "fieldtype": "Date", "fieldname": "date", "width": 140},
        {"label": "Worked Hours", "fieldtype": "Float", "fieldname": "hours_worked", "width": 140},
        {"label": "Total Amount", "fieldtype": "Float", "fieldname": "total_amount", "width": 140}
    ]


def get_data(filters):
    conditions = []
    values = {}

    
    if filters.get("project"):
        conditions.append("project = %(project)s")
        values["project"] = filters.get("project")

    if filters.get("task_link"):
        conditions.append("task_link = %(task_link)s")
        values["task_link"] = filters.get("task_link")

    if filters.get("resource"):
        conditions.append("resource = %(resource)s")
        values["resource"] = filters.get("resource")

    if filters.get("date"):
        conditions.append("date = %(date)s")
        values["date"] = filters.get("date")

    condition_str = ""
    if conditions:
        condition_str = " WHERE " + " AND ".join(conditions)

    query = f"""
        SELECT
            task_link,
            project,
            resource,
            date,
            hours_worked,
            total_amount
        FROM `tabTimesheet Entry`
        {condition_str}
    """

    return frappe.db.sql(query, values, as_dict=True)
