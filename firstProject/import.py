import csv, sys, os
project_dir = "/Users/Narayana c/ProjectFolder/firstProject"
sys.path.append(project_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstProject.settings")
# os.environ["DJANGO_SETTINGS_MODULE"] = 'settings'

import django
django.setup()
from firstApp.models import employee

data = csv.reader(open("/Users/Narayana c/ProjectFolder/firstProject/Book11.csv"), delimiter=",")


for row in data:
	if row[0] != 'name':
		post = employee()
		post.name = row[0]
		post.phone = row[1]
		post.address = row[2]
		post.role = row[3]
		post.save()