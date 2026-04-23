---
layout: page
title: "Genome Assembly – Practical"
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/11b-genome-assembly-practical/
---

<style>
.exercise-block {
  border: 2px solid var(--c-border);
  border-radius: var(--radius);
  background: var(--c-bg-alt);
  padding: 1.25rem 1.25rem 1rem;
  margin: 1.5rem 0;
}
.exercise-block h3 { margin-top: 0; }
.exercise-block ol li { margin-bottom: 0.5rem; }
</style>

## Genome Assembly Practical Exercises

These exercises accompany the **Genome Assembly and MIRA-NF** module. They walk you through downloading FASTQ files from SRA, preparing samplesheets, running MIRA-NF, and building a complete wrapper script.

---
<p style="color: #015CAE; font-size: 19px;">Exercises developed by Kristine Lacek</p>

### Exercise 1 — FASTQ Knowledge Check
{: .mt-4}

{% include qa.html id="genome_fastq_lines" %}

{% include qa.html id="genome_fastq_line3" %}

---

### Exercise 2 — FASTQ Download and Preparation
{: .mt-4}

<div class="exercise-block" markdown="1">

1. Create a working directory structure:

   ```bash
   mkdir ~/MIRA_NGS
   mkdir ~/MIRA_NGS/day3
   cd ~/MIRA_NGS/day3
   ```

2. Using `sra-toolkit` and a loop, pull down the following samples from SRA:

   | SRR accession | Sample ID |
   |---|---|
   | SRR37675411 | f58cd412 |
   | SRR37675412 | f133a406 |
   | SRR37675413 | e91ea59e |

   ```bash
   fastq-dump --split-3 --defline-seq '@$sn/$ri' --defline-qual '+' <SRR_ACCESSION>
   ```

3. Rename the FASTQs according to the sample ID mapping, adding `_R1` and `_R2` suffixes.

4. Compress all FASTQs with `gzip`.

5. Move the compressed files to a subfolder called `fastqs`.

</div>

{% include qa.html id="genome_mkdir_day3" %}

<details>
<summary class="btn-solution">Possible Solution</summary>

<pre><code>mkdir ~/MIRA_NGS
mkdir ~/MIRA_NGS/day3
cd ~/MIRA_NGS/day3

# Download from SRA
for i in SRR37675411 SRR37675412 SRR37675413; do
    fastq-dump --split-3 --defline-seq '@$sn/$ri' --defline-qual '+' $i
done

# Create accessions mapping
cat > accessions.txt << EOF
SRR37675411,f58cd412
SRR37675412,f133a406
SRR37675413,e91ea59e
EOF

# Rename using the mapping
for i in $(cat accessions.txt); do
    mv $(echo $i | cut -f1 -d,)_1.fastq $(echo $i | cut -f2 -d,)_R1.fastq
    mv $(echo $i | cut -f1 -d,)_2.fastq $(echo $i | cut -f2 -d,)_R2.fastq
done

# Compress and organize
gzip *.fastq
mkdir fastqs
mv *.fastq.gz fastqs
</code></pre>

</details>

---

### Exercise 3 — Build a Samplesheet for MIRA-NF
{: .mt-4}

<div class="exercise-block" markdown="1">

1. Create a samplesheet using `echo`, `ls`, `cut`, `uniq`, and `sed`:

   ```bash
   echo "sample_id,sample_type" > samplesheet.csv
   ls fastqs | cut -f1 -d_ | uniq | sed "s/$/,Test/g" >> samplesheet.csv
   ```

2. Verify the samplesheet looks correct with `cat samplesheet.csv`.

</div>

{% include qa.html id="genome_samplesheet_header" %}

---

### Exercise 4 — Build a Mira-NF Execution Statement
{: .mt-4}

<div class="exercise-block" markdown="1">

