---
layout: page
title: Containers and Registries
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/10-container-registries/
---
<<<<<<< HEAD
## Introduction to Containers and Common Bioinformatic Tools

### Key Points

Dockerhub and Quay.io, using containers to run programs, and learning basic tools

Logan Fink

## Module Objectives

- Trainees will learn what containers are and how they differ from other virtual environments
- Trainees will understand the flags to remove a container, mount a volume, and define usergroups for a docker container
- Trainees will learn how to ensure that data persists on their system after a container is run and removed
- Trainees will be able to identify the differences between container software providers and select an appropriate system for use within their laboratory

## Virtualization

Containerization is a way to allocate resources on a system in a very compartmentalized way
- Virtual machines
	- Hypervisor
	- Maintaining an environment that partitions a host machine
- Containers
	- Individual software
	- Dependencies included
	- Reproducible environment
	- “Works on my machine”

## Containerization Software

Different containerization software exists to run containers

- Docker
- Apptainer (Formerly Singularity)
- ECR
- Podman

There are advantages and disadvantages to each

## Root Privileges

Running Docker requires root access
Depending on the IT restrictions available at your site, access to certain container software may be limited 
Root privileges are not required by Apptainer, and Podman 

## User Groups

`-u $(id -u):$(id -g)`

By default, when Docker containers are run, they are run as the root user. 
To ensure files can be accessed, read and written to by the local user and machine and not just root, the -u flag sets the container's user and group based on the user and group from the local machine, resulting in the correct file ownership.

## Volumes

`-v $PWD:/data`

By default, containers are isolated environments.
When a container is removed, so is the data inside it, unless the user ensured continued access.
If the data is exported to std out, it will remain there, but the data can also be captured in a volume which is mounted from the home system ($PWD, current working directory) onto the container (/data, a folder within the container).
Data which is generated in or moved to the volume will persist on the host system even after the container has been deleted.

## Running Containers

Containers can be run in interactive mode 
- The flag for this is: -it
	- The i stands for interactive
	- The t stands for a pseudo TTY, that offers basic input/output
Containers can be called and given a specific command to run
Removal of containers that are no longer running saves space your system, but persistent containers can be called and used again, and any changes that were made during that session will remain

## OS Differences

Containerization allows users to specify whatever operating system they would like to use within the container, whether that matches the host system or not

![Presentation9 Img01]({{ site.baseurl }}/assets/images/presentation9-img01.PNG){: width="75%"}

## Container Versioning

- Versions are specified in container naming/tags as a convention for noting which version of a software is in that container
- “Latest” tag is less useful than more specific semantic versioning of a container, i.e. 1.1.0 since this will be more easily trackable and revertable (“latest” must be assigned, and authors do not always keep track or update the latest track, which can lead to problems downstream)

![Presentation9 Img02]({{ site.baseurl }}/assets/images/presentation9-img03.PNG){: width="75%"}

## Repositories

