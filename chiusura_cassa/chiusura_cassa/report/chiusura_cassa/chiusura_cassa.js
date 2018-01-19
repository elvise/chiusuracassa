// Copyright (c) 2016, Syed Abdul Qadeer and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["CHIUSURA CASSA"] = {
	"filters": [
		{
			"fieldname":"store",
			"label": __("Store"),
			"fieldtype": "Link",
			"options": "Store"
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default": frappe.defaults.get_user_default("year_start_date")
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default": frappe.defaults.get_user_default("year_end_date")
		}
	]
}
