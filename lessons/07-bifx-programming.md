---
layout: lesson
title: Intro to Bioinformatics Programming
nav_order: 7
---

{% capture section_overview_1 %}
Bioinformatics programming basics, scripting, and functionality
{% endcapture %}

{% capture section_body_1 %}
## **Introduction to Bioinformatics Programming**

### Key Points

Bioinformatics programming basics, scripting, and functionality

Presenter Name

![Presentation4 Img01]({{ site.baseurl }}/assets/images/presentation4-img01.png){: width="75%"}

{% endcapture %}

{% capture section_overview_2 %}
Key concepts for Disclaimer.
{% endcapture %}

{% capture section_body_2 %}
## **Disclaimer**

{% endcapture %}

{% capture section_overview_3 %}
Trainees will learn scripting basics applicable to any programming language or infrastructure: variables, loops, logic gates, functions, and shebang lines
{% endcapture %}

{% capture section_body_3 %}
## **Module Objectives**

### Key Points

- Trainees will learn scripting basics applicable to any programming language or infrastructure: variables, loops, logic gates, functions, and shebang lines
- Trainees will be able to write simple Bash scripts and customize their shell environment by setting variables, using conditional statements (if/fi), and leveraging loops and aliases for automation and efficiency
- Trainees will understand parallel processing and its utility in optimizing runtime
- Trainees will learn pipe, pipelining, and how it applies to productionalized bioinformatics and ad hoc analyses

{% endcapture %}

{% capture section_overview_4 %}
Commands can be run interactively
{% endcapture %}

{% capture section_body_4 %}
## **Bash Scripting**

### Key Points

Commands can be run interactively

Enter commands one at a time directly in the terminal


- Commands can be saved in a script file
- A script is a text file (e.g., .sh) containing multiple commands
- Scripts can be executed as a program
- Make executable with `chmod +x` script.sh (permissions!) and run with `./script.sh`
- `Echo` : print text to screen
- Shebang line: tells computer how to interpret script


![Presentation4 Img02]({{ site.baseurl }}/assets/images/presentation4-img02.png){: width="75%"}


![Presentation4 Img04]({{ site.baseurl }}/assets/images/presentation4-img04.png){: width="75%"}


{% endcapture %}

{% capture section_overview_5 %}
Vim is a terminal-based text editor
{% endcapture %}

{% capture section_body_5 %}
## **vim**

### Key Points

Vim is a terminal-based text editor


- Vim is a terminal-based text editor
- Common on servers, HPC systems, and remote machines
- Designed for speed and efficiency
- Keyboard-driven (mouse won’t work!)
- Uses different modes
- Commands behave differently depending on the mode
- Highlights syntax usefully
- Vim demo
- Start and exit
    -   `vim file.txt` — open a file
    -   `:w` save
    - `:q` quit
    - `:wq` save & quit
    - `q!` quit without saving
- Modes
    - `i` — insert (edit text)
    - `Esc` — return to normal mode
- Navigation
    - Arrow keys or `h j k l`
    - `gg` top of file
    - `G` bottom of file
    - `:<number>`go to line number
- Editing
    - `dd` delete line
    - `yy` copy line
    - `p` paste
    - `u` undo
- Search
    - `/text` search forward
    - `n` next match

![Presentation4 Img07]({{ site.baseurl }}/assets/images/presentation4-img07.png){: width="25%"}

{% endcapture %}

{% capture section_overview_6 %}
Syntax is the set of rules for writing code
{% endcapture %}

{% capture section_body_6 %}
## **Syntax**

### Key Points

- Syntax is the set of rules for writing code
- Like grammar in a spoken language
    - Strong coffee is good
    - El café fuerte es bueno.
- Different programming languages have different syntax
- The same task looks different in Bash, Python, R, etc.
- These two scripts do the same exact task
- Small differences matter
- Symbols, spacing, and keywords must be used correctly
- Using a text editor or Integrative Development Environment (IDE) can help detect errors
- Errors often come from syntax issues
- Missing characters or incorrect formatting can prevent code from running

