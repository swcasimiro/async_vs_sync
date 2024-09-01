# SYNC VS ASYNC DJANGO 5.2

<img src="https://img.shields.io/badge/django 5.2-async-black?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/>

<p>Взяты две стандартные связанные модели категории и продукта. Которые заполнены 10 тысячими экземпляров модели продукта. Сравнение скорости запросов. Хоть не со всем честные, ведь задача у ассинхронности немного другая. Но всё же интересная. Решил пустить в общий доступ, 
если кому-то придет на ум такая же идея.</p>
<hr>
<strong><p>Активация проекта:</p></strong>
<code>python -m venv venv</code>
<br>
<br>
<code>venv\Scripts\activate.bat</code>
<br>
<br>
<code>pip install -r requirements.txt</code>
<br>
<br>
<code>python manage.py makemigrations</code>
<br>
<br>
<code>python manage.py migrate</code>
<br>
<br>
<code>python manage.py createsuperuser</code>
<br>
<br>
