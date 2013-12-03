---
layout: default
title: Your New Jekyll Site
---

<div id="home">
  <h1>Blog Posts</h1>
  <ul class="posts">
    {% for post in site.posts %}
	  <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}"><strong>{{ post.title }}</strong></a></li>
    {% endfor %}
  </ul>
  <a class="twitter-timeline" href="https://twitter.com/su104003" data-widget-id="407771890686492672">@su104003 からのツイート</a>
  <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
  <iframe src="http://blueegrets.web.fc2.com">iframe</iframe>
</div>