![Presentation4 Img08]({{ site.baseurl }}/assets/images/presentation4-img08.png){: width="75%"}

![Presentation4 Img09]({{ site.baseurl }}/assets/images/presentation4-img09.png){: width="75%"}

![Presentation4 Img10]({{ site.baseurl }}/assets/images/presentation4-img10.png){: width="75%"}

{% endcapture %}

{% capture section_overview_7 %}
Focuses on logic, not syntax
{% endcapture %}

{% capture section_body_7 %}
## **Pseudo Code**

### Key Points

- Focuses on logic, not syntax
- Describe what the program does without worrying about language rules
- One pseudocode outline can be implemented in Bash, Python, R, etc.
- Helps plan before coding
- Breaks complex problems into clear, manageable steps
- Improves communication
- Easy to read and discuss with collaborators, even non-programmers

Pseudocode for reverse compliment:

Input sequence = “my sequence”

A change to T

T change to A

G change to C

C change to G

Translate nucleotides in “my sequence”

Reverse the translated “my sequence”

Output “my sequence”

![Presentation4 Img11]({{ site.baseurl }}/assets/images/presentation4-img11.png){: width="25%"}

{% endcapture %}

{% capture section_overview_8 %}
Variables store values like text or numbers
{% endcapture %}

{% capture section_body_8 %}
## **Variables**

### Key Points

- Variables store values like text or numbers
- Commonly used for file names, paths, or sequences
- In syntax example, I set the variable my_sequence to hold “ACTGACTG”
- Assigned without spaces
- Accessed with a $
- Good habit to use “$name” to reference
- Useful for making scripts reusable
- Change a variable once instead of editing multiple commands
- Variables can hold many kinds of things:
- Bash variables are untyped by default: everything is treated like a string (not true for every coding language)
- Numbers are handled through context
- Arrays hold multiple values (also called lists in other languages)
- Variables can even hold the output of another command!
- Subshell
- Current_time as a variable let me run the same code with different results: time changed!
- Choose unique variable names: if you reuse a common variable name, you’ll overwrite it
- Certain variables in certain programming languages are already assigned (file, date, etc)

`name=value` (spaces will cause errors)

Use `$name` to reference the stored value

`VAR=value` : Assign a variable

`$VAR` : Use a variable

`export` : Make variable available to subshells

`read` : Read input from user

`set` : Set or unset shell options

`unset` : Remove variable or function

```bash
#!/bin/bash

set –euo pipefail
```
-e exit on error

-u error on undefined variable

-o pipefail : fail if any command in pipeline fails

![Presentation4 Img12]({{ site.baseurl }}/assets/images/presentation4-img12.png){: width="75%"}

![Presentation4 Img13]({{ site.baseurl }}/assets/images/presentation4-img13.png){: width="75%"}

![Presentation4 Img14]({{ site.baseurl }}/assets/images/presentation4-img14.png){: width="75%"}

![Presentation4 Img15]({{ site.baseurl }}/assets/images/presentation4-img15.png){: width="50%"}

![Presentation4 Img16]({{ site.baseurl }}/assets/images/presentation4-img16.png){: width="50%"}

![Presentation4 Img17]({{ site.baseurl }}/assets/images/presentation4-img17.png){: width="75%"}

{% endcapture %}

{% capture section_overview_9 %}
You can string together multiple commands using and/or logic
{% endcapture %}

{% capture section_body_9 %}
## **Logic: and, or**

### Key Points

- You can string together multiple commands using and/or logic


Command1 && Command2

Command1 \|\| Command2

- Execute command2 if command1 succeeds
- Execute command 2 if command1 fails, otherwise, do not execute command 2

`cd data && echo "Entered data directory" || echo "Could not enter data"`

![Presentation4 Img18]({{ site.baseurl }}/assets/images/presentation4-img18.png){: width="75%"}

![Presentation4 Img19]({{ site.baseurl }}/assets/images/presentation4-img19.png){: width="75%"}

![Presentation4 Img20]({{ site.baseurl }}/assets/images/presentation4-img20.png){: width="75%"}