- [Dockerhub](https://hub.docker.com/)
- [Quay.io](https://quay.io/)

It is important to use trusted sources of containers
	- Reputable institutions ([StaPH-B](https://hub.docker.com/u/staphb), etc.)

![Presentation9 Img03]({{ site.baseurl }}/assets/images/presentation9-img02.PNG){: width="75%"}

## Common Bioinformatic Tools

- [Fastqc](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/), [multiqc](https://github.com/MultiQC/MultiQC)
- [Kraken2](https://github.com/DerrickWood/kraken2)
- [Docker](https://docs.docker.com/engine/install/ubuntu/#prerequisites)
- [Singularity](https://docs.sylabs.io/guides/4.1/user-guide/quick_start.html#quick-installation-steps)
- [Nextflow](https://docs.seqera.io/nextflow/)
- [Sra-toolkit](https://github.com/ncbi/sra-tools)
- [Samtools](https://github.com/ncbi/sra-tools)
- Bcl2fastq [(user guide)](https://support.illumina.com/content/dam/illumina-support/documents/documentation/software_documentation/bcl2fastq/bcl2fastq_letterbooklet_15038058brpmi.pdf)
- [Dorado](https://github.com/nanoporetech/dorado/)
- [Nextstrain](https://github.com/nextstrain)
- [Nanoplot](https://github.com/wdecoster/NanoPlot)

## Bcl2fastq, Dorado

Bcl2fasta
- Illumina software for creating fastq files from bcl files (clustering photos to sequence)
- Demultiplexing

Dorado
- Software for basecalling ONT reads from fast5 files
- Demultiplexing, alignment, trimming, correction, polishing 

## FastQC, MultiQC, and Nanoplot

- Quality control softwares that allow for viewing of sequencing data associated with sample quality
- Aggregate Q scores across reads
- Expected distribution of bases, visualizing adapter removal
- Visual representations of sequencing quality

## Kraken2

- Used for classifying reads to the most specific level of certainty within a taxonomic ranking scheme
- Dependent on a database

![Presentation9 Img04]({{ site.baseurl }}/assets/images/presentation9-img04.PNG){: width="75%"}

## SRA-ToolKit

- Tools and libraries for using data in the INSDC Sequence Read Archives (SRA)
- Allows for downloading of NCBI data easily using command line
- SRA Accession numbers can be used to download data
	- Basic commands
	- prefetch
	- Fasterq-dump

## Samtools

- A set of tools for analyzing and working with sequencing data
- Samtools
	- Reading, writing, indexing, viewing, editing and working with files in SAM, BAM, CRAM format
- BCFTools
	- Reading, writing, BCF2, VCF, gVCF files for filtering and calling SNPs and short indels
- HTSlib
	- A C library for reading and writing high-throughput sequencing data

## Nexstrain

- A set of tools to create phylogenies and visualize genomic sequencing data 
- Augur
	- Filter, align, tree build, refine, export
- Auspice
	- Visualization program for viewing trees and metadata overlays
- Can build a visualization with in- house data or use a preconfigured build

## Nextflow

- Software for running containers in orchestrated ways, developing pipelines that optimize parallelization and create faster and reproducible ways to generate data
- Modular for ease of updating and changing
- Workflow tracking for troubleshooting and quality assurance
- Configurability 
	- Config files for pipeline variable maintenance
- There exists a set of best-practice values for coding with, using, and contributing to nextflow called nf-core

## Docker, Apptainer, Podman

- Softwares that run Docker containers
- Based on the security restrictions, one container may be a better fit for a user’s organization
=======

{: title}

---

## Module Objectives
- Understand the fundamentals of virtual environments
- Understand basic use of environment management software (`venv` and `conda` / `mamba` / `pixi`)

## Computer Environment Basics
Use the interactive diagram below to learn more about how software and their dependencies are managed in a typical computing environment.
<div style="border: 1px solid #ccc; border-radius: 6px; padding: 12px;">
  {% include comp-env/diagram-1.html %}
</div>

## Environment Management Programs
Managing software, dependencies, and environments on a single machine can quickly become complex, especially when different projects require different versions of the same package. Environment management programs help by creating and maintaining isolated environments, each with their own set of dependencies, so that changes in one project do not break another.
Many environment managers are language-specific - for example, `venv` and `pip` for Python, `renv` for R, `Bundler` for Ruby, and `Maven` or `Gradle `for Java. Others are more language-agnostic and can manage dependencies across multiple ecosystems - e.g., `conda`, `mamba`, and `pixi`. This module will focus on `venv` for lightweight Python environment management, and `conda` / `mamba` / `pixi` for more flexible, cross-language environment management.

### Venv
**Venv** is a lightweight, python-specific environment management tool that facilitates the **isolation of python libraries, NOT the python executable**.

As shown in the diagram below, the `venv` does not change which Python executable is used. Instead, it changes the path to the Python module library.
<div style="border: 1px solid #ccc; border-radius: 6px; padding: 12px;">
  {% include comp-env/diagram-2.html %}
</div>

#### Basic Usage
The code below shows an example of basic `venv` use on the command line.
```bash
# Create and activate environment
python -m venv myenv
source myenv/bin/activate
# Install modules
pip install numpy<2 pandas=1.5.0

# Run script
Python script.py

# Deactivate (close) environment
deactivate
```

#### Sharing environments
Environments can be recreated with `venv` using `pip freeze`. This creates a list of module requirements that can be reinstalled with `pip`. See the example below:
```bash
# Create sharable requirements file
pip freeze > requirements.txt

# Install via requirements file
pip install –r requirements.txt
```

<br>
Example of `requirements.txt`:
```
numpy==1.18
pandas==1.5.0
```


### Conda / Mamba / Pixi
Conda, Mamba, and Pixi support multiple languages (Python, Java, C++, etc.,) and binaries. Manage **BOTH** the executables and their dependencies.


As shown in the diagram below, `conda` (also `mamba` and `pixi`) changes both the Python executable and module library that is used, thus providing a more *isolated* environment.
<div style="border: 1px solid #ccc; border-radius: 6px; padding: 12px;">
  {% include comp-env/diagram-3.html %}
</div>

#### Conda vs Mamba vs Pixi
The tables below outlines key differences between each management tool.

| Feature | Conda | Mamba | Pixi |
|---|---|---|---|
| Initial release date | 2012 | 2019 | 2023 |
| Ecosystem | Conda | Conda | Conda + PyPI |
| Solver speed | Slow | Fast | Fast |
| Environment scope | Global / named | Global / named | Project-local |
| Config format | environment.yml | environment.yml | pixi.toml |
| Reproducibility | Medium | Medium | High |
| Drop-in replacement for Conda | — | Sometimes | No |

| Feature | Conda | Miniconda | Mamba | Micromamba |
|---|---|---|---|---|
| Drop-in replacement for Conda | — | Yes | Yes | No |
| Packages included | 600+ | 130+ | 89 | 0 |
| Approx. install size (GB) | 9.7 | 0.9 | 0.4 | 0.05 |

- Miniconda is Conda but with fewer base packages
- Micromamba is an executable binary of Mamba with no base packages
- **Micromamba is recommended for most applications**

#### Micromamba Shell Configuration
Conda, Mamba, and Miniconda are not compiled — they rely on a Python interpreter and run in the current shell. Micromamba, on the other hand, is a compiled binary executable that requires no interpreter and runs in a subshell. **The subshell output must be interpreted by the current shell for changes to be applied to the environment!** Micromamba solves this by wrapping the binary in shell functions.

Add this to your `.bashrc` file to make this occur on login:
```
eval "$(micromamba shell hook --shell bash)“
```

#### Basic Usage
The code below shows an example of basic `conda` use on the command line. The same general approach also applies for `mamba` and `pixi`.
```
# Create and activate environment
conda create \
    -n myenv \
    python=3.10

conda activate myenv

# Install binaries & libraries
conda install \
    -c conda-forge \
    -c bioconda \
     samtools numpy pandas

# Run script
Python script.py
samtools view alignment.bam

# Deactivate (close) environment
deactivate
```
#### Sharing environments
Conda environments are shared via a yaml file that outlines all conda-managed packages and dependencies.
```
# Create sharable environment file
conda env export -n myenv > environment.yml

# Install via environment file
conda create -f environment.yml 
```

Example of `environment.yml`:
```
name: myenv
channels:
  - bioconda
  - conda-forge
dependencies:
samtools=1.18=hd87286a_0
numpy=1.26.4=py311h64a7726_0
pandas=2.2.3=py311h7db5c69_1
```

## Practical
Click [here](../09b-comp-env-practical/) to navigate to the `Computer Environment` practical.
>>>>>>> main
