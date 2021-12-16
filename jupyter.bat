@echo off
echo ini adalah run jupyter notebook yang telah saya buat
echo ini akan dijalankan
pause
cd d:
cd /python39/project/dua
cmd /k "venv\scripts\activate.bat & cd mysite & python manage.py shell_plus --notebook"