---
layout: page
title: "CLI Introduction – Exercises"
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/06-cli-intro-exercises/
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

## CLI Introduction Exercises

These exercises accompany the **Introduction to BASH** module. They alternate between hands-on practice and knowledge checks.

---

### Exercise 1 — Manual, Flags, and Arguments
{: .mt-4}

View the full manual for each of these commands by running `man <command>`.
Get quick help with the flags for each command by running `<command> --help`.

- `ls`
- `sort`
- `head`
- `vim`
- `date`
- `time`

{% include qa.html id="practical_text_editor" %}

{% include qa.html id="practical_no_manual" %}

---

### Exercise 2 — Command Line Navigation
{: .mt-4}

<div class="exercise-block" markdown="1">

Complete the following steps in order:

1. Open your terminal.
2. Change directory to your home directory (`~`).
3. List the contents of that directory.
4. Make a directory within your home directory called `2026-BIFX-TRAINING`.
5. `cd` to that new directory you just made.
6. Using `..`, cd back "up" to your home directory.
7. **Try tab-complete:** start the command `cd 2026-` then press Tab to complete the full directory name.
8. **Try using your history:** using only the up arrow to move through your recent commands, re-run the command you ran for step 2.

</div>

{% include qa.html id="practical_cd_home" %}

{% include qa.html id="practical_mkdir" %}

---

### Exercise 3 — Network and Downloads
{: .mt-4}

<div class="exercise-block" markdown="1">

Download the samplesheet from the workshop website for the next practical.

**Linux (wget):**
```bash
wget https://raw.githubusercontent.com/CDCgov/id-bioifx-workshop/refs/heads/main/practical/samplesheet.csv
```

**macOS / Unix (curl):**
```bash
curl https://raw.githubusercontent.com/CDCgov/id-bioifx-workshop/refs/heads/main/practical/samplesheet.csv > samplesheet.csv
```

</div>

---

### Exercise 4 — File Viewing and Manipulation (Part 1)
{: .mt-4}

<div class="exercise-block" markdown="1">

1. Ensure your `samplesheet.csv` downloaded properly with `cat`.
2. Copy your samplesheet using `cp` to make `samplesheet_copy.csv`.
3. Rename your `samplesheet_copy.csv` to `samplesheet2.csv` using `mv`.
4. Using `tail`, output the last 20 lines of your samplesheet, and using redirect (`>`), write them to another file called `samplesheet_subset.csv`.
5. Using `head` and then piping into `tail`, output only the **8th line** of `samplesheet.csv`.
6. Sort the samplesheet according to sample ID, numerically, then redirect to a file called `samplesheet_sorted.csv`.

</div>

{% include qa.html id="practical_tail_20" %}

{% include qa.html id="practical_head_pipe_tail" %}

{% include qa.html id="practical_sort_numeric" %}

---

### Exercise 5 — File Viewing and Manipulation (Part 2)
{: .mt-4}

<div class="exercise-block" markdown="1">

7. `cat samplesheet_sorted.csv` to **append** to `samplesheet2.csv`. Cat `samplesheet2.csv` — it should look twice as long!
8. `cat samplesheet_sorted.csv` to **overwrite** `samplesheet2.csv`. Cat `samplesheet2.csv` — it should look just like `samplesheet_sorted.csv`.
9. Rename `samplesheet2.csv` back to `samplesheet_copy.csv`.
10. Using `rm` and glob (`*`) remove both `samplesheet_copy.csv` and `samplesheet_sorted.csv` **without** removing `samplesheet.csv`.

</div>

{% include qa.html id="practical_append_redirect" %}

{% include qa.html id="practical_overwrite_redirect" %}

{% include qa.html id="practical_rm_glob" %}

---

### Exercise 6 — Searching and Text Processing (Part 1)
{: .mt-4}

<div class="exercise-block" markdown="1">

1. Using `wc` on `samplesheet.csv`, how many **lines** are there?
2. Using `wc` on `samplesheet.csv`, how many **characters** are there?
3. Using `cut` on `samplesheet.csv`, output only the Barcode # field.
4. Make a file called `sample_list.txt` by cutting and redirecting unique sample IDs from your fastqs.
5. **Bonus:** Using `tr` and `sort` on `samplesheet.csv`, output the highest barcode number only (no "barcode").

