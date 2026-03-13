---
layout: lesson
title: "Bioinformatics Programming – Exercises"
nav_order: 8
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
2. Use VIM to navigate through it, chmod it, and modify it so that it can run and get the correct output
3. Open the “cores_incorrect.sh” file in VIM
4. Fix the shebang line to run a bash script
5. Modify the “echo” command to fix the typo
6. Delete the line that says “Delete this line”
7. Navigate to the next line, follow the instructions in the file
8. Navigate to the end of the file
9. Save the modified file as
10. Make the file executable
11. Run the script
12. Extra practice: use VIM to create a bash file that lists all the files in a directory that end in .sh files and outputs a message that lists all bash files to stdout
13. Open the “cores_incorrect.sh” file in VIM > vim cores_incorrect.sh
14. Fix the shebang line to run a bash script #!/bin/MISTAKE  #!/bin/bash (i, esc)
15. Modify the “echo” command to fix the typo eecho echo (navigate using arrows or letter keys, i, esc)
16. Delete the line that says “Delete this line” dd
17. Navigate to the next line, follow the instructions in the file delete #, copy line with vv
18. Navigate to the end of the file G, paste line with p
19. Save the modified file as :wq enter
20. Make the file executable chmod +x mem
21. Run the script ./mem_incorrect.sh

</div>

---

### Exercise 2 — Pseudo Code Practical
{: .mt-4}

<div class="exercise-block" markdown="1">

1. From a list of numbers, determine the mean
2. Calculate the percentage of numbers in the file that are below 6
3. How many different flu subtypes appear in a list?
4. Translate this DNA into its possible protein sequences (keeping in mind frames, coding and non-coding)
5. From a list of numbers, determine the mean Possible solution: a. Count up the number of entries in the file, store that number as a variable (e.g. total_entries) b. Use a function to go through each of the numbers and add them up, line by line until you reach the end of the file, then store that number as a variable (sum_entries) c. Divide the sum_entries by the total_entries, but make sure to capture the final value as a “float” so that it is not rounded to the nearest whole integer
6. Calculate the percentage of numbers in a list that are below 6
7. Calculate the percentage of numbers in a list that are below 6Possible solution:a. Instantiate two variables, x and y set them equal to zero to begin (x is number of values less than six, y is number of values greater than six)b. Write a function to determine whether a value is less than 6c. Iterate through the list, using each number as an input to the function i. If the value is true, increment x by “1” ii. If the value is false, increment y by “1”d. Create a new variable, z, which is the sum of x and y (total number of values)e. Divide x by z, capture the result as a float
8. How many different flu subtypes appear in a list?Possible solution:a. Create a new empty list to hold unique variables (e.g. unique_list)b. Iterate through the flu subtype list, comparing the value to the unique list. If the subtype is not in the empty list, add itPossible Solution:a. Take the list, sort it, and condense it to unique variables (see the pipeline practical!)
9. Translate this DNA into its possible protein sequences (keeping in mind frames, coding and non-coding)Possible solution:a. Obtain a codon table for converting DNA codons to amino acidsb. Starting at the first nucleotide, iterate through the sequence by three, and use the codon table to create a protein sequencec. Starting at the second nucleotide, repeat step bd. Starting at the third nucleotide, repeat step be. Convert the DNA into its reverse complement (can expand here based on the steps in the lecture) f. Repeat steps b through d

</div>

---

### Exercise 3 — Logic and Variables Practical
{: .mt-4}

<div class="exercise-block" markdown="1">

1. Using the ordinal number file on github (ordinal_check.sh)
2. Exercise 1: change the ordinal statement to execute as true if the number is greater than 50 and less than 100
3. Exercise 2: change the ordinal statement to execute as true if the number is less than 25 or greater than 75
4. Exercise 3: change the ordinal statement to execute as true if the number is greater than 1 and less than 10, or greater than or equal to 90 and less than 100
5. Set a variable to be the current working directory. Change directory to the top level directory. Navigate back to the directory you were in using the variable
6. Using the Random number generator file on github (random_number_generator.sh)
7. Exercise 1: change the ordinal statement to execute as true if the number is greater than 50 and less than 100if [ “$n” –gt 50 && “$n” –lt 100 ]; then (amend echo statements to reflect exercise instructions)
8. Exercise 2: change the ordinal statement to execute as true if the number is less than 25 or greater than 75if [ “$n” –lt 25 ] || [ “$n” –gt 75 ]; then (amend echo statements to reflect exercise instructions)
9. Exercise 3: change the ordinal statement to execute as true if the number is greater than 1 and less than 10, or greater than or equal to 90 and less than 100if [ “$n” –gt 1 ] && [ “$n” –lt 10 ] || [ “$n” –ge 90 ] && [ “$n” –lt 100 ]; then (amend echo statements to reflect exercise instructions)
10. Set a variable to be the current working directory. Change directory to the top level directory. Navigate back to the directory you were in using the variable in one commandPossible solution:
11. > thispath=”$(pwd)”
12. > cd
13. > cd $thispath

</div>

---

### Exercise 4 — Loops Practical
{: .mt-4}

<div class="exercise-block" markdown="1">

1. For every file in the loops_practical directory, if the file is not empty, print the name of the file to stout. (wc - -byte < filename can be used to give the size of a file)
2. For each file in a directory, find out if the file contains a shebang line as the first line, if so, print the filename to stout
3. Find the sick cat! (Hint: execute the files with shebangs!)
4. For every file in the loops_practical directory, if the file is not empty, print the name of the file to stout. (“wc - -byte < filename” can be used to give the size of a file)for i in *; do bytesize=$(wc --byte < $i); if [ "$bytesize" -gt 0 ]; then echo $i; fi;done
5. Find the sick cat! (Hint: execute the files with shebangs!)for i in *; do bytesize=$(wc --byte < $i); if [ "$bytesize" -gt 0 ]; then if bash $i 2>/dev/null; then echo $i; fi; fi; done

</div>

---

### Exercise 5 — Pipeline practical
{: .mt-4}

<div class="exercise-block" markdown="1">

1. List the contents of a directory, pipe that output to word count to find how many files there are (may be helpful to use man wc to find out what wc can do)
2. List the contents of a file, sort the contents and find a list of the unique values
3. Decode the secret message: 1%76q#948^4q5@23q2q492q07&/@i5#q#76
4. Convert all the numbers into letters using the provided variable
5. Reverse the order of the sequence
6. Cut using “/” as delimiter, take the second field
7. convert all the letters into uppercase
8. List the contents of a directory, pipe that output to word count to find how many files there are (may be helpful to use man wc to find out what wc can do)Possible solution:ls | wc
9. List the contents of the /usr/bin directory, pipe that output to word count to find how many files there are (may be helpful to use “man wc” to find out what wc can do)
10. List the contents of a file, sort the contents and find a list of the unique values (bonus: count the number of unique values and output to screen)Possible solution: cat flu_types.txt | sort | uniqcat flu_types.txt | sort | uniq | wc
11. Convert all the numbers into letters using the provided conversion
12. convert all the letters into uppercasePossible solution:> secret_message=“$(cat decode_the_secret_message.txt)”> secret_key=“$(cat secret_message_key.txt)”> echo $secret_message | tr $secret_key | rev | cut -d"/" -f 2 | tr '[:lower:]' '[:upper:]'Possible solution:> echo “1%76q#948^4q5@23q2q492q07&/@i5#q#76” | tr '123456789@#0%^&q=' '!abehnoprstuwxy_' | rev | cut -d"/" -f 2 | tr '[:lower:]' '[:upper:]'

</div>
