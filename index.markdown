---
layout: default
title: Your New Jekyll Site
---

<div id="home">
  <!--PROFILE BEGIN-->
  <table class="profile">
  <caption>PROFILE</caption>
  <tr><td>
  <p>
    Naoki Ueda<br />
    su104003(a)gmail.com<br />
    OPU, 3G<br />
  </p>
  </td></tr>
  </table>
  <!--PROFILE END-->

  <!--POST BEGIN-->
  <table class="posts">
    <caption>POSTS</caption>
    {% for post in site.posts %}
    <tr>
      <td>
        <span>{{ post.date | date_to_string }}</span> &raquo;
        <a href="{{ post.url }}" target="content">
          <strong>{{ post.title }}</strong>
        </a>
      </td>
    </tr>
    {% endfor %}
  </table>
  <!--POST END-->

  <!--LINK BEGIN-->
  <!--<table class="link">-->
  <!--<caption>LINK</caption>-->
  <!--<tr><td>-->
  <!------->
  <!--</td></tr>-->
  <!--</table>-->
  <!--LINK END-->
</div>
