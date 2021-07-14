This repository is hands-on guide for [pirogramming](https://pirogramming.com/) 15th members.  
You can see the lecture slides in [here](https://drive.google.com/file/d/1FdoTuAN1r1cT3j-H3uQnHwZFecqI0LB-/view?usp=sharing).

---
## Process

1. Code class model in `models.py`

2. Make migration files for the model code
    - `python manage.py makemigrations <app_name>`
    - You can skip app name. Then django would make migrations file for all apps.

3. Migrate your code to database, based on migration files!
    - `python manage.py migrate <app_name>`
    - You can skip app name, either.
    
4. Check your database!
    - The easiest way is seeing django admin pannel(`http://localhost:8000/admin`)
    - Or, if you want to see database explicitly ...
        - you can use database CLI (`python manage.py dbshell`)
        - GUI tools such as [TablePlus](https://tableplus.com/)!
   
    
