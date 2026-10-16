# Quran Class

An Odoo 19 module (`quran_class`) for running a Quran class: keeping a roster of
students, recording each class session, tracking every student's attendance and
recitation in that session, and following up on memorization and review
homework.

It depends only on `base` and `mail`, installs as a standalone app, and adds a
**Quran Class** menu with three entries: **Sessions**, **Students** and
**Assignments**.

## Data model

| Model | Purpose |
| --- | --- |
| `class.student` | A student, with their parent or guardian (`res.partner`), contact phone and email, notes, and an `active` flag for archiving. Links to the student's session lines and assignments. |
| `class.session` | One class meeting: number, date, start and end time, topic, notes and a status (Draft → Done, or Cancelled). Has chatter and activities through `mail.thread`. |
| `class.session.line` | One student in one session: attendance (present, absent, late, excused), the surah and ayah range recited, recitation and memorization ratings (1–5), mistake notes, motivation points, a reward note and a "needs review" flag. |
| `class.assignment` | Homework for a student: type (memorization, review or recitation), surah and ayah range, due date, the session it was given in, and its submission (status, date, 1–5 rating, notes). |

```
class.student ──< class.session.line >── class.session
      │                                        │
      └──────────< class.assignment >──────────┘
                                  (given_session_id)
```

## Behaviour

- **Automatic session lines.** When a session is created, it gets a session
  line for every active student, so the teacher can fill in attendance and
  ratings without adding each student by hand
  (`quran_class/models/quran_class_session.py`).
- **Session form.** A smart button opens the session's lines, and a notebook
  holds an inline-editable list of the assignments given in that session, plus
  notes.
- **Student form.** Shows the student's history across sessions and their
  assignments, with an "Archived" ribbon for inactive students.
- **Access.** All four models are readable and writable by any internal user
  (`base.group_user`); there are no separate teacher or parent roles yet.

## Not built yet

- `attendance_rate`, `latest_recitation_rating` and
  `latest_memorization_rating` on `class.student` are plain fields for now; the
  code marks them to be computed in a later phase.
- The manifest describes managing teachers, schedules and enrollment, but
  there is no teacher model and no enrollment: every active student is added to
  every session.
- There is no automatic session numbering (`name` defaults to `New`), no demo
  data and no tests.

## Layout

```
quran_class/
├── __manifest__.py
├── models/       student, session, session line, assignment
├── views/        list and form views, actions, menus
└── security/     ir.model.access.csv
```

## Installing

Put the `quran_class` directory on an Odoo 19 addons path, update the apps
list, and install **Quran Class**.
