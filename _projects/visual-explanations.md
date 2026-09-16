---
layout: page
title: Visual explanations for machine learning
permalink: /projects/visual-explanations/
description: Animated explanations of machine learning, beginning with batch and layer normalization.
img: assets/img/visualizations/batch-layer-normalization.jpg
og_image: /assets/img/visualizations/batch-layer-normalization.jpg
importance: 2
category: learning design
related_publications: false
---

**Focus:** Visualization · Machine learning · Multiple representations

## Watch the visualizations

{% for visualization in site.data.visualizations %}

<section aria-labelledby="{{ visualization.id }}-title">
  <h3 id="{{ visualization.id }}-title">{{ visualization.title }}</h3>
  <p id="{{ visualization.id }}-summary">{{ visualization.summary }}</p>
  <figure>
    <video
      controls
      playsinline
      preload="metadata"
      width="1920"
      height="1080"
      style="display: block; width: 100%; height: auto; border-radius: 6px;"
      poster="{{ visualization.poster | relative_url }}"
      aria-labelledby="{{ visualization.id }}-title"
      aria-describedby="{{ visualization.id }}-summary {{ visualization.id }}-caption"
    >
      <source src="{{ visualization.video | relative_url }}" type="video/mp4">
      Your browser does not support embedded video. <a href="{{ visualization.video | relative_url }}">Open the video</a>.
    </video>
    <figcaption id="{{ visualization.id }}-caption" class="caption">
      {{ visualization.duration }} · Silent animation · Use the player controls to pause, replay, or view full screen.
    </figcaption>
  </figure>
  <p><a href="{{ visualization.video | relative_url }}">Open or download {{ visualization.title }}</a></p>
  <p><strong>Learning goal:</strong> {{ visualization.learning_goal }}</p>
  <p><strong>Try this:</strong> {{ visualization.prompt }}</p>
  <details>
    <summary>Read the visual explanation</summary>
    <div>{{ visualization.text_alternative | markdownify }}</div>
  </details>
</section>
{% endfor %}

## The learning need

Computational ideas can be difficult to understand when students encounter only notation or code. A visual representation can make an abstract process more concrete and provide another way into a challenging concept.

## What I create

I create visual artifacts explaining difficult concepts, particularly in machine learning. My tools include Manim, Remotion, and AI-assisted coding.

These explanations are intended to help students develop the intuition they need to engage with mathematical and algorithmic reasoning. I use them as one representation within a broader learning experience.

## How the work connects to instruction

Students develop understanding through different pathways. I pair visual explanations with targeted resources and alternative explanations for students who need additional support. Aligned challenge problems give students opportunities to explore edge cases, generalize an idea, or connect it to a more advanced application.

The shared goal is rigorous understanding, reached through multiple routes.

[Explore visualization resources]({{ '/resources/' | relative_url }}) · [All selected work]({{ '/projects/' | relative_url }})