{% endcapture %}

{% capture section_overview_10 %}
Bash if / then Statements
{% endcapture %}

{% capture section_body_10 %}
## **Logic: if, then**

### Key Points

- Bash if / then Statements
- Used to make decisions in a script
- Run commands only when a condition is true
- Based on command success or a test condition
- Exit status 0 = true, non-zero = false
- Basic structure

```
if [condition]; then

commands

fi
```
- Common if conditional flags
- File tests

`-e file` — path exists

`-f file` — regular file exists

`-d file` — directory exists

`-s file` — file exists and is not empty

- String tests

`-z string` — string is empty

`-n string` — string is not empty

`string1 = string2` — strings are equal

`string1 != string2` — strings are not equal

- Numeric comparisons

`-eq` — equal

`-ne` — not equal

`-lt` — less than

`-le` — less than or equal

`-gt` — greater than

`-ge` — greater than or equal

![Presentation4 Img21]({{ site.baseurl }}/assets/images/presentation4-img21.png){: width="75%"}

![Presentation4 Img22]({{ site.baseurl }}/assets/images/presentation4-img22.png){: width="75%"}


{% endcapture %}

{% capture section_overview_11 %}
if / else / fi handles yes-or-no decisions
{% endcapture %}

{% capture section_body_11 %}
## **Logic: else, case**

### Key Points

- if / else / fi handles yes-or-no decisions
- Run one set of commands or another based on a condition

```
if [ -f data.txt ]; then

echo "File exists"

else

echo "File not found"

fi
```
- case / esac handles multiple choices
- Cleaner than many if / else statements

```
case "$option" in

start) echo "Starting" ;;

stop) echo "Stopping" ;;

*) echo "Unknown option" ;;

esac
```
![Presentation4 Img25]({{ site.baseurl }}/assets/images/presentation4-img25.png){: width="75%"}

![Presentation4 Img26]({{ site.baseurl }}/assets/images/presentation4-img26.png){: width="75%"}

{% endcapture %}

{% capture section_overview_12 %}
Bash does not do math by default
{% endcapture %}

{% capture section_body_12 %}
## **Math**

### Key Points

- Bash does not do math by default
- Arithmetic must be explicitly requested
- Uses integers only by default
- Can use bc –l for floating-point math
- Common operators

\+ add

\- subtract

\* multiply

/ divide

% remainder

- Math is often used for counters
- Loops, file counts, and simple logic

![Presentation4 Img27]({{ site.baseurl }}/assets/images/presentation4-img27.png){: width="25%"}

![Presentation4 Img28]({{ site.baseurl }}/assets/images/presentation4-img28.png){: width="75%"}

{% endcapture %}

{% capture section_overview_13 %}
Loops repeat commands automatically
{% endcapture %}

{% capture section_body_13 %}
## **Loops**

### Key Points

- Loops repeat commands automatically
- Avoid copying and pasting the same command
- Useful for files, samples, and pipelines
- Common in batch processing and automation
- If you have a nanopore run of 24 samples, you want the same assembly and analysis to happen on each sample
- Run until a condition is met
- Based on lists, counters, or logical tests
- When to use loops
- Process multiple files
- Run the same command on many inputs
- Iterate over values
- Sample IDs, numbers, or directories
- Control workflow logic
- Continue until a condition changes

__for / do / done__

- Loop over a list of values

```
for file in *.txt; do

    echo "$file"

done
```
__while__

- Loop while a condition is true

```
while read line; do

    echo "$line"

done < sorting_example.txt
```

```
i=1

while (( i <= 5 )); do

    echo "Count: $i"

    i=$((i + 1))
done
```
- Loops are powerful but can cause problems
- Infinite loops occur when conditions never change
    - Example: while true; do ... done
- Forgetting to update loop variables
- Counters or conditions must change inside the loop
- Easy ways to stop a runaway loop
- Ctrl + C to interrupt
- Test with echo before running real commands

![Presentation4 Img29]({{ site.baseurl }}/assets/images/presentation4-img29.png){: width="25%"}

