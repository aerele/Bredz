# -*- coding: utf-8 -*-
# Copyright (c) 2021, Bredz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class BredzCustomerDetails(Document):
	def validate(self):
		status = frappe.db.exists('Customer', self.sun_code)
		if not status:
			new_doc = frappe.new_doc("Customer")
			new_doc.customer_name = self.sun_code
			new_doc.save()
		if frappe.db.exists("Address", {'address_title':self.bc_code}):
			update = frappe.get_doc('Address', {'address_title':self.bc_code})
			update.address_line1 = self.outlet_name
			update.address_title = self.bc_code
			update.phone = self.contact_number
			update.city = self.address if self.address else self.outlet_name
			update.payment_type = self.payment_type
			update.save() 
		else:
			new_address = frappe.new_doc('Address')
			new_address.address_line1 = self.outlet_name
			new_address.address_title = self.bc_code
			new_address.phone = self.contact_number
			new_address.city = self.address if self.address else self.outlet_name
			new_address.payment_type = self.payment_type
			links = new_address.append("links",{})
			links.link_doctype = "Customer"
			links.link_name = self.sun_code
			new_address.save()

	def on_trash(self):
		frappe.db.delete("Address", {'address_title':self.bc_code})