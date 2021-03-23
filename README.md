# Arabic_Database_Web_App
A web application served as a database for Arabic Literature


Entity - 文章

- id - int - Django 会自动生成
- title - string (max 120)
- content - string
- author - list
- Period - string
  - year
- form - 体裁 - string / char
- language - language code "EN"
- Region
  - Country and sub-region might be optional
- Genre / Tag

【Note】 - 数据同步问题 （github上目前不分享数据）

【TODO】找一找问卷星相关的APP  搜集数据


前端参照[这个网站](https://www.loebclassics.com/browse?pageSize=10&sort=authorsort&t1=library.greek)


【TODO】改Django的 schema

【TODO】Complete Database 页面的 UI


---------

Useful references: 

1. [Django (Python) : DatabaseError : x Table has No Column named y](https://stackoverflow.com/questions/11175856/django-python-databaseerror-x-table-has-no-column-named-y/43249130)
2. [What is the most efficient way to store a list in the Django models?](https://stackoverflow.com/questions/1110153/what-is-the-most-efficient-way-to-store-a-list-in-the-django-models)