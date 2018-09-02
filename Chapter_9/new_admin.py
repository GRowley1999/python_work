from admin import Admin, Privileges
from users import Users

eric = Admin('eric', 'matthes', 'e_matthes')
print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()
