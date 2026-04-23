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

<div style="text-align: center;">
  <img src="{{ '/assets/images/DSCF3295-Mejorado-NR.jpg' | relative_url }}" alt="Workshop photo" style="max-width: 80%; height: auto;">
</div>
