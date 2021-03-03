# -*- coding: utf-8 -*-
# Copyright (c) 2021, Bredz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import datetime

@frappe.whitelist()
def get_address(suncode):
	return [i[0] for i in frappe.db.get_list("Dynamic Link", {"link_name": suncode}, ['parent'], as_list =1)] 


class BredzSalesInvoice(Document):
	def before_submit(self):
		new_doc = frappe.new_doc("Sales Invoice")
		new_doc.customer = self.sun_code 
		new_doc.invoice_number = self.invoice_no 
		new_doc.assigned_driver = self.assigned_driver 
		new_doc.outlet_name = self.customer_name
		new_doc.payment_type = self.payment_type
		new_doc.closing_time = datetime.strptime(self.close_time, "%m/%d/%Y %I:%M:%S %p")
		new_doc.customer_address = self.bc_code
		new_doc.address_display = self.address
		try:
			datetime.strptime(self.buisness_date,  '%d-%b-%y').date()
		except :
			new_doc.buisness_date = self.buisness_date
		row = new_doc.append("items",{})
		row.item_code = '001'
		row.item_name = "General Item"
		row.qty = 1
		row.rate = self.value
		new_doc.save()
		new_doc.submit()

	def on_trash(self):
		frappe.db.delete("Sales Invoice", {'invoice_number':self.invoice_no})