from odoo import fields, models


class Vaccine(models.Model):
    _name = "animal.vaccine"
    _description = "Animal vaccines table"

    name = fields.Char(string="Vaccine", required=True)
    description = fields.Text(string="Description")
