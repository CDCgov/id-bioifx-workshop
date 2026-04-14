---
layout: page
title: "Bioinformatics Programming – Exercises"
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/08-bifx-programming-exercises/
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

## Bioinformatics Programming Exercises

These exercises accompany the **Intro to Bioinformatics Programming** module. They alternate between hands-on practice and knowledge checks.

---

### Exercise 1 — Vim practical
{: .mt-4}

<div class="exercise-block" markdown="1">

1. Students download the pre-built file from the github

```bash
wget https://raw.githubusercontent.com/CDCgov/id-bioifx-workshop/refs/heads/main/practical/bash_practical_exercises/vim_practical/mem_incorrect.sh
```

2. Use VIM to navigate through it, chmod it, and modify it so that it can run and get the correct output
3. Open the “mem_incorrect.sh” file in VIM
4. Fix the shebang line to run a bash script
5. Modify the “echo” command to fix the typo
6. Delete the line that says “Delete this line”
7. Navigate to the next line, follow the instructions in the file
8. Navigate to the end of the file
9. Save the modified file as
10. Make the file executable
11. Run the script
12. Extra practice: use VIM to create a bash file that lists all the files in a directory that end in .sh files and outputs a message that lists all bash files to stdout

<details>
<summary class="btn-solution">Possible Solution</summary>

<ol>
  <li>Open the “cores_incorrect.sh” file in VIM: <code>vim cores_incorrect.sh</code></li>
  <li>Fix the shebang line to run a bash script: <code>#!/bin/MISTAKE</code> → <code>#!/bin/bash</code> (i, esc)</li>
  <li>Modify the <code>echo</code> command to fix the typo: <code>eecho</code> → <code>echo</code> (navigate using arrows or letter keys, i, esc)</li>
  <li>Delete the line that says “Delete this line”: <code>dd</code></li>
  <li>Navigate to the next line and follow the instructions in the file.</li>
  <li>Delete <code>#</code> where instructed.</li>
  <li>Copy the line with <code>yy</code>.</li>
  <li>Navigate to the end of the file with <code>G</code> and paste the line with <code>p</code>.</li>
  <li>Save the modified file: <code>:wq</code> + Enter.</li>
  <li>Make the file executable: <code>chmod +x mem</code>.</li>
  <li>Run the script: <code>./mem_incorrect.sh</code>.</li>
  <li>Extra practice: create a bash file that lists all <code>.sh</code> files in a directory and outputs a message listing bash files to stdout.</li>
</ol>

</details>

</div>

---

### Exercise 2 — Pseudo Code Practical
{: .mt-4}

<div class="exercise-block" markdown="1">

#1. From a list of numbers, determine the mean

<details>
<summary class="btn-solution">Possible Solution</summary>

<ol>
  <li>Count up the number of entries in the file and store that number as a variable (e.g., <code>total_entries</code>).</li>
  <li>Use a function to iterate through each number and add them line by line until the end of the file, then store that sum as a variable (<code>sum_entries</code>).</li>
  <li>Divide <code>sum_entries</code> by <code>total_entries</code>, and capture the final value as a float so it is not rounded to a whole integer.</li>
</ol>

</details>


#2. Calculate the percentage of numbers in the file that are below 6

<details>
<summary class="btn-solution">Possible Solution</summary>

<ol>
  <li>Instantiate two variables, <code>x</code> and <code>y</code>, and set both to zero (<code>x</code> = count of values below 6, <code>y</code> = count of values 6 or above).</li>
  <li>Write a function to determine whether a value is less than 6.</li>
  <li>Iterate through the list and use each value as input to the function.</li>
  <li>If the condition is true, increment <code>x</code> by 1; if false, increment <code>y</code> by 1.</li>
  <li>Create a new variable <code>z</code> as <code>x + y</code> (total values), then divide <code>x</code> by <code>z</code> and capture the result as a float.</li>
</ol>

</details>

#3. How many different flu subtypes appear in a list?

<details>
<summary class="btn-solution">Possible Solution</summary>

<ol>
  <li>Create an empty list to hold unique subtype values (e.g., <code>unique_list</code>).</li>
  <li>Iterate through the subtype list and check whether each subtype is already in <code>unique_list</code>.</li>
  <li>If it is not present, add it to <code>unique_list</code>.</li>
  <li>Alternative: sort the list and condense to unique values (pipeline approach, e.g., sort/uniq).</li>
</ol>

</details>

#4. Translate this DNA into its possible protein sequences (keeping in mind frames, coding and non-coding)

<details>
<summary class="btn-solution">Possible Solution</summary>

<ol>
  <li>Obtain a codon table for converting DNA codons into amino acids.</li>
  <li>Starting at nucleotide 1, iterate in steps of 3 and translate codons to build a protein sequence.</li>
  <li>Repeat from nucleotide 2 (frame 2).</li>
  <li>Repeat from nucleotide 3 (frame 3).</li>
  <li>Convert the DNA to its reverse complement.</li>
  <li>Repeat translation for the three reverse-complement frames.</li>
</ol>

</details>


</div>

---

### Exercise 3 — Logic and Variables Practical
{: .mt-4}

<div class="exercise-block" markdown="1">

1. Using the ordinal number file on github (ordinal_check.sh)

```bash
wget https://raw.githubusercontent.com/CDCgov/id-bioifx-workshop/refs/heads/main/practical/bash_practical_exercises/logic_and_variable_practical/ordinal_check.sh

```

2. Exercise 1: change the ordinal statement to execute as true if the number is greater than 50 and less than 100
3. Exercise 2: change the ordinal statement to execute as true if the number is less than 25 or greater than 75
4. Exercise 3: change the ordinal statement to execute as true if the number is greater than 1 and less than 10, or greater than or equal to 90 and less than 100
5. Set a variable to be the current working directory. Change directory to the top level directory. Navigate back to the directory you were in using the variable
6. Using the Random number generator file on github (random_number_generator.sh)

