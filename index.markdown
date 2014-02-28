---
layout: bootstrap
title: Your New Jekyll Site
---

<div id="home">

<!--POST BEGIN-->
<div class="post">
  {% for post in site.posts %}
  <span>{{ post.date | date_to_string }}</span> &raquo;
  <a href="{{ post.url }}" target="content">
    <strong>{{ post.title }}</strong>
  </a>
  <br />
  {% endfor %}
</div>
<!--POST END-->

