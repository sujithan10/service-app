frappe.query_reports["Timesheet Report"] = {
    "filters": [

        {
            "fieldname": "project",
            "label": "Project",
            "fieldtype": "Link",
            "options": "Project Data",
			"reqd" : 1
        },

        {
            "fieldname": "task_link",
            "label": "Task",
            "fieldtype": "Link",
            "options": "Project Task"
        },

        {
            "fieldname": "resource",
            "label": "Resource",
            "fieldtype": "Link",
            "options": "Resource"
        },
        {
            "fieldname": "date",
            "label": "From Date",
            "fieldtype": "Date"
        }

    ]
};
