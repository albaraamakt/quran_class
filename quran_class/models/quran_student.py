from odoo import fields, models


class ClassStudent(models.Model):
    _name = 'class.student'
    _description = 'Quran Class Student'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    parent_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Parent / Guardian',
    )
    parent_phone = fields.Char(string='Parent Phone')
    parent_email = fields.Char(string='Parent Email')
    active = fields.Boolean(string='Active', default=True)
    notes = fields.Text(string='Notes')

    session_line_ids = fields.One2many(
        comodel_name='class.session.line',
        inverse_name='student_id',
        string='Session Lines',
    )
    assignment_ids = fields.One2many(
        comodel_name='class.assignment',
        inverse_name='student_id',
        string='Assignments',
    )

    # Computed in a later phase.
    attendance_rate = fields.Float(string='Attendance Rate')
    latest_recitation_rating = fields.Char(string='Latest Recitation Rating')
    latest_memorization_rating = fields.Char(string='Latest Memorization Rating')
