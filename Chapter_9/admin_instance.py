from imported_admin import Users, Admin, Privileges

admin = Admin('Gregor', 'Rowley', 19)
admin_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
admin.privileges.privileges = admin_privilegesn
admin.privileges.show_privileges()