import os

root = os.path.dirname(__file__)
dir_list = ['settings', 'mainapp', 'adminapp', 'authapp']

for dir in dir_list:
    os.makedirs(os.path.join(root, f'my_project/{dir}'))
