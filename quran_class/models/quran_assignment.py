from odoo import fields, models

RATING_SELECTION = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]


class ClassAssignment(models.Model):
    _name = 'class.assignment'
    _description = 'Quran Class Assignment'
    _order = 'due_date desc'

    student_id = fields.Many2one(
        comodel_name='class.student',
        string='Student',
        required=True,
        ondelete='cascade',
    )
    given_session_id = fields.Many2one(
        comodel_name='class.session',
        string='Given In Session',
        ondelete='set null',
    )
    due_date = fields.Date(string='Due Date')

    assignment_type = fields.Selection(
        selection=[
            ('memorization', 'Memorization'),
            ('review', 'Review'),
            ('recitation', 'Recitation'),
        ],
        default='memorization',
        string='Type',
    )
    surah = fields.Char(string='Surah')
    ayah_from = fields.Integer(string='Ayah From')
    ayah_to = fields.Integer(string='Ayah To')

    state = fields.Selection(
        selection=[
            ('assigned', 'Assigned'),
            ('submitted', 'Submitted'),
            ('missed', 'Missed'),
            ('partial', 'Partial'),
        ],
        string='Status',
        default='assigned',
        required=True,
    )
    submission_date = fields.Date(string='Submission Date')
    submission_rating = fields.Selection(
        selection=RATING_SELECTION, string='Submission Rating')
    submission_notes = fields.Text(string='Submission Notes')
