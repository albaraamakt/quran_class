{
    'name': 'Quran Class',
    'version': '19.0.1.0.0',
    'category': 'Education',
    'summary': 'Manage Quran classes, students, and teachers',
    'description': """
Quran Class Management
======================
Manage Quran classes including students, teachers, schedules and enrollment.
    """,
    'author': 'Albaraa Maktabi',
    # 'website': 'https://www.albaraamaktabi.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/quran_student_views.xml',
        'views/quran_class_session_views.xml',
        'views/quran_assignment_views.xml',
        'views/quran_class_menus.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