![Presentation4 Img30]({{ site.baseurl }}/assets/images/presentation4-img30.png){: width="75%"}

![Presentation4 Img31]({{ site.baseurl }}/assets/images/presentation4-img31.png){: width="75%"}

![Presentation4 Img32]({{ site.baseurl }}/assets/images/presentation4-img32.png){: width="75%"}

{% endcapture %}

{% capture section_overview_14 %}
A nested loop is a loop inside another loop
{% endcapture %}

{% capture section_body_14 %}
## **Nested Loops**

### Key Points

- A nested loop is a loop inside another loop
- The inner loop runs completely for each iteration of the outer loop

```
for i in 1 2 3
do
    for j in A B
    do
        echo “$i $j”
    done
done
```
OUTPUT:
```
1 A
1 B
2 A
2 B
3 A
3 B
```


Outer loop runs 3 times

Inner loop runs 2 time for each outer iteration

Total executions: 3x2=6

{% endcapture %}

{% capture section_overview_15 %}
Functions group related commands
{% endcapture %}

{% capture section_body_15 %}
## **Functions**

### Key Points

Functions group related commands

- Package repeated logic into a single unit
- Improve script organization and make long scripts easier to read and maintain
- Defined once, reused many times
- Should have meaningful names to describe what the function does
- Function called reverse_complement
    - `$1` is the first argument passed to the function
    - `tr` performs base complementation
- `rev` reverses the sequence
- Function output goes to script output, like a command
- If you notice that you are writing the same code over and over, it can be useful to package that part as a function
    - then replace the repeats with said function
    - DRY = Don’t Repeat Yourself
- You define the arguments for a function, so it is useful to remember the variables you have already used and make sure not to overwrite them or cause logic errors in the script
- Can define the output of a function as a variable, output to screen, or even a logic evaluation (true/false)

![Presentation4 Img33]({{ site.baseurl }}/assets/images/presentation4-img33.png){: width="25%"}

![Presentation4 Img34]({{ site.baseurl }}/assets/images/presentation4-img34.png){: width="75%"}

![Presentation4 Img35]({{ site.baseurl }}/assets/images/presentation4-img35.png){: width="75%"}

{% endcapture %}

{% capture section_overview_16 %}
Common Bash Errors
{% endcapture %}

{% capture section_body_16 %}
## **Errors**

### Key Points

- Common Bash Errors
    - Syntax errors
    - Missing do, done, then, or fi
    - Extra or missing brackets [ ]
    - Missing or extra “ “ ( )
- Infinite loops
    - Loop condition never changes
    - Missing counter update or exit condition
- Permission errors
    - Script not executable (chmod +x script.sh)
    - No access to files or directories
- Variable mistakes
    - Using $var before it is set
    - Missing $ when referencing a variable
- A good IDE can help with many of these syntax errors, because it will color code things, make suggestions about what might be common fixes

{% endcapture %}

{% capture section_overview_17 %}
Start with Pseudocode!
{% endcapture %}

{% capture section_body_17 %}
## **Debugging Bash scripts**

### Key Points

- Start with Pseudocode!
- Run in debug mode
    - `bash -x script.sh` shows each command as it runs
- Print values to check logic
- Use `echo "$variable"` inside loops or conditions
- Test commands step by step
- Run lines manually in the terminal
- Start simple and build up
- Confirm each part works before combining commands

![Presentation4 Img36]({{ site.baseurl }}/assets/images/presentation4-img36.png){: width="75%"}

{% endcapture %}

{% capture section_overview_18 %}
Standard Output (stdout)
{% endcapture %}

{% capture section_body_18 %}
## **Standard Output and Standard Error**

### Key Points

- Standard Output (stdout)
    - Normal program output (results, messages)
    - File descriptor 1
- Standard Error (stderr)
    - Error, logging, and warning messages
    - File descriptor 2
- Allows errors to be handled differently from results
- Useful for scripting and debugging: redirect output and errors independently
- Both go to the terminal by default, but can be redirected separately or together
- Common redirection operators
    - `>` redirect stdout
    - `2>` redirect stderr
    - `| tee` : writes standard input to standard output
