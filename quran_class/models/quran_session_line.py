from odoo import fields, models

RATING_SELECTION = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]


class ClassSessionLine(models.Model):
    _name = 'class.session.line'
    _description = 'Quran Class Session Line'

    session_id = fields.Many2one(
        comodel_name='class.session',
        string='Session',
        required=True,
        ondelete='cascade',
    )
    student_id = fields.Many2one(
        comodel_name='class.student',
        string='Student',
        required=True,
        ondelete='cascade',
    )

    attendance_status = fields.Selection(
        selection=[
            ('present', 'Present'),
            ('absent', 'Absent'),
            ('late', 'Late'),
            ('excused', 'Excused'),
        ],
        string='Attendance',
    )

    recitation_surah = fields.Char(string='Recitation Surah')
    recitation_ayah_from = fields.Integer(string='Ayah From')
    recitation_ayah_to = fields.Integer(string='Ayah To')
    recitation_rating = fields.Selection(
        selection=RATING_SELECTION, string='Recitation Rating')
    memorization_rating = fields.Selection(
        selection=RATING_SELECTION, string='Memorization Rating')

    mistake_notes = fields.Text(string='Mistake Notes')
    motivation_points = fields.Integer(string='Motivation Points')
    reward_note = fields.Char(string='Reward Note')
    needs_review = fields.Boolean(string='Needs Review')
