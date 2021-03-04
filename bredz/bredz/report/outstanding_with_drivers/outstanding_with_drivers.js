// Copyright (c) 2016, Bredz and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Outstanding with drivers"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"fieldtype": "Date",
			"label": "From Date",
			"mandatory": 1
		},
		{
			"fieldname": "to_date",
			"fieldtype": "Date",
			"label": "To Date",
			"mandatory": 1
		}
	]
};
