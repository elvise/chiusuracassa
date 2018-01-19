# Copyright (c) 2013, Syed Abdul Qadeer and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from erpnext.controllers.queries import get_match_cond
from frappe import _


def execute(filters=None):
	if not filters: filters = frappe._dict()
	columns, data = get_data(frappe._dict(filters))
	return columns, data


def get_data(filters):
	conditions = ""
	if filters.from_date:
		conditions += " and `tabSales Invoice`.posting_date >= %(from_date)s"
	if filters.to_date:
		conditions += " and `tabSales Invoice`.posting_date <= %(to_date)s"
	if filters.store:
		conditions += " and `tabSales Invoice`.store = %(store)s"

	columns = [
		_("Store") + ":Link/Store:120",
		_("Mode Of Payment") + "::120",
		_("Grand Total") + "::120"]

	if not filters.from_date and not filters.to_date:
		frappe.throw(_("Please select From Date and To Date"))

	data = frappe.db.sql("""
		SELECT
		`tabSales Invoice`.store,
		`tabSales Invoice`.mode_of_payment,
		SUM(`tabSales Invoice`.grand_total)

	FROM
		`tabSales Invoice`
	WHERE
		`tabSales Invoice`.docstatus = 1 {conditions} {match_cond}
	GROUP BY `tabSales Invoice`.store, `tabSales Invoice`.mode_of_payment
	ORDER BY
		`tabSales Invoice`.posting_date desc, `tabSales Invoice`.posting_time desc
	""".format(conditions=conditions, match_cond=get_match_cond('Sales Invoice')), filters)

	return columns, data