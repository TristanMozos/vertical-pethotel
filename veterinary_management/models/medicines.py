from odoo import fields, models


class Medicine(models.Model):
    _name = "animal.medicine"
    _description = "Animal medicines table"

    name = fields.Char(string="Medicine", required=True)
    description = fields.Text(string="Description")
