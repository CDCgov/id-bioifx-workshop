---
layout: page
title: Workshops
permalink: /workshops/
sidebar: workshop_sidebar
topnav: topnav
---

# Workshops

Below are scheduled workshops.

<ul>
{% assign ws = site.workshops | sort: 'workshop_order' %}
{% for w in ws %}
  <li><a href="{{ w.url | relative_url }}">{{ w.title }}</a> {% if w.location %}- {{ w.location }}{% endif %} {% if w.event_date %}({{ w.event_date | date: '%Y-%m-%d' }}){% endif %}</li>
{% endfor %}
</ul>
