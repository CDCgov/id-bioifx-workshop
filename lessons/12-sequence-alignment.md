---
layout: page
title: Sequence Alignment Overview
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/12-sequence-alignment/
---
<p style="color: #015CAE; font-size: 19px;">Content developed by Kristine Lacek</p>
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

## References

- **What is a reference?**
  - A reference sequence serves as a standardized baseline for sequence comparisons.

## Coordinate Space

- **Coordinate space** is very important for discussing alignments. It defines the positioning and boundaries of a sequence, allowing researchers to pinpoint exactly where mutations, genes, or other features are located relative to a reference.