- Useful patterns
    - Save results while still seeing errors
    - Suppress errors during batch processing
- Example
`command > output.txt 2> error.log`

{% endcapture %}

{% capture section_overview_19 %}
Pipelines connect commands together
{% endcapture %}

{% capture section_body_19 %}
## **Pipelines**

### Key Points

- Pipelines connect commands together
- Output of one command becomes input to the next
- Use the pipe symbol `|`
- Pass data through a sequence of tools
- Each tool does one job well
- Common in data processing
- Text files, FASTQ files, and command output
- Bioinformatic pipelines grow from this concept
- Example pseudo code:
```
#!/bin/bash
demultiplex > fastq
genome assembly on fastq > fasta
update database with genome assembly output
curate assembly fastas
```
- Pipelines within pipelines:
- Genome Assembly: MIRA
`check inputs | combine fastqs | subsample reads | trim barcodes | trim primers | run IRMA | check IRMA output | combine output | annotate | create figures`

![Presentation4 Img37]({{ site.baseurl }}/assets/images/presentation4-img37.png){: width="75%"}

![Presentation4 Img38]({{ site.baseurl }}/assets/images/presentation4-img38.png){: width="75%"}

{% endcapture %}

{% capture section_overview_20 %}
Two common approaches
{% endcapture %}

{% capture section_body_20 %}
## **Parallel processing**

### Key Points

- Two common approaches
    - Task parallelism: same command on many inputs
    - Data parallelism: split one dataset into parts
- Within tools (multi-threaded software)
- Across tools (running jobs simultaneously)
- Common Bash patterns
    - Background jobs (&)
    - Job control with wait
- Common bioinformatics tools support multithreading
    - Use flags like -t, -p, or –threads
    - `bwa mem -t 8 ref.fa reads.fq > aln.sam`

{% endcapture %}

{% capture section_overview_21 %}
history : Show command history
{% endcapture %}

{% capture section_body_21 %}
## **More useful tools and shortcuts**

### Key Points

`history` : Show command history

`!!` : Repeat last command

`!n` : Run nth command from history

`alias` : Create command shortcut

`unalias` : Remove alias

`clear `: Clear terminal screen

`man` : Display command manual

`help` : Show built-in help

`date` : Show or set system date

`time` : Show the runtime of the following command

`dos2unix` : convert Windows file to readable Unix file, remove carriage returns

Bash tip! Ctrl+r to SEARCH your history in command line!

![Presentation4 Img39]({{ site.baseurl }}/assets/images/presentation4-img39.png){: width="75%"}

![Presentation4 Img40]({{ site.baseurl }}/assets/images/presentation4-img40.png){: width="75%"}

![Presentation4 Img41]({{ site.baseurl }}/assets/images/presentation4-img41.png){: width="75%"}

![Presentation4 Img42]({{ site.baseurl }}/assets/images/presentation4-img42.png){: width="75%"}

![Presentation4 Img43]({{ site.baseurl }}/assets/images/presentation4-img43.png){: width="75%"}

![Presentation4 Img44]({{ site.baseurl }}/assets/images/presentation4-img44.png){: width="75%"}

{% endcapture %}

{% capture section_overview_22 %}
Bash scripting differs from other coding languages
{% endcapture %}

{% capture section_body_22 %}
## **Higher level coding languages**

### Key Points

- Bash scripting differs from other coding languages
- Abstract away low-level details
- Manage memory, data types, and errors automatically
- Can be compiled into binary
- More expressive and readable
- Fewer lines of code to perform complex tasks
- Rich ecosystems and libraries
- Built-in tools for data analysis, visualization, and networking

{% endcapture %}

{% capture section_overview_23 %}
Group data and actions together
{% endcapture %}

{% capture section_body_23 %}
## **Object oriented programming**

### Key Points

- Group data and actions together
- Similar to treating a file + its operations as one unit
- Classes act like templates
- Define a “sample,” “read set,” or “experiment” once
- Objects represent real things
- Each object holds its own data and methods
- Bash: “Run commands on files”
- Python/R: “Create objects, operate on data”

