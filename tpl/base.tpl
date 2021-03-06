<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="{{lang}}" lang="{{lang}}">
  <head>
    <title>OSU Theses and Dissertations&emdash;{% block title %} {% endblock %}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <style type="text/css">
      html {background-color: #CCC;}
      body {
        font: 13px/1.231 arial,helvetica,clean,sans-serif;
        width: 62em;
        margin: 5em auto ;
        padding: 3em 5em 10em;
        background-color: #EEE;
        -moz-box-shadow: 3px 3px 5px 6px #888;
        -webkit-box-shadow: 3px 3px 5px 6px #888;
        box-shadow: 3px 3px 5px 6px #888;
      }
      h1 { 
        font-family:arial,helvetica,clean,sans-serif;
        text-align: center;
        margin: .5em;
      }
      h4 {
        margin: 0;
      }
      #searchBox {
        width: 20em;
        margin: 5em auto 1em;
      }

      input:not([type=submit]) {
        font-weight: bold;
        border: 3px solid white; 
        -webkit-box-shadow: 
          inset 0 0 3px  rgba(0,0,0,0.1),
                0 0 6px rgba(0,0,0,0.1); 
        -moz-box-shadow: 
          inset 0 0 3px  rgba(0,0,0,0.1),
                0 0 6px rgba(0,0,0,0.1); 
        box-shadow: 
            inset 0 0 3px  rgba(0,0,0,0.1),
                  0 0 6px rgba(0,0,0,0.1); 
        padding: 5px;
        background: rgba(255,255,255,0.5);
        margin: 0 3em 8px 10px;
      }
      .listing { 
        width: 45em;
        margin: 2em auto;
        background-color: #FFF;
        -moz-box-shadow: 1px 1px 4px 4px #CCC;
        -webkit-box-shadow: 1px 1px 4px 4px #CCC;
        box-shadow: 1px 1px 4px 4px #CCC;
      }
      tr {
            height: 2em;
      }
      tr.odd {
      	background-color: #ccc;
      }
      tr.even {
      	background-color: #eee;
      }
      td {
      padding: 0 1em;
      }
      .searchHit {
        -khtml-border-radius: 10px;
        -moz-border-radius: 10px;
        -webkit-border-radius: 10px;
        border-radius: 10px;
        background: white;
        border: 1px solid #CCC;
        margin: 10px 0 0 0;
        padding: 1em;
        background: #FFF;
      }
      .searchHit .degree {
        float: right;
        height: 100%;
        width: 5em;
      }
    </style>

    {% block scripts %}{% endblock %}
  </head>
  <body>

    {% block content %}{% endblock %}

  </body>
</html>
