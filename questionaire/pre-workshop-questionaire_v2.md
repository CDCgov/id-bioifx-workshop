# Influenza Bioinformatics Pre-Workshop Questionnaire (Technical Focus)

This workshop is a **hands-on, computation-intensive course intended for the person who will perform influenza bioinformatics analyses directly**.  
The questions below help us tailor the course and ensure that participants have the technical capability and system access required.

---

## Section 1 — Computational Background

### 1. How would you describe your day-to-day role with respect to computational work?
- [ ] I routinely perform command-line or scripting–based analyses.
- [ ] I occasionally run bioinformatics workflows but do not maintain systems.
- [ ] I supervise or manage teams that perform bioinformatics analyses.
- [ ] Other (please specify): ___________

### 2. Which operating systems do you actively administer or work in for analysis? (Select all that apply)
- [ ] Linux (Ubuntu, CentOS, Rocky, Debian, etc.)
- [ ] macOS
- [ ] Windows with WSL
- [ ] Windows without WSL
- [ ] Other: __________

### 3. Have you previously installed scientific software that required dependency management (conda, virtualenv, pip, apt, brew, etc.)?
- [ ] Yes, many times
- [ ] Yes, a few times
- [ ] I have used pre-installed tools but have not installed them myself
- [ ] No

---

## Section 2 — Virtualization, Internet, & System Administration

### 4. Have you personally installed and configured any of the following? (Select all that apply)
- [ ] Virtual machines (VirtualBox, VMware, Hyper-V)
- [ ] WSL or WSL2
- [ ] Docker or Singularity/Apptainer containers
- [ ] Remote Linux servers (SSH access, environment setup)
- [ ] None of the above

### 5. If you use VMs or containers, briefly describe what you used them for and what operating system(s) were involved.
*(Short answer)*

### 6. Does your computer have virtualization enabled (required for workshop VM images)?
- [ ] Yes
- [ ] No
- [ ] Not sure — I will check before the workshop
- [ ] I will be using a managed workstation and cannot modify BIOS/UEFI settings

### 7. How would you describe your internet connection’s speed and reliability at the location where you will participate?
- [ ] Fast and reliable (e.g., can easily download files >2 GB)
- [ ] Moderate but stable (downloads work but may take time)
- [ ] Slow or intermittent (frequent dropouts or difficulty downloading large files)
- [ ] I will need offline/low-bandwidth options

---

## Section 3 — Command Line Skills (Practical)

### 8. How frequently do you use a command-line interface for your work?
- [ ] Daily
- [ ] Weekly
- [ ] Occasionally
- [ ] Rarely or never

### 9. Which types of command-line tasks have you performed? (Select all that apply)
- [ ] Navigating the filesystem (cd, ls/dir, mkdir, rm)
- [ ] Editing files using terminal-based editors (nano, vim, emacs)
- [ ] Installing software via package managers (apt, yum, brew, conda, pip)
- [ ] Running or modifying shell scripts (.sh)
- [ ] Using SSH to access remote servers
- [ ] Environment/module management (conda, mamba, virtualenv, environment variables)
- [ ] None of the above

### 10. Please list at least five commands you commonly use.
*(Short answer)*

---

## Section 4 — Required System Self-Check

### 11. Provide your exact operating system version.
Example: `Ubuntu 22.04.3 LTS`, `Windows 11 Pro 22H2`, `macOS 14.3 Sonoma`  
*(Short answer)*

### 12. What is your default shell?
Run one of the following:
- Linux/macOS: `echo $SHELL`
- WSL: `echo $SHELL` within WSL
- Windows PowerShell: note `PowerShell`

Answer: __________

### 13. How much free disk space do you have available for workshop tools?
(Use `df -h` on Linux/macOS/WSL or disk properties on Windows.)  
*(Short answer — numeric value required)*

### 14. If you will use a work laptop, do you have administrative rights to install software and enable virtualization?
- [ ] Yes
- [ ] No
- [ ] I’m not sure — I will confirm with my IT department
- [ ] My organization does not permit local installs

---

## Section 5 — Bioinformatics Experience & Sample Context

### 15. Have you previously analyzed influenza sequencing data?
- [ ] Yes, routinely
- [ ] Yes, occasionally
- [ ] No, but I have analyzed other pathogens
- [ ] No, I am new to pathogen genomics

### 16. Briefly describe a recent analysis you performed, including which tools and computational steps were involved.
*(Short answer)*

### 17. How are influenza samples typically collected, processed, and submitted for sequencing in your country or institution?
*(Short answer — include sample types, collection timing, transport or storage conditions, metadata availability, etc.)*

### 18. Do the sample collection methods or logistics in your setting create any challenges for genetic analyses (e.g., low viral load, long transport times, missing metadata, partial genomes)?
- [ ] Yes — please describe: __________
- [ ] No
- [ ] Not sure

---

## Section 6 — Learning Goals

### 19. What are the most important technical skills you need to develop during this workshop (e.g., VM setup, command-line proficiency, influenza genome assembly, pipeline debugging)?
*(Short answer)*

---
