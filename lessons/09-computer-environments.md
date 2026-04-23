---
layout: page
title: Computer Environments
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/09-computer-environments/
---

{: title}

---
<p style="color: #015CAE; font-size: 19px;">Content developed by Jared Johnson</p>
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