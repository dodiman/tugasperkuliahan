@echo off
echo ini adalah file bat yang saya buat DODIMAN TAKIMPOO
pause
cd d:
cmd /k "cd /python39/project/dua & venv\scripts\activate.bat & cd tugasperkuliahan & python manage.py runserver 0.0.0.0:8000"