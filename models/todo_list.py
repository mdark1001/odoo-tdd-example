"""
@author: Miguel Cabrera R. <miguel.cbarera@oohel.net>
@date: 18/01/23
@name: 
"""

from odoo import api, fields, models


class ToDoList(models.Model):
    """
    Modelo que almacena los datos de un tarea por hacer (to do) para los usuarios registrados en la plataforma.
    """
    _name = 'oohel.todo.list'
    _description = 'Todo'

    title = fields.Char(
        string='Título',
        required=True
    )
    description = fields.Text(
        string="Descripción",
        required=False
    )
    state = fields.Selection(
        string='State',
        selection=[
            ('draft', 'Borrador'),
            ('started', 'Iniciado'),
            ('completed', 'Completo'),
            ('late', 'Atrasado')
        ],
        required=True,
        default='draft'
    )
    deadline = fields.Datetime(
        string='Deadline',
        required=True,
    )

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        required=True,
        default=lambda self: self.env.user.id,
    )

    tags_ids = fields.Many2many(
        comodel_name='oohel.todo.list.tag',
        string='Tags'
    )


class ToDoListTags(models.Model):
    """
        Modelo que almacena las etiquetas que identifica una categoría en las  tareas.
    """

    _name = 'oohel.todo.list.tag'
    _description = 'Tags'

    name = fields.Char(
        string='Tag',
        required=True
    )