{% endcapture %}

{% capture section_overview_24 %}
Logic becomes complex
{% endcapture %}

{% capture section_body_24 %}
## **When to stop using BASH**

### Key Points

- Logic becomes complex
- Many nested loops, if/else, or long one-liners that are hard to read
- Data structures are needed
- Lists of samples, tables, dictionaries, or metadata don’t fit cleanly in Bash
- Error handling gets messy
- Too many `&&`, `||`, and manual checks for failures
- Scripts grow large
- Files longer than ~100–200 lines become difficult to maintain
- You need reproducibility and testing
- Unit tests, versioned packages, and structured logging are easier in Python/R
- Parallelization becomes necessary
- Wrap the bash in a workflow manager like snakemake, wdl, or nextflow
- Visualization is needed
- Better packages and libraries in Python and R
- Other coding languages or packages exist to better handle specific use-cases (biopython, etc)

{% endcapture %}

{% capture section_overview_25 %}
As workflows grow, reuse becomes important
{% endcapture %}

{% capture section_body_25 %}
## **Packages and tools!**

### Key Points

- As workflows grow, reuse becomes important
- Copy-pasting scripts leads to errors and drift
- Packages bundle code and functionality
- Install once, use everywhere
- Tools provide standard, tested solutions
- Avoid rewriting common tasks
- Utilize code written by others that is optimized for a certain task
- Easier collaboration and reproducibility
- Others can install the same package and get the same results
- Use Bash to orchestrate tools (in a pipeline)

{% endcapture %}

{% include activity.html variant="1" title="Part 1: Introduction to Bioinformatics Programming" overview=section_overview_1 content=section_body_1 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="2" title="Part 2: Disclaimer" overview=section_overview_2 content=section_body_2 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="3" title="Part 3: Module Objectives" overview=section_overview_3 content=section_body_3 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="1" title="Part 4: Bash Scripting" overview=section_overview_4 content=section_body_4 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="2" title="Part 5: vim" overview=section_overview_5 content=section_body_5 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="3" title="Part 6: Syntax" overview=section_overview_6 content=section_body_6 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="1" title="Part 7: Pseudo Code" overview=section_overview_7 content=section_body_7 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="2" title="Part 8: Variables" overview=section_overview_8 content=section_body_8 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="3" title="Part 9: Logic: and, or" overview=section_overview_9 content=section_body_9 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="1" title="Part 10: Logic: if, then" overview=section_overview_10 content=section_body_10 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="2" title="Part 11: Logic: else, case" overview=section_overview_11 content=section_body_11 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="3" title="Part 12: Math" overview=section_overview_12 content=section_body_12 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="1" title="Part 13: Loops" overview=section_overview_13 content=section_body_13 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="2" title="Part 14: Nested Loops" overview=section_overview_14 content=section_body_14 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="3" title="Part 15: Functions" overview=section_overview_15 content=section_body_15 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="1" title="Part 16: Errors" overview=section_overview_16 content=section_body_16 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="2" title="Part 17: Debugging Bash scripts" overview=section_overview_17 content=section_body_17 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="3" title="Part 18: Standard Output and Standard Error" overview=section_overview_18 content=section_body_18 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="1" title="Part 19: Pipelines" overview=section_overview_19 content=section_body_19 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="2" title="Part 20: Parallel processing" overview=section_overview_20 content=section_body_20 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="3" title="Part 21: More useful tools and shortcuts" overview=section_overview_21 content=section_body_21 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="1" title="Part 22: Higher level coding languages" overview=section_overview_22 content=section_body_22 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="2" title="Part 23: Object oriented programming" overview=section_overview_23 content=section_body_23 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="3" title="Part 24: When to stop using BASH" overview=section_overview_24 content=section_body_24 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
{% include activity.html variant="1" title="Part 25: Packages and tools!" overview=section_overview_25 content=section_body_25 icon="/id-bioifx-workshop/assets/images/presentation4-img01.png" %}
