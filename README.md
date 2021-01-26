# Arabic_Database_Web_App
A web application served as a database for Arabic Literature


Entity - 文章

- id - int
- title - string (max 200)
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