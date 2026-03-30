---
layout: page
title: Intro to Command Line Interface
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/05-cli-intro/
---

{% capture section_overview_1 %}
An introduction to BASH, module objectives, and key terminal definitions.
{% endcapture %}

{% capture section_body_1 %}
## **Introduction to BASH**

### A tour of command line navigation and 100 BASH commands.

## Module Objectives

- Define fundamental terminal definitions, present 100 essential bash command encyclopedia
- Enable you to confidently:
  - Move between directories, list files, and manage folder structures
  - Create, copy, move, rename, delete, and view files
  - Search, filter, and transform text files (samplesheets, FASTAs, FASTQs) using key utilities such as `grep`, `sed`, and `wc`
  - Perform administrative tasks, set file permissions, and interact with remote systems or network resources

### Practical Component

Module will alternate between lecture and practice. Practical materials available at [https://cdcgov.github.io/id-bioifx-workshop/](https://cdcgov.github.io/id-bioifx-workshop/)
{% endcapture %}

{% capture section_overview_2 %}
Core terminal definitions: command prompt, directories, paths, flags, and arguments.
{% endcapture %}

{% capture section_body_2 %}
## **Command Line Navigation: Review**

- **Command prompt:** Text displayed by the shell indicating it is ready to accept a command
- **Directory:** Folder
- **Path:** Exact location of a file or directory in the filesystem
- **`pwd`:** Print Working Directory — show where in the filesystem you are

![Command Prompt]({{ site.baseurl }}/assets/images/presentation3-img02.png){: width="75%"}

![Terminal Example]({{ site.baseurl }}/assets/images/presentation3-img03.png){: width="75%"}

### Flags, Arguments, and Options

- **Flag (or option):** A modifier added to a command (often starting with `-` or `--`) that changes how the command behaves
- **Defaults:** Settings for the program if user provides no modifier
- **Argument:** Additional information provided to a command, such as a filename, directory name, or value to operate on

### Types of Arguments

**Positional arguments:** Arguments defined by order

```bash
cp file.txt backup.txt
```
- `file.txt` is the 1st positional argument (source)
- `backup.txt` is the 2nd positional argument (destination)
- Switching the order changes the behavior

**Binary (Boolean) flags:** Flag is either ON (present) or OFF (absent)
```bash
ls -l
```
- `-l` enables long listing mode, no value required

**Argument (Value) flags:** Requires a value after it
```bash
head –n 5 file.txt
```
- `-n` : flag
- `5` : value

### Manuals and Help

- **Command:** Program
- Difficult for anyone to remember exactly how to use every program on a system
- There are programs that help you use programs!
  - `man` — full manual pages
  - `--help` — quick flag reference
{% endcapture %}

{% capture section_overview_3 %}
Navigating the filesystem: ls, cd, mkdir, rmdir, tree, special symbols, relative vs absolute paths.
{% endcapture %}

{% capture section_body_3 %}
## **Command Line Navigation: Moving in the Filesystem**

| Command | Description |
|---------|-------------|
| `ls` | List directory contents |
| `cd` | Change directory |
| `mkdir` | Create directory |
| `rmdir` | Remove an empty directory |
| `tree` | Show directory structure |

![ls command example]({{ site.baseurl }}/assets/images/presentation3-img04.png){: width="75%"}
![Directory listing]({{ site.baseurl }}/assets/images/presentation3-img05.png){: width="75%"}

### Special Symbols

| Symbol | Meaning |
|--------|---------|
| `~` | Home directory |
| `.` | Current location |
| `..` | "Back" or "up" a directory |

![Navigation with special symbols]({{ site.baseurl }}/assets/images/presentation3-img06.png){: width="75%"}

### BASH Tips

- **Tab-complete:** The shell will try to "guess" what you're typing next if it's an existing filename or directory. Hit Tab to complete the full name for faster navigation.
- **History:** The shell remembers everything you run in your "history" — use the up arrow to go back in history.
- **`cd –`:** Go to the last directory you were in (not necessarily relative to your cwd).



### Relative Paths vs Absolute Paths

**Absolute Path:**
- Full path from the root directory (`/`)
- Always starts with `/`
- Works regardless of current location
- Example: `/home/user/project/data/sample.fastq`

**Relative Path:**
- Path relative to your current directory
- Does NOT start with `/`
- Depends on where you are (`pwd`)
- Example: `data/sample.fastq`
{% endcapture %}

{% capture section_overview_4 %}
Intermediate directory management, special symbols, input/output operators, and shorthand.
{% endcapture %}

{% capture section_body_4 %}
## **Intermediate Directory Management**

- `du` : Disk usage summary (`-h` flag suggested)
- `df` : Display disk space usage for all file-systems mounted by OS

![du and df examples]({{ site.baseurl }}/assets/images/presentation3-img08.png){: width="75%"}

## **Command Line Special Symbols & Shorthand**

### Directories and Pathing

Builtins include special symbols and words that are reserved. Type `help` to see the full list.

| Symbol | Meaning |
|--------|---------|
| `~` | Home directory |
| `.` | Current location |
| `..` | "Back" or "up" a directory |
| `*` | Glob — matches any characters (can represent nothing as well) |

![Glob examples]({{ site.baseurl }}/assets/images/presentation3-img09.png){: width="100%"}

![Glob patterns]({{ site.baseurl }}/assets/images/presentation3-img10.png){: width="100%"}

### Input and Output Operators

| Operator | Meaning |
|----------|---------|
| `>` | Send command output to a file (new or overwrite) |
| `>>` | Append or add command output to a file |
| `<` | Send multiple inputs to a command from a file |
| `|` | Pipe — send output from one command to input of another |

![Redirect examples]({{ site.baseurl }}/assets/images/presentation3-img11.png){: width="75%" .img-center}
![Redirect to file]({{ site.baseurl }}/assets/images/presentation3-img12.png){: width="75%" .img-center}

### Other Special Characters

| Symbol | Meaning |
|--------|---------|
| `;` | Separate multiple commands on a single line |
| `#` | Comment — ignore to the end of line |

![Semicolon and comment]({{ site.baseurl }}/assets/images/presentation3-img13.png){: width="100%"}

### Special Characters in Text Files

- `\t` = tab character in a textfile
- `\n` = newline character in a textfile

![Human view vs shell view]({{ site.baseurl }}/assets/images/presentation3-img14.png){: width="75%"}

![Tab and newline characters]({{ site.baseurl }}/assets/images/presentation3-img15.png){: width="75%"}
![Special character example]({{ site.baseurl }}/assets/images/presentation3-img16.png){: width="75%"}
{% endcapture %}

{% capture section_overview_5 %}
File viewing, sorting, piping, copying, moving, and deleting files.
{% endcapture %}

{% capture section_body_5 %}
## **File Viewing and Manipulation**

### Viewing Files

| Command | Description |
|---------|-------------|
| `cat` | Display file contents |
| `head` | Show first 10 lines of file (change with `-n` flag or `-#`) |
| `tail` | Show last 10 lines of file (change with `-n` flag or `-#`) |
| `vim` | Open text editor |
| `less` | View file content interactively |

![cat, head, tail diagram]({{ site.baseurl }}/assets/images/presentation3-img17.png){: width="75%"}


### Sorting

| Command | Description |
|---------|-------------|
| `sort` | Sort lines in a file |

- Defaults to first column or field, sorting alphabetically
- `-n` tells the command to sort numerically
- `-k 4` tells command to sort according to the fourth field
- `-d ,` tells command to divide fields according to ","

![Sort example 1]({{ site.baseurl }}/assets/images/presentation3-img19.png){: width="50%"}

![Sort example 2]({{ site.baseurl }}/assets/images/presentation3-img20.png){: width="50%"}

![Sort example 3]({{ site.baseurl }}/assets/images/presentation3-img21.png){: width="75%"}

### Piping

`|` = Pipe, or send output from one command to input of another command.

> **Caution:** Not all commands accept stdin.

**Sort the first 10 lines of a file:**
```bash
head samplesheet.csv | sort
```
![Piping example 1]({{ site.baseurl }}/assets/images/presentation3-img22.png){: width="75%"}

**Sort a file then output the first 5 entries alphabetically:**
```bash
sort samplesheet.csv | head -5
```
![Piping example 2]({{ site.baseurl }}/assets/images/presentation3-img23.png){: width="75%"}
![Piping example 3]({{ site.baseurl }}/assets/images/presentation3-img24.png){: width="75%"}

### Copying, Moving, and Deleting

| Command | Description |
|---------|-------------|
| `cp` | Copy files or directories (use `-R` flag for directories) |
| `mv` | Move or rename files |
| `rm` | Remove files or directories — **CAUTION: This is permanent deletion** |
| `touch` | Create an empty file |

![cp example]({{ site.baseurl }}/assets/images/presentation3-img25.png){: width="75%"}

![mv example]({{ site.baseurl }}/assets/images/presentation3-img26.png){: width="75%"}

![rm example]({{ site.baseurl }}/assets/images/presentation3-img27.png){: width="75%"}

![cp -R directory example]({{ site.baseurl }}/assets/images/presentation3-img28.png){: width="75%"}

To remove a directory AND everything in it, use the recursive flag:
```bash
rm –r directory
```
![rm -r example]({{ site.baseurl }}/assets/images/presentation3-img29.png){: width="100%"}
{% endcapture %}

{% capture section_overview_6 %}
Downloading files from the web with wget and curl.
{% endcapture %}

{% capture section_body_6 %}
## **Network and Downloads (Part 1)**

| Command | Description |
|---------|-------------|
| `wget` | Download files from the web |
| `curl` | Transfer data to/from URLs |

- `wget` will pull the file; `curl` will pull the contents
- Use a redirect (`>` or `>>`) with `curl`

![wget example]({{ site.baseurl }}/assets/images/presentation3-img30.png){: width="50%"}

![curl redirect]({{ site.baseurl }}/assets/images/presentation3-img32.png){: width="75%"}

![wget vs curl]({{ site.baseurl }}/assets/images/presentation3-img31.png){: width="50%"}


{% endcapture %}

{% capture section_overview_7 %}
Text processing with wc, cut, uniq, grep, sed, and regular expressions.
{% endcapture %}

{% capture section_body_7 %}
## **Searching and Text Processing**

### wc, cut, uniq

| Command | Description |
|---------|-------------|
| `wc` | Count lines, words, and bytes |
| `cut` | Remove sections from lines |
| `uniq` | Report or filter duplicate lines |

![wc and cut example]({{ site.baseurl }}/assets/images/presentation3-img33.png){: width="50%" }

![cut with duplicates]({{ site.baseurl }}/assets/images/presentation3-img34.png){: width="50%"}

- Cutting by field may not work unless you provide a delimiter (`-d`)
- Piping `cut` into `sort` and `uniq` gives unique values only

![uniq piping example]({{ site.baseurl }}/assets/images/presentation3-img35.png){: width="75%"}

### grep — Search for Text in Files

![grep example]({{ site.baseurl }}/assets/images/presentation3-img36.png){: width="75%"}

- `grep` is case sensitive unless you use `-i`
- Any text is searchable — does not have to match the entire word

![grep case sensitive]({{ site.baseurl }}/assets/images/presentation3-img37.png){: width="75%"}

![grep partial match]({{ site.baseurl }}/assets/images/presentation3-img38.png){: width="75%"}

**Most Useful grep Flags:**

| Flag | Description |
|------|-------------|
| `-v` | Invert match — shows lines that do NOT match |
| `-i` | Ignore case |
| `-r` | Recursive search — searches all files in a directory tree |
| `-n` | Show line numbers for each match |
| `-c` | Count matches — outputs the number of matching lines |

> **Remember:** Flags can be combined! `grep -i –v –c` will ignore case AND invert match and count matches.

![grep flags]({{ site.baseurl }}/assets/images/presentation3-img39.png){: width="75%" }

### sed — Stream Editor for Find/Replace

**Stream mode (output to stdout):**
```bash
sed -s "s/find/replace/g" <file>
```
- Sends replaced line to output stream, can pipe (`|`) or redirect (`>`, `>>`)
- `g` = "global", replaces _all_ matches

**In-place mode (modifies file directly):**
```bash
sed -i "s/find/replace/g" <file>
```
- **Be careful!** Not easy to undo if you make a mistake
- **TIP:** Add `-i .bak` to copy the original file to `original.bak` first

![sed example]({{ site.baseurl }}/assets/images/presentation3-img41.png){: width="75%"}

> **sed is very powerful and it is easy to make inadvertent changes.**

![sed caution]({{ site.baseurl }}/assets/images/presentation3-img42.png){: width="75%"}

**Special character example: TSV to CSV**

![sed tsv to csv]({{ site.baseurl }}/assets/images/presentation3-img43.png){: width="75%"}

**What if the string you want to find or replace has a `/` in it?**

You don't have to use `/` to pass your sed command:
```bash
sed -s "s%find%replace%g"
sed -s "s&find&replace&g"
```

### Regular Expressions (Regex)

Regular expressions are pattern matching tools used by `grep`, `sed`, and other text editors to find and extract text in strings and files.

**Most Important Symbols:**

| Symbol | Meaning |
|--------|---------|
| `.` | Any character |
| `*` | Previous character zero or more times |
| `\+` | Previous character one or more times |
| `[]` | Character sets |

![Regex basics]({{ site.baseurl }}/assets/images/presentation3-img44.png){: width="75%" .img-center}

### Intermediate Regex (`egrep` or `grep –e`)

| Concept | Syntax | Example |
|---------|--------|---------|
| **Anchors** | `^` start, `$` end | `^ERROR` — lines starting with "ERROR" |
| **Character classes** | `[abc]`, `[0-9]` | `user[0-9]+` — user1, user42 |
| **Quantifiers** | `*` (0+), `+` (1+), `{n}` (exact) | `.{8,}` — at least 8 characters |
| **Alternation (OR)** | `\|` | `error\|fail\|critical` |
| **Escaping** | `\.` literal dot, `\*` literal asterisk | `\d+\.\d+` — decimal numbers |

> [www.regex101.com](https://www.regex101.com) is a great resource for checking and testing regex.

![Regex reference]({{ site.baseurl }}/assets/images/presentation3-img45.png){: width="75%" .img-center}
![Regex examples]({{ site.baseurl }}/assets/images/presentation3-img46.png){: width="75%" .img-center}
{% endcapture %}

{% capture section_overview_8 %}
Intermediate text processing with diff, comm, tr, xargs, and a real-world example.
{% endcapture %}

{% capture section_body_8 %}
## **Intermediate Text Processing**

| Command | Description |
|---------|-------------|
| `diff` | Compare files line by line |
| `comm` | Compare sorted files |
| `tr` | Translate or delete characters |
| `xargs` | Build and execute command lines |

![diff and comm]({{ site.baseurl }}/assets/images/presentation3-img47.png){: width="75%"}

![tr and xargs]({{ site.baseurl }}/assets/images/presentation3-img48.png){: width="75%"}

### Putting It All Together: Real World Example

Need a "sample_type" column — replace (sed) end of line (`$`) with `,Test`:

![Real world example 1]({{ site.baseurl }}/assets/images/presentation3-img49.png){: width="100%"}

![Real world example 2]({{ site.baseurl }}/assets/images/presentation3-img50.png){: width="100%"}
{% endcapture %}

{% capture section_overview_9 %}
Networking, SSH, SCP, and remote connections.
{% endcapture %}

{% capture section_body_9 %}
## **Networking and Downloads (Part 2)**

| Command | Description |
|---------|-------------|
| `ping` | Check network connection |
| `ssh` | Connect to remote server |
| `scp` | Copy files via SSH from one server to another |
| `host` | DNS lookup utility |
| `ftp` | File transfer protocol client |

![Networking commands]({{ site.baseurl }}/assets/images/presentation3-img52.png){: width="75%" .img-center}

![SSH example]({{ site.baseurl }}/assets/images/presentation3-img53.png){: width="75%" .img-center}
{% endcapture %}

{% capture section_overview_10 %}
Compression and archiving: tar, gzip, zip, zcat, gunzip, unzip.
{% endcapture %}

{% capture section_body_10 %}
## **Compression and Archives**

### Why Compress?

- NGS generates very large files — raw data (e.g., FASTQ, BAM) can quickly reach GB–TB scale
- Compressed files are faster to transfer — reduced size improves download, upload, and sharing speed
- Best practice for long-term storage — saves disk space and lowers storage and backup costs


### Common Formats

| Format | Description |
|--------|-------------|
| **Tarballs (.tar)** | Bundles multiple files into a single archive (no compression by itself) |
| **Gzip (.gz)** | Common for FASTQ files; fast compression/decompression |
| **Zip archives (.zip)** | Widely supported; combines archiving and compression |
| **Compressed tar (.tar.gz)** | Archive multiple files and compress them in one step. Common for distributing sequencing datasets |

### Compression Commands

| Create / Compress | Extract / Decompress |
|-------------------|---------------------|
| `tar –c` : Create archives | `tar –x` : Extract archives |
| `gzip` : Compress files | `gunzip` : Decompress gzip files |
| `zip` : Create zip archives | `unzip` : Extract zip archives |
| | `zcat` : View compressed files |

![Create commands]({{ site.baseurl }}/assets/images/presentation3-img57.png){: width="75%"}

![Extract commands]({{ site.baseurl }}/assets/images/presentation3-img58.png){: width="75%"}

### Examples

- `gzip` / `pigz` (parallel gzip for many files)

![gzip examples]({{ site.baseurl }}/assets/images/presentation3-img59.png){: width="75%"}

![gunzip examples]({{ site.baseurl }}/assets/images/presentation3-img60.png){: width="75%"}

- `tar` archive and extract:

![tar examples]({{ site.baseurl }}/assets/images/presentation3-img61.png){: width="75%"}

- `zcat` — view compressed contents without uncompressing:

![zcat examples]({{ site.baseurl }}/assets/images/presentation3-img62.png){: width="75%"}

![zcat piping]({{ site.baseurl }}/assets/images/presentation3-img63.png){: width="75%"}
{% endcapture %}

{% capture section_overview_11 %}
File permissions, ownership, and common administrative commands.
{% endcapture %}

{% capture section_body_11 %}
## **Permissions and Ownership**

### Core Concepts

- **Ownership** defines control — each file has a user (owner) and group assigned to it
- **Permissions** control access — Read (r), Write (w), and Execute (x)
- **Three permission levels** — apply separately to owner, group, and others

![Permission concept]({{ site.baseurl }}/assets/images/presentation3-img64.png){: width="75%" .img-center}

### Managing Permissions

| Command | Description |
|---------|-------------|
| `ls -l` | View permissions (owner, group, others: `-rwx`) |
| `chmod` | Change permissions (letters or numbers) |
| `chown` | Change ownership |

**Numeric Permissions:**

| Value | Permission |
|-------|-----------|
| `r = 4` | Read |
| `w = 2` | Write |
| `x = 1` | Execute |

Add values to set permissions:
- `7 = 4+2+1` (rwx)
- `6 = 4+2` (rw-)
- `5 = 4+1` (r-x)
- `-rw-r--r--` → `644` — Owner: read/write, Group & others: read

![chmod examples]({{ site.baseurl }}/assets/images/presentation3-img66.png){: width="75%"}

### Intermediate Permissions and Ownership

| Command | Description |
|---------|-------------|
| `chgrp` | Change group ownership |
| `sudo` | Run command as superuser |
| `umask` | Set default file permissions |
| `id` | Display user identity |
| `whoami` | Show current user |
| `groups` | Show group memberships |
| `passwd` | Change user password |
| `su` | Switch user |
{% endcapture %}

{% capture section_overview_12 %}
System information and process management tools.
{% endcapture %}

{% capture section_body_12 %}
## **System Info & Process Management**

| Command | Description |
|---------|-------------|
| `top` | Display running processes (`htop` for enhanced view) |
| `ps` | Report current processes |
| `kill` | Terminate processes |
| `pkill` | Kill by process name |
| `jobs` | List active jobs |

> Ever need to cancel what you just ran? **Ctrl + C**

![top/htop example]({{ site.baseurl }}/assets/images/presentation3-img67.png){: width="100%"}
{% endcapture %}

{% include activity.html variant="1" title="Introduction & Objectives" overview=section_overview_1 content=section_body_1 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="2" title="CLI Review: Definitions" overview=section_overview_2 content=section_body_2 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="3" title="Filesystem Navigation" overview=section_overview_3 content=section_body_3 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="1" title="Symbols & Shorthand" overview=section_overview_4 content=section_body_4 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="2" title="File Viewing & Manipulation" overview=section_overview_5 content=section_body_5 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="3" title="Network & Downloads" overview=section_overview_6 content=section_body_6 icon="/id-bioifx-workshop/assets/images/presentation3-img54.png" %}
{% include activity.html variant="1" title="Searching & Text Processing" overview=section_overview_7 content=section_body_7 icon="/id-bioifx-workshop/assets/images/presentation3-img40.png" %}
{% include activity.html variant="2" title="Intermediate Text Processing" overview=section_overview_8 content=section_body_8 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}
{% include activity.html variant="3" title="Networking Part 2" overview=section_overview_9 content=section_body_9 icon="/id-bioifx-workshop/assets/images/presentation3-img54.png" %}
{% include activity.html variant="1" title="Compression & Archives" overview=section_overview_10 content=section_body_10 icon="/id-bioifx-workshop/assets/images/presentation3-img56.png" %}
{% include activity.html variant="2" title="Permissions & Ownership" overview=section_overview_11 content=section_body_11 icon="/id-bioifx-workshop/assets/images/presentation3-img65.png" %}
{% include activity.html variant="3" title="System Info & Processes" overview=section_overview_12 content=section_body_12 icon="/id-bioifx-workshop/assets/images/presentation3-img01.png" %}

