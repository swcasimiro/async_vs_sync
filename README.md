# SYNC VS ASYNC DJANGO 5.2

<img src="https://img.shields.io/badge/django 5.2-async-black?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/>

<p>Взяты две стандартные связанные модели категории и продукта. Которые заполнены 10 тысячими экземпляров модели продукта. Сравнение скорости запросов. Хоть не со всем честные, ведь задача у ассинхронности немного другая. Но всё же интересная. Решил пустить в общий доступ, 
если кому-то придет на ум такая же идея.</p>
<hr>

<p><code>Фреймворк и библиотеки</code></p>

<a>
    <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/> 
</a>
<p><code>База данных</code></p>
<a>
    <img src="https://img.shields.io/badge/sqlite-3f9cd8?style=for-the-badge&logo=sqlite&logoColor=white" alt="nginx Badge"/>
</a>

</div>

<strong><p>Активация проекта:</p></strong>
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

<strong><p>Инструкция при первом запуске:</p></strong>
<p>Перед использованием административной панели и создание новый суперюзеров. Ознакомьтесь с инструкцией ниже. Пользователь создан с которым вы можете перейти на следующий этап. А именно заполнению
самого сайта нужным вам контентом.</p>
<ul>
<li>База данных заполнена.</li>
<li>Произведены миграции</li>
<li>Создан superuser
<ul>
<li>Login: root</li>
<li>Password: 123</li>
</ul></li>
</ul>

<br>
<strong><p>Адреса для входа в административную панель:</p></strong>
<ul>
<li>http://127.0.0.1:8000/admin/</li>
<li>http://localhost/admin/</li>
<li><code>http://domain_name.ru/admin/</code></li>
</ul>
