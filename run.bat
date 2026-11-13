@echo off
cls
if "%~1"=="" (
    python manage.py runserver
) else (
    python manage.py %*
)