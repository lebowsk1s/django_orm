# django_orm
ORM from django


How to use it?

1.use django_orm as a package

2.modify the **databases setting** in djsettings.py, put your IP, PORT, USER NAME, PASSWORD of database in djsettings.py

3.run the command to generate django models: **"python manage.py inspectdb > app/models.py"**. OK, here we got the models.

4.use the models like:
**from django_orm.app.models import Model_A, Model_B**
