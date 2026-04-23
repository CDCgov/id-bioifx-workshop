---
layout: page
title: BLAST Fundamentals
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/13-blast/
---
<p style="color: #015CAE; font-size: 19px;">Content developed by Kristine Lacek</p>
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

## BLAST Databases Search Considerations

- **Databases:** NCBI BLAST, GISAID BLAST, Custom Blast Database (CLI)
- **NCBI GenBank:** open source, INSDC database
- **GISAID:** access control, but ingests INSDC samples
- For a more complete set of flu samples, which BLAST is better?
- When might an open-source BLAST search be better?

![Sample database 1]({{ site.baseurl }}/assets/blast-72-3.png){: width="75%"}

![Sample database 2]({{ site.baseurl }}/assets/blast-72-4.png){: width="75%"}

## Interpreting BLAST output

- **Percent Identity →** How similar the aligned region is
- **E-value →** Probability the match occurred by chance
  - Lower = more significant
- **Bit Score →** Alignment strength (higher = better)
- **Alignment Length →** How much of the query matched

![BLAST Table]({{ site.baseurl }}/assets/blast-73-5.png){: width="75%"}

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

## Useful CLI Options

- Control output format
  - `-outfmt 6` → tabular format (easy to parse)
- Limit results
  - `-max_target_seqs 5`
- Adjust sensitivity
  - `-evalue 1e-5`
- Set number of threads
  - `-num_threads 8`