</div>

{% include qa.html id="practical_wc_lines" %}

{% include qa.html id="practical_wc_chars" %}

---

### Exercise 7 — Searching and Text Processing (Part 2)
{: .mt-4}

<div class="exercise-block" markdown="1">

Download the influenza FASTA file:

```bash
# Linux
wget https://raw.githubusercontent.com/CDCgov/id-bioifx-workshop/refs/heads/main/practical/influenza.fasta

# macOS
curl https://raw.githubusercontent.com/CDCgov/id-bioifx-workshop/refs/heads/main/practical/influenza.fasta > influenza.fasta
```

1. Using `grep` with a flag or piping into `wc`, how many times does the sequence `GGGGCGGGG` (4G 1C 4G) appear in your `influenza.fasta`?
2. Using `grep` with the `-A` flag (`--help` if you don't recall what that does), output all the `A_HA_H1` sequences to a file called `H1_HA.fasta`.

</div>

{% include qa.html id="practical_grep_count" %}

---

### Exercise 8 — Searching and Text Processing (Part 3): sed
{: .mt-4}

<div class="exercise-block" markdown="1">

Now we will use `sed` to turn our `H1_HA.fasta` headers into strain names:

```
sed -s "s/find/replace/g"
```

**Goal:** `>3004125441_N8KIRZTI_v1 | A_HA_H1` → `>A/Country/3004125441_N8KIRZTI_v1/2026`

Complete the following parts:

1. **Part 1:** Use `sed -s` to remove the lines with two dashes (`--`) from grep output, redirect to `H1_HA_1.fasta`.
   - Find: `--` → Replace: nothing
2. **Part 2:** Use `sed -s` to replace `>` with `>A/Country/` in `H1_HA_1.fasta`, redirect to `H1_HA_2.fasta`.
   - Since the replacement contains `/`, you will need to use another delimiter character (`%`, `#`) for your sed.
3. **Part 3:** Use `sed -s` to replace ` | A_HA_H1` with `/2026` in `H1_HA_2.fasta`, redirect to `H1_HA_3.fasta`.
   - Again, use an alternative delimiter since the replacement contains `/`.
4. **Part 4:** Rename `H1_HA_3.fasta` to `H1_HA_final.fasta`.

**Intermediate challenge:** Can you do this all in one command using multiple `sed` commands with pipe `|`?

</div>

{% include qa.html id="practical_sed_delimiter" %}

---

### Exercise 9 — Compression and Archives
{: .mt-4}

<div class="exercise-block" markdown="1">

Download, uncompress, and re-compress the following files:

- ```bash
  wget https://raw.githubusercontent.com/CDCgov/id-bioifx-workshop/refs/heads/main/practical/2012704893_273083_v1_H3_PCR_original_R1_001.fastq.gz
  wget https://raw.githubusercontent.com/CDCgov/id-bioifx-workshop/refs/heads/main/practical/2012704893_273083_v1_H3_PCR_original_R2_001.fastq.gz
  ```

Use `ls -lah` (the `-h` flag makes file sizes human-readable) to display the file sizes **before and after** compression.

</div>

{% include qa.html id="practical_gunzip" %}

{% include qa.html id="practical_gzip" %}

---

### Exercise 10 — Permissions and Ownership
{: .mt-4}

<div class="exercise-block" markdown="1">

1. Using `wget` or `curl`, pull down `permissions.txt` at:  
   `https://raw.githubusercontent.com/CDCgov/id-bioifx-workshop/refs/heads/main/practical/permissions.txt`
2. `cat permissions.txt`.
3. Using `chmod`, **remove** read permissions for owner on `permissions.txt`.
4. `cat permissions.txt` — what does it say now?
5. Using `chmod` again, **add** read permissions back to `permissions.txt`.
6. Using the up arrow to load your last `wget` or `curl` command, pull down `permissions.sh` by changing the command's final `.txt` to `.sh`.

</div>

{% include qa.html id="practical_chmod_remove_read" %}

{% include qa.html id="practical_chmod_add_read" %}
