---
layout: bootstrap
title: Toppatz
---
<div class="note">
  <p>welcome</p>
</div>

<div class="menu">
  <div class="post">
    {% for post in site.posts %}
    <span>{{ post.date | date_to_string }}</span> &raquo;
    <a href="{{ post.url }}"><strong>{{ post.title }}</strong></a>
    <br />
    {% endfor %}
  </div>
</div>
