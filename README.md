# Plyushkin

Tool for managing backups (monitoring, generating scripts n etc.)
With duplicity in heart, but may be used with any backup tools with supported backends.

![Screenshot](https://raw.githubusercontent.com/rusaksoft/Plyushkin/master/Screenshot.png)

# Current status

Usable proof-of-concept

# Functional diagram

![Screenshot](https://raw.githubusercontent.com/rusaksoft/Plyushkin/master/Diagram.png)

# Setup

```
vagrant up
```

for setup admin:

```
vagrant ssh
cd /var/Plyushkin
python manage.py createsuperuser
```  


<http://localhost:8000> to view
<http://localhost:8000/admin> to edit via django administration
