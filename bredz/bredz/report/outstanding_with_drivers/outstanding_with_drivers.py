# Copyright (c) 2013, Bredz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from datetime import datetime

def execute(filters=None):
	columns = [
		{
			"fieldname": "customer_name",
			"fieldtype": "Data",
			"label": "Customer Name",
			"width": 0
		},
		{
			"fieldname": "invoice_no",
			"fieldtype": "Data",
			"label": "Invoice No",
			"width": 0
		},
		{
			"fieldname": "outstanding_amount",
			"fieldtype": "Currency",
			"precision": 2,
			"label": "Outstanding Amount",
			"width": 0
		},
		{
			"fieldname": "driver_name",
			"fieldtype": "Data",
			"label": "Driver Name",
			"width": 0
		}
	]
	data = ''
	print(filters)
	if (filters.from_date and filters.to_date) or (filters.from_date and filters.to_date and filters.driver_name):
		data = get_data(filters.from_date, filters.to_date, filters.driver_name)
	print(data)
	return columns, data

def get_data(from_date, to_date, driver):
	from_date = datetime.strptime(from_date, "%Y-%m-%d")
	to_date = datetime.strptime(to_date, "%Y-%m-%d")
	if driver:
		print(from_date, to_date, driver)
		return frappe.db.sql("""SELECT outlet_name, invoice_number, outstanding_amount, assigned_driver FROM `tabSales Invoice` where payment_type = "CASH" AND closing_time >= %s AND closing_time <= %s AND assigned_driver = %s AND status != "Unpaid" """,(from_date, to_date, driver))
	else:
		print(from_date, to_date)
		return 	frappe.db.sql("""SELECT outlet_name, invoice_number, outstanding_amount, assigned_driver FROM `tabSales Invoice` where payment_type = "CASH" AND closing_time >= %s AND closing_time <= %s AND status != "Unpaid" """,(from_date, to_date))
								# SELECT outlet_name, invoice_number, outstanding_amount, assigned_driver FROM `tabSales Invoice` where payment_type = "CASH" AND closing_time >="2021-02-01 00:00:00" AND closing_time <= "2021-02-13 00:00:00" AND status = "Unpaid"