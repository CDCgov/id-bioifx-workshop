---
layout: page
title: Common Problems in Influenza Bioinformatics
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/17b-common-problems/
---
<p style="color: #015CAE; font-size: 19px;">Content developed by Ben Rambo-Martin and Kristine Lacek</p>
## Slides

<iframe
  src="{{ site.baseurl }}/presentations/Presentation10_QMS_CommonProblems.html"
  width="100%"
  height="600px"
  frameborder="0"
  allowfullscreen>
</iframe>

<a href="{{ site.baseurl }}/presentations/Presentation10_QMS_CommonProblems.html" download>Click to Download Slides</a>

---

## Objectives

- Recognize common failure modes in influenza NGS analysis
- Interpret MIRA QC failures and apply appropriate remediation
- Understand the impact of DI particles and homopolymer-induced frameshifts

---

## Common Problems in Influenza Bioinformatics

### Failed MIRA QC: Low-Coverage / Incomplete Segment Coverage

- Not enough reads in your library — go back to the lab
  - Ct <= 28?
  - Gel image resolves segment bands cleanly?
  - Proper sample number on your flow cell?
- MIRA <= v2.0.0?
  - Reads are being subsampled

### Failed MIRA QC: Minor Variant Count > 10

- In standard *clinical* samples, we have never observed >6 minor alleles (>=5% frequency) with the majority having 1-3, per segment
- Cell cultures regularly have high genetic variability which can result in high counts
- Could be a co-infection (e.g., both H1N1 and H3N2 infection at the same time)
- **Most likely contamination!**

### Failed MIRA QC: Premature Stop-Codon

- ONT homopolymer issue may require manual correction
- DI particle induced alignment

### DI Particles

Defective interfering (DI) particles can interfere with NGS analysis:

- Common in polymerase segments
- Coverage shape can spike at the ends or show "bat ears" pattern
- Can create erroneous indel mutations at coverage dropoff points

### Frameshifts

- Prevalent in homopolymer regions of Oxford Nanopore Sequencing
- DAIS-Ribosome is frameshift-tolerant
  - Shows as (~) mutation
- Convert back to nucleotide space and add or remove a base to fix

---

## MIRA Demands High Quality Results

- Together we can stop the "Garbage In" side of the data analysis mantra: **"Garbage In, Garbage Out"**
- Built-in thresholds are for standardizing QC
- Amended consensus gives us extra information from a single sequence
  - A mixed site may be under active or balancing selection in the host
- Consider each sample as a whole: if HA and NA pass but all other segments fail, consider why
- High priority samples can be useful even when QC thresholds are not met
