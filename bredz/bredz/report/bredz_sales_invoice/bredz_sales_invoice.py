# Copyright (c) 2013, Bredz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = [
		{
			"fieldname": "bc_code",
			"fieldtype": "link",
			"options": "Address",
			"label": "BC Code",
			"width": 0
		},
		{
			"fieldname": "sun_code",
			"fieldtype": "link",
			"options": "Customer",
			"label": "Sun Code",
			"width": 0
		},
		{
			"fieldname": "invoice_no",
			"fieldtype": "Data",
			"label": "Invoice No",
			"width": 0
		},
		{
			"fieldname": "assigned_driver",
			"fieldtype": "Data",
			"label": "Assigned Driver",
			"width": 0
		},
		{
			"fieldname": "payment_type",
			"fieldtype": "Data",
			"label": "Payment Type",
			"width": 0
		},
		{
			"fieldname": "customer_name",
			"fieldtype": "Data",
			"label": "Customer Name",
			"width": 0
		}, 
		{
			"fieldname": "buisness_date",
			"fieldtype": "Data",
			"label": "Buisness Date",
			"width": 0
		},
		# {
		# 	"fieldname": "status",
		# 	"fieldtype": "Data",
		# 	"label": "Status",
		# 	"width": 0
		# },
		{
			"fieldname": "value",
			"fieldtype": "Data",
			"label": "Value",
			"width": 0
		}
	]
	data = ''
	if filters.from_date and filters.to_date:
		data = get_data(filters.from_date, filters.to_date)
	return columns, data
def get_data(from_date, to_date):
	return frappe.db.sql(f'''SELECT 
		customer_address, customer, invoice_number, assigned_driver, payment_type, outlet_name, closing_time, grand_total
		FROM `tabSales Invoice` where closing_time >={from_date} and closing_time <={to_date}''')