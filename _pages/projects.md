---
layout: page
title: Selected work
permalink: /projects/
description: Learning tools, visual explanations, and educational software.
nav: true
nav_order: 2
---

These project overviews describe my contributions and the learning questions behind them.

<div class="projects">
  <div class="row row-cols-1 row-cols-md-3">
    {% assign sorted_projects = site.projects | sort: 'importance' %}
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
</div>
