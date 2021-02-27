// Copyright (c) 2021, Bredz and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bredz Sales Invoice', {
	sun_code:function(frm) {
		if(frm.doc.sun_code){
			frappe.call({
				method:"bredz.bredz.doctype.bredz_sales_invoice.bredz_sales_invoice.get_address",
				args:{
					"suncode": frm.doc.sun_code,
				},
				callback:function(res){
					if(!res.exc){
						frm.set_query("bc_code", function(){
							return{
								filters:[
									["Address", "name", 'in', res.message]
								]
							}
						})
					}
				}
			})
		}
	}
});
