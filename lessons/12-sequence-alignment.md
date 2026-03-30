---
layout: page
title: Sequence Alignment Overview
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/12-sequence-alignment/
---

{% capture section_overview_1 %}
Sequence Alignment Basics
{% endcapture %}

{% capture section_body_1 %}
## Global Sequence Alignment
- Aligns sequences end to end
- Forces alignment across the full length of both sequences
- Best for similar-length, closely related sequences
  - Whole genes or full genomes
- Penalizes gaps and mismatches across entire sequence
  - Missing regions reduce overall score
- Classic algorithm: **Needleman–Wunsch**

**MULTIPLE SEQUENCE ALIGNMENT**
- `Multifasta -> multifasta`

## Local Sequence Alignment
- Aligns the best matching regions only
- Finds high-similarity subsequences
- Best for sequences of different lengths
  - Reads vs reference, conserved domains
- Ignores poorly matching regions
  - Unaligned ends are not penalized
- Classic algorithm: **Smith–Waterman**

**GENOME ASSEMBLY**
- `Fastq -> fasta`
{% endcapture %}

{% capture section_overview_2 %}
Pairwise Sequence Alignment
{% endcapture %}

{% capture section_body_2 %}
## Pairwise Sequence Alignment

- Compares two sequences at a time
- Identifies similarity and differences
- Determines optimal alignment
- Accounts for matches, mismatches, and gaps
- Can be global or local:
  - **Global &rarr;** full-length comparison
  - **Local &rarr;** best matching region only
- Used for:
  - Comparing a read to a reference
  - Gene-to-gene comparisons
  - Similarity scoring
{% endcapture %}

{% capture section_overview_3 %}
Multiple Sequence Alignment
{% endcapture %}

{% capture section_body_3 %}
## Multiple Sequence Alignment

- Aligns three or more sequences simultaneously
- Identifies conserved and variable regions
- Used to study evolutionary relationships
  - Compare strains, species, or gene families
- Highlights mutations and conserved motifs
  - Detect SNPs, insertions, deletions
- Common tools:
  - **MAFFT**
  - **MUSCLE**
  - **Clustal Omega**
- Practical uses:
  - Compare viral genomes across samples
  - Build phylogenetic trees
  - Identify conserved primer or target regions
{% endcapture %}

{% capture section_overview_4 %}
References
{% endcapture %}

{% capture section_body_4 %}
## References

- **What is a reference?**
  - A reference sequence serves as a standardized baseline for sequence comparisons.
{% endcapture %}

{% capture section_overview_5 %}
Coordinate Space
{% endcapture %}

{% capture section_body_5 %}
## Coordinate Space

- **Coordinate space** is very important for discussing alignments. It defines the positioning and boundaries of a sequence, allowing researchers to pinpoint exactly where mutations, genes, or other features are located relative to a reference.
{% endcapture %}

{% include activity.html variant="1" title="Sequence Alignment Basics" overview=section_overview_1 content=section_body_1 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="2" title="Pairwise Sequence Alignment" overview=section_overview_2 content=section_body_2 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="3" title="Multiple Sequence Alignment" overview=section_overview_3 content=section_body_3 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="1" title="References" overview=section_overview_4 content=section_body_4 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="2" title="Coordinate Space" overview=section_overview_5 content=section_body_5 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
