---
layout: page
title: BLAST Fundamentals
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/13-blast/
---

{% capture section_overview_1 %}
BLAST
{% endcapture %}

{% capture section_body_1 %}
## BLAST (Basic Local Alignment Search Tool)

- Finds regions of similarity between sequences
- Compares a query sequence to a database
- Identifies closest matches
- Uses local alignment
- Finds the best matching regions, not full-length alignment
- Widely used in bioinformatics
  - Gene identification
  - Species confirmation
  - Contamination checks
{% endcapture %}

{% capture section_overview_2 %}
Different BLAST Programs & Databases
{% endcapture %}

{% capture section_body_2 %}
## Different BLAST Programs

- **`blastn`**
  - Nucleotide vs nucleotide database
- **`blastp`**
  - Protein vs protein database
- **`blastx`**
  - Translated nucleotide vs protein database
- **`tblastn`**
  - Protein vs translated nucleotide database
- **`megablast`**
  - Optimized for highly similar sequences

## Databases
- NCBI BLAST
- GISAID BLAST
- Custom Blast Database (CLI)

![NCBI BLAST]({{ site.baseurl }}/assets/blast-71-1.png){: width="75%"}

![GISAID BLAST]({{ site.baseurl }}/assets/blast-71-2.png){: width="75%"}
{% endcapture %}

{% capture section_overview_3 %}
BLAST Databases Search Considerations
{% endcapture %}

{% capture section_body_3 %}
## BLAST Databases Search Considerations

- **Databases:** NCBI BLAST, GISAID BLAST, Custom Blast Database (CLI)
- **NCBI GenBank:** open source, INSDC database
- **GISAID:** access control, but ingests INSDC samples
- For a more complete set of flu samples, which BLAST is better?
- When might an open-source BLAST search be better?

![Sample database 1]({{ site.baseurl }}/assets/blast-72-3.png){: width="75%"}

![Sample database 2]({{ site.baseurl }}/assets/blast-72-4.png){: width="75%"}
{% endcapture %}

{% capture section_overview_4 %}
Interpreting BLAST Output
{% endcapture %}

{% capture section_body_4 %}
## Interpreting BLAST output

- **Percent Identity →** How similar the aligned region is
- **E-value →** Probability the match occurred by chance
  - Lower = more significant
- **Bit Score →** Alignment strength (higher = better)
- **Alignment Length →** How much of the query matched

![BLAST Table]({{ site.baseurl }}/assets/blast-73-5.png){: width="75%"}
{% endcapture %}

{% capture section_overview_5 %}
Running BLAST from the CLI
{% endcapture %}

{% capture section_body_5 %}
## Running BLAST from the CLI

- BLAST+ is the command-line version
  - Installed locally for large datasets or automation
  - More reproducible than web BLAST
  - Exact parameters and databases can be recorded
- Common workflow
  - Prepare database → run BLAST → interpret output

**Example command:**
```bash
blastn -query query.fasta \
       -db nt \
       -out results.txt
```
{% endcapture %}

{% capture section_overview_6 %}
Creating and Using Local Databases
{% endcapture %}

{% capture section_body_6 %}
## Creating and Using Local Databases

- Download or prepare reference FASTA
  - Example: novel influenza genomes for diagnostics efficacy
- Create a BLAST database
```bash
makeblastdb -in reference.fasta \
            -dbtype nucl
```
- Run BLAST against local database
```bash
blastn -query sample.fasta \
       -db reference.fasta \
       -out results.txt
```
- Faster and ideal for targeted analysis
- Especially useful in viral genomics
{% endcapture %}

{% capture section_overview_7 %}
Useful CLI Options
{% endcapture %}

{% capture section_body_7 %}
## Useful CLI Options

- Control output format
  - `-outfmt 6` → tabular format (easy to parse)
- Limit results
  - `-max_target_seqs 5`
- Adjust sensitivity
  - `-evalue 1e-5`
- Set number of threads
  - `-num_threads 8`
{% endcapture %}

{% include activity.html variant="1" title="BLAST Overview" overview=section_overview_1 content=section_body_1 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="2" title="Programs & Databases" overview=section_overview_2 content=section_body_2 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="3" title="Database Considerations" overview=section_overview_3 content=section_body_3 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="1" title="Interpreting Output" overview=section_overview_4 content=section_body_4 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="2" title="CLI Basics" overview=section_overview_5 content=section_body_5 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="3" title="Local Databases" overview=section_overview_6 content=section_body_6 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="1" title="CLI Options" overview=section_overview_7 content=section_body_7 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
