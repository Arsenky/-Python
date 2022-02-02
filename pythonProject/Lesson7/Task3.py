import os
import shutil

root_dir = os.path.join(os.path.dirname(__file__), 'my_project')
new_dir = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')

if not os.path.exists(new_dir):
    os.mkdir(new_dir)

for root, dirs, files in os.walk(root_dir):
    if root.count('templates'):
        for dir in dirs:
            if not os.path.exists(os.path.join(new_dir, dir)):
                os.makedirs((os.path.join(new_dir, dir)))
        for file in files:
            file1 = os.path.join(root, file)
            file2 = os.path.join(new_dir, os.path.basename(root))
            if not os.path.dirname(file1) == file2:
                shutil.copy(file1, file2)
