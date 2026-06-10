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

    @api.model_create_multi
    def create(self, vals_list):
        sessions = super().create(vals_list)
        students = self.env['class.student'].search([])
        session_line_model = self.env['class.session.line']

        lines_to_create = []
        for session in sessions:
            existing_student_ids = session.line_ids.student_id.ids
            lines_to_create.extend(
                {
                    'session_id': session.id,
                    'student_id': student.id,
                }
                for student in students
                if student.id not in existing_student_ids
            )

        if lines_to_create:
            session_line_model.create(lines_to_create)

        return sessions
