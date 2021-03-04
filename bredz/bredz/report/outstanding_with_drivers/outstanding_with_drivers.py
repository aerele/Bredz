# Copyright (c) 2013, Bredz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from datetime import datetime

def execute(filters=None):
	columns = [
		{
			"fieldname": "driver_name",
			"fieldtype": "Data",
			"label": "Driver Name",
			"width": 0
		},
		{
			"fieldname": "outstanding_amount",
			"fieldtype": "Data",
			"label": "Outstanding Amount",
			"width": 0
		}
	]
	data = ''
	if filters.from_date and filters.to_date:
		data = get_data(filters.from_date, filters.to_date)
	return columns, data

def get_data(from_date, to_date):
	from_date = datetime.strptime(from_date, "%Y-%m-%d")
	to_date = datetime.strptime(to_date, "%Y-%m-%d")
	return frappe.db.sql(f'''SELECT assigned_driver,SUM(outstanding_amount) FROM `tabSales Invoice` where payment_type = \'CASH\' AND closing_time >=\'{from_date}\' AND closing_time <=\'{to_date}\' GROUP BY assigned_driver''')