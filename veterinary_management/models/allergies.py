from odoo import fields, models


class Allergy(models.Model):
    _name = "animal.allergy"
    _description = "Animal allergies table"

    name = fields.Char(string="Allergies", required=True)
    description = fields.Text(string="Description")
