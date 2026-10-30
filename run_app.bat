@echo off
title Walmart Sales Predictive API
cd /d "%~dp0"
call .venv\Scripts\activate.bat
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
pause