Build a [Mira-NF Docker](https://hub.docker.com/r/cdcgov/mira-nf/tags) run command. You can write it directly as a shell script (`.sh` file) to reuse in the future.

- _The first time you run this, it will pull the image from Docker Hub, which may take a few minutes. Subsequent runs will be faster._

1. Create a file called `run_mira.sh` using `vim` or another editor.

2. Add the following content, adjusting paths to match your setup:

   ```bash
   #!/bin/bash
docker run \
    --privileged \
    --user $(id -u):$(id -g) \
    -v ${PWD}:/data \
    cdcgov/mira-nf:v2.1.0 \
    nextflow run /MIRA-NF/main.nf \
        -profile mira_nf_container \
        --input /data/samplesheet.csv \
        --runpath /data \
        --outdir /data/mira-output \
        --e Flu-Illumina \
        --nextclade true
   ```

3. Make it executable and run:

   ```bash
   chmod +x run_mira.sh
   ./run_mira.sh
   ```

</div>

{% include qa.html id="genome_experiment_flag" %}

{% include qa.html id="genome_profile_flag" %}

---

### Exercise 5 — Putting It All Together: Full Pipeline Script
{: .mt-4}

<div class="exercise-block" markdown="1">

For a second run, build a complete wrapper script (`mira_wrapper.sh`) that handles everything from downloading FASTQs to running MIRA-NF.

Use the following accessions:

```
SRR37675414,d969e179
SRR37675415,ba21bd1f
SRR37675416,ad336cc2
SRR37675417,89bb6967
SRR37675418,81ae9ee5
SRR37675419,73ceed0e
SRR37675420,6796f13d
SRR37675421,314ac5ba
SRR37675422,240aa994
SRR37675423,239e44e6
```

Your script should:

1. Download all FASTQs from SRA using a loop
2. Rename them using the sample ID mapping
3. Compress the FASTQs
4. Create a `fastqs/` directory and move files into it
5. Generate the samplesheet automatically
6. Run MIRA-NF

</div>

<details>
<summary class="btn-solution">Possible Solution</summary>

<pre><code>#!/bin/bash

# Download FASTQs from SRA
for i in $(cut -f1 -d, accessions.txt); do
    fastq-dump --split-3 --defline-seq '@$sn/$ri' --defline-qual '+' $i
done

# Rename FASTQs using sample IDs
for i in $(cat accessions.txt); do
    mv $(echo $i | cut -f1 -d,)_1.fastq $(echo $i | cut -f2 -d,)_R1.fastq
    mv $(echo $i | cut -f1 -d,)_2.fastq $(echo $i | cut -f2 -d,)_R2.fastq
done

# Compress and organize
gzip *.fastq
mkdir fastqs
mv *.fastq.gz fastqs

# Generate samplesheet
echo "sample_id,sample_type" > samplesheet.csv
ls fastqs | cut -f1 -d_ | uniq | sed "s/$/,Test/g" >> samplesheet.csv

# Run MIRA-NF
docker run \
    --privileged \
    -v ${PWD}:/data \
    --user $(id -u):$(id -g) \
    cdcgov/mira-nf:v2.1.0 \
    nextflow run /MIRA-NF/main.nf \
        -profile mira_nf_container \
        --input /data/samplesheet.csv \
        --runpath /data \
        --outdir /data/mira-output \
        --e Flu-Illumina \
        --nextclade true
</code></pre>

</details>

---

### Exercise 6 — Post-Pipeline Challenges
{: .mt-4}

<div class="exercise-block" markdown="1">

After MIRA-NF completes, extend your wrapper script with one or more of the following:

1. **Copy** the amended `consensus.fasta` to your home directory.
2. **Use `sed`** on the amended consensus FASTA to convert sample IDs into strain names.
3. **Rename** the `aggregate_outputs` directory to `<runID>_outputs`.
4. **Count** the number of samples that pass QC by grepping the `aggregate_outputs/csv-reports/<runid>_summary.csv`.
5. **Challenge:** Loop through the amended `consensus.fasta` and break it into 8 per-segment multifastas.

</div>

<details>
<summary class="btn-solution">Possible Solutions</summary>

<ul>
  <li><strong>Copy consensus:</strong> <code>cp outputs/aggregate_outputs/mira-reports/*amended_consensus.fasta ~/</code></li>
  <li><strong>Sed strain names:</strong> Use <code>sed -s</code> with an alternative delimiter (<code>%</code> or <code>#</code>) since strain names contain <code>/</code></li>
  <li><strong>Count passing samples:</strong> <code>grep -c "PASS" outputs/aggregate_outputs/csv-reports/*_summary.csv</code></li>
  <li><strong>Per-segment split:</strong> Use <code>grep</code> with segment names and redirect to individual files in a loop</li>
</ul>

</details>

---

### Exercise 7 — Samtools Practical
{: .mt-4}

<div class="exercise-block" markdown="1">

Navigate to the Mira output from your first run and perform the following tasks using `samtools`:

1. View the first 10 lines of each `A_HA.bam` file across the three sample outputs. Approximately where in the gene are these reads?
2. Do these BAM files need to be sorted?
3. Remove the `A_HA.bam.bai` file, then re-index the HA BAM file with `samtools index`.
4. Using `ls -lah`, how large is the `A_HA.bam` file? Using `samtools view` with redirect or the `-o` argument, convert `A_HA.bam` to `A_HA.sam`. How large is the SAM file?

</div>

{% include qa.html id="genome_samtools_sorted" %}

<details>
<summary class="btn-solution">Possible Solution</summary>

<pre><code># View first 10 aligned reads
samtools view A_HA_H1.bam | head -10

# First reads all map to position 1 — the file is already sorted

# Remove and recreate the index
rm A_HA_H1.bam.bai
samtools index A_HA_H1.bam

# Convert BAM to SAM
samtools view -o A_HA_H1.sam A_HA_H1.bam
</code></pre>

</details>

---

### Exercise 8 — Multiple Sequence Alignment Practical
{: .mt-4}

<div class="exercise-block" markdown="1">

Using the Mira output `amended_consensus.fasta`, perform the following:

1. Extract the **H3 HA** segments and align them with MAFFT. Do any sequences have gaps in your MSA?
2. Do the same for **A_PB2** segments.
3. What happens if you try to align **all HA segments** (H1, H3, H5, and B) together?

</div>

{% include qa.html id="genome_msa_all_ha" %}

<details>
<summary class="btn-solution">Possible Solution</summary>

<pre><code># Extract H3 HA segments and align
grep -A1 HA_H3 aggregate_outputs/mira-reports/mira_pipeline_test_amended_consensus.fasta | sed "s/--//g" > H3.fasta
mafft H3.fasta > aligned_h3.fasta
</code></pre>

</details>

---

### Exercise 9 — MSA Pipeline Extension
{: .mt-4}

<div class="exercise-block" markdown="1">

Add to your Mira wrapper shell script the commands for extracting and aligning pass-QC sequences for:

- **HA:** A_HA_H1, B_HA, A_HA_H3
- **NA:** B_NA, A_NA_N1, A_NA_N2

</div>

---

### Exercise 10 — BLAST Practical
{: .mt-4}

<div class="exercise-block" markdown="1">

1. Using **NCBI BLAST**, determine which season and region (Americas, Eurasia, Africa, Oceania) each HA segment most closely matches.
2. Using **GISAID BLAST**, how do your results differ?
3. **Discussion:** What are some factors that might influence your BLAST results?

</div>

{% include qa.html id="genome_blast_gisaid_vs_ncbi" %}
