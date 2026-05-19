---
layout: page
title: Bioinformatic Tool Installation
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/10b-tool-installation/
---

<p style="color: #015CAE; font-size: 19px;">Content developed by Jared Johnson</p>

## Module Objectives
- Install Nextstrain
- Install all other tools used in later modules into a single Micromamba environment

## Nextstrain
Install Nextstrain following the `Conda` runtime instructions on the <a href="https://docs.nextstrain.org/en/latest/install.html#installation-steps" target="_blank">docs page</a>.

## Other Software
### Install
Use the command below to create a new environment with micromamba and install the _other_ software that will be used in future lessions.

<pre><code class="language-bash">
micromamba create -n flu_env \
  -c bioconda \
  -c conda-forge \
  -c defaults \
  "sra-tools=3.4.1" \
  "samtools=1.1" \
  "nextflow=26.04.1" \
  --yes
</code></pre>

### Verify
<pre><code class="language-bash">
# activate the environment
micromamba activate flu_env

# check for installed tools
fasterq-dump -v
samtools
nextflow version -v

# deactivate the environment
micromamba deactivate
</code></pre>
