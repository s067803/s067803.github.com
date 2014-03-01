---
layout: bootstrap
title: Your New Jekyll Site
---

<!--==================================================================== HOME-->
<div id="home">

<!--==================================================================== POST-->
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

</div>