<details>
<summary class="btn-solution">Possible Solution</summary>

<ol>
  <li>
    Exercise 1: change the ordinal statement to execute as true if the number is greater than 50 and less than 100.
    <pre><code>if [ "$n" -gt 50 ] && [ "$n" -lt 100 ]; then
  # amend echo statements to reflect exercise instructions
fi</code></pre>
  </li>
  <li>
    Exercise 2: change the ordinal statement to execute as true if the number is less than 25 or greater than 75.
    <pre><code>if [ "$n" -lt 25 ] || [ "$n" -gt 75 ]; then
  # amend echo statements to reflect exercise instructions
fi</code></pre>
  </li>
  <li>
    Exercise 3: change the ordinal statement to execute as true if the number is greater than 1 and less than 10, or greater than or equal to 90 and less than 100.
    <pre><code>if { [ "$n" -gt 1 ] && [ "$n" -lt 10 ]; } || { [ "$n" -ge 90 ] && [ "$n" -lt 100 ]; }; then
  # amend echo statements to reflect exercise instructions
fi</code></pre>
  </li>
  <li>
    Set a variable to the current working directory, change to the top-level directory, then return using the variable.
    <pre><code>thispath="$(pwd)"
cd
cd "$thispath"</code></pre>
  </li>
</ol>
</details>

</div>

---

### Exercise 4 — Loops Practical
{: .mt-4}

<div class="exercise-block" markdown="1">

```bash
mkdir loops_practical && cd loops_practical; for ((i=1;i<=99;i++)); do wget https://raw.githubusercontent.com/CDCgov/id-bioifx-workshop/refs/heads/main/practical/bash_practical_exercises/loops_practical/gato${i}; done
```

1. For every file in the loops_practical directory, if the file is not empty, print the name of the file to stout. (wc - -byte < filename can be used to give the size of a file)
2. For each file in a directory, find out if the file contains a shebang line as the first line, if so, print the filename to stout
3. Find the sick cat! (Hint: execute the files with shebangs!)
4. For every file in the loops_practical directory, if the file is not empty, print the name of the file to stout. (“wc - -byte < filename” can be used to give the size of a file)
5. Find the sick cat! (Hint: execute the files with shebangs!)

<details>
<summary class="btn-solution">Possible Solution</summary>

<ol>
  <li>
    Print each non-empty file name in the <code>loops_practical</code> directory.
    <pre><code>for i in *; do
  bytesize=$(wc --byte &lt; "$i")
  if [ "$bytesize" -gt 0 ]; then
    echo "$i"
  fi
done</code></pre>
  </li>
  <li>
    Find the “sick cat” by executing only non-empty bash-readable files and printing successful file names.
    <pre><code>for i in *; do
  bytesize=$(wc --byte &lt; "$i")
  if [ "$bytesize" -gt 0 ]; then
    if bash "$i" 2&gt;/dev/null; then
      echo "$i"
    fi
  fi
done</code></pre>
  </li>
</ol>
</details>

</div>

---

### Exercise 5 — Pipeline practical
{: .mt-4}

<div class="exercise-block" markdown="1">

```bash
mkdir pipeline_practical && cd pipeline_practical; for i in decode_the_secret_message.txt flu_types.txt secret_message_key.txt; do wget https://raw.githubusercontent.com/CDCgov/id-bioifx-workshop/blob/main/practical/bash_practical_exercises/pipeline_practical/${i} ; done

```

1. List the contents of a directory, pipe that output to word count to find how many files there are (may be helpful to use man wc to find out what wc can do)
2. List the contents of a file, sort the contents and find a list of the unique values
3. Decode the secret message: 1%76q#948^4q5@23q2q492q07&/@i5#q#76
4. Convert all the numbers into letters using the provided variable
5. Reverse the order of the sequence
6. Cut using “/” as delimiter, take the second field
7. convert all the letters into uppercase
8. List the contents of a directory, pipe that output to word count to find how many files there are (may be helpful to use man wc to find out what wc can do)
9. List the contents of the /usr/bin directory, pipe that output to word count to find how many files there are (may be helpful to use “man wc” to find out what wc can do)
10. List the contents of a file, sort the contents and find a list of the unique values (bonus: count the number of unique values and output to screen)
11. Convert all the numbers into letters using the provided conversion
12. convert all the letters into uppercase

<details>
<summary class="btn-solution">Possible Solution</summary>

<ol>
  <li>
    Count files in a directory using a pipe to <code>wc</code>.
    <pre><code>ls | wc</code></pre>
  </li>
  <li>
    Sort a file and return unique values (bonus: count unique values).
    <pre><code>cat flu_types.txt | sort | uniq
cat flu_types.txt | sort | uniq | wc</code></pre>
  </li>
  <li>
    Decode the secret message by converting characters, reversing, cutting field 2 by <code>/</code>, then uppercasing.
    <pre><code>secret_message="$(cat decode_the_secret_message.txt)"
secret_key="$(cat secret_message_key.txt)"
echo "$secret_message" | tr "$secret_key" '123456789@#0%^&q=' | rev | cut -d"/" -f 2 | tr '[:lower:]' '[:upper:]'</code></pre>
  </li>
  <li>
    One-line direct decode example.
    <pre><code>echo "1%76q#948^4q5@23q2q492q07&/@i5#q#76" | tr '123456789@#0%^&q=' '!abehnoprstuwxy_' | rev | cut -d"/" -f 2 | tr '[:lower:]' '[:upper:]'</code></pre>
  </li>
</ol>
</details>

</div>
