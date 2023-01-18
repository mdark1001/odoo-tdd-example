"""
@author: Miguel Cabrera R. <miguel.cbarera@oohel.net>
@date: 18/01/23
@name: 
"""
from datetime import datetime
from datetime import timedelta

from odoo.tests.common import TransactionCase
from odoo.tests.common import new_test_user


class TestOnTodoListModelsCheck(TransactionCase):
    """
        Test sobre los modelos del módulo todo list
    """

    def setUp(self):
        super(TestOnTodoListModelsCheck, self).setUp()
        self.state_default = 'draft'
        self.admin = new_test_user(
            self.env,
            login='admin-user-todo-list',
            groups='oohel_todo_list.group_admin_todo_list,base.group_user'
        )
        self.user = new_test_user(
            self.env,
            login='user-todo-list',
            groups='oohel_todo_list.group_user_todo_list,base.group_user'
        )
        self.user2 = new_test_user(
            self.env,
            login='user2-todo-list',
            groups='oohel_todo_list.group_user_todo_list,base.group_user'
        )

    def test_check_model_todo_list_read(self):
        items = self.env['oohel.todo.list'].with_user(self.admin).search([])
        self.assertEqual(0, len(items))

    def test_check_model_tags_read(self):
        items = self.env['oohel.todo.list.tag'].with_user(self.admin).search([])
        self.assertEqual(0, len(items))

    def test_create_todo_list_without_tags_and_check_user(self):
        """ Crear una registro con un usuario y validad que tenga el usuario correcto sin asignar tags   """
        items = self.env['oohel.todo.list'].with_user(self.user).create(
            {
                'title': 'Test todo list',
                'description': "Example",
                "deadline": datetime.now() + timedelta(days=2),
            }
        )
        self.assertIsNotNone(items)
        self.assertEqual(self.user, items.user_id)
        self.assertEqual(self.state_default, items.state)


