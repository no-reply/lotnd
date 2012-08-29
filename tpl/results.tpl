{% extends "base.tpl" %}

{% block title %}Search Results{% endblock %}

{% block content %}
    <h1>Search Results</h1>	
    <div id='results'>
    {% for r in results %}
      <div class="searchHit">
	<div class="degree">{{ r.degree.label }}</div>
	<h4>{{ r.title }}</h4>

	<span class="author">{{ r.author.name }}</span>
	<span class="advisor">{{ r.advisor.name }}</span>		


	<div style="height: 0; visibility:hidden;">{{ r }}</div>
      </div>
    {% endfor %}
    </div>
{% endblock %}

