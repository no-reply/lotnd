{% extends "base.tpl" %}

{% block title %}Search{% endblock %}

{% block content %}
   <form action="/results" method="get" id="searchBox"> 
     <label for="id_searchText">Search:</label>
     {{ form.searchText }}
   </form>
{% endblock %}
