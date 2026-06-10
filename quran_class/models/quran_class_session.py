from odoo import api, fields, models


class ClassSession(models.Model):
    _name = 'class.session'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Quran Class Session'
    _order = 'date desc, start_datetime desc'

    name = fields.Char(string='Number', required=True, copy=False, default='New')
    date = fields.Date(string='Date')
    start_datetime = fields.Datetime(string='Start')
    end_datetime = fields.Datetime(string='End')
    topic = fields.Char(string='Topic')
    notes = fields.Text(string='Notes')

    line_ids = fields.One2many(
        comodel_name='class.session.line',
        inverse_name='session_id',
        string='Session Lines',
    )
    assignment_ids = fields.One2many(
        comodel_name='class.assignment',
        inverse_name='given_session_id',
        string='Assignments',
    )
    line_count = fields.Integer(
        string='Session Lines',
        compute='_compute_line_count',
    )

    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
        default='draft',
        required=True,
    )

    @api.depends('line_ids')
    def _compute_line_count(self):
        for session in self:
            session.line_count = len(session.line_ids)
