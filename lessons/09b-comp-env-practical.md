---
layout: page
title: "Computer Environments – Practical"
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/09b-comp-env-practical/
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

## Computer Environments Practical Exercises

These exercises accompany the **Computer Environments** module. They walk you through installing `venv` and `micromamba`, exploring environment isolation, and observing how package managers can silently alter dependencies.

---

### Exercise 1 — Installing Micromamba and Venv
{: .mt-4}

<div class="exercise-block" markdown="1">

This section walks through installing `venv` and `micromamba` for use in later sections.

#### Installing Micromamba

The steps below will install `micromamba` into your `$HOME` directory. Skip to [Installing Venv](#installing-venv) if you plan to use an existing installation of `micromamba`, `mamba`, `conda`, or `miniconda`.

**1.1 Install Micromamba**

Check if `micromamba` is installed:

```bash
micromamba --version
```

Install `micromamba`, if needed (no `sudo` required):

```bash
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
```

Reset your shell:

```bash
source ~/.bashrc
```

**1.2 Add bioconda channel (optional)**

```bash
micromamba config append channels bioconda
```

#### Installing Venv

This process checks whether `venv` is available via your system-wide Python. If not, you will install Python (with `venv`) inside a `micromamba` environment (suitable for non-root users).

**1.3 Check if venv is installed**

```bash
python3 -m venv --help
```

**1.4 Install Python with venv via micromamba (if needed)**

```bash
micromamba create -n py311_env python=3.11
```

</div>

---

### Exercise 2 — Environment Isolation
{: .mt-4}

This exercise highlights differences in how `venv` and `micromamba` create *isolated* environments.

> Attempt each step below before exposing the answer.

<div class="exercise-block" markdown="1">

#### Getting Started

**2.1 Record the path to your base python3 executable**

```bash
realpath "$(command -v python3)"
```

{% include textbox.html %}

#### Venv Environments

**2.2 Create and activate a new venv**

```bash
python3 -m venv venv_test_1
source venv_test_1/bin/activate
```

{% include tip.html content="You can revert to a clean state with: <code>deactivate; rm -rf venv_test_1/</code>" %}

**2.3 Determine Python executable location**

```bash
realpath "$(command -v python3)"
```

{% include textbox.html %}

**Question 2.5.1 Is this the same as the `python3` path in step 2.1?**

{% include radio-lab.html id="2.5.1" %}

{% capture answer_content %}
Your venv uses the same Python executable as your base install.
{% endcapture %}

{% include answer.html id="2.5.1" content=answer_content %}

**2.4 Deactivate environments**

```bash
deactivate
micromamba deactivate
```

You should now be in your base environment.

#### Conda / Mamba Environments

> The following should be performed from your base environment, not the `py311_env` created in Exercise 1. You can return to your base environment using `micromamba deactivate`.

**2.5 Create and activate a new micromamba environment**

Create a new `micromamba` environment called `mamba_test_1`:

```bash
micromamba create -n mamba_test_1 python=3.11
```

Activate your new environment:

```bash
micromamba activate mamba_test_1
```

**2.6 Determine the location of your Python executable again**

```bash
realpath "$(command -v python3)"
```

{% include textbox.html %}

**Question 2.6.1 Is this the same as the `python3` path in step 2.1?**

{% include radio-lab.html id="2.6.1" %}

{% capture answer_content %}
Your `mamba_test_1` environment should use a different Python executable than recorded in step 1. This is because Conda and Mamba install a new Python executable for each environment, making it independent from your base installation.
{% endcapture %}

{% include answer.html id="2.6.1" content=answer_content %}

</div>

---

### Exercise 3 — Silent Changes
{: .mt-4}

This exercise shows how `pip` can silently alter already-installed packages.

<div class="exercise-block" markdown="1">

#### Testing a new script (venv)

**3.1 Download the test script and data**

```bash
curl https://github.com/DOH-JDJ0303/binfx-hub/raw/refs/heads/main/docs/presentations/2026/International_Influenza_Workshop/pt2_script.py -o pt2_script.py
curl https://github.com/DOH-JDJ0303/binfx-hub/raw/refs/heads/main/docs/presentations/2026/International_Influenza_Workshop/pt2_data_1.csv -o pt2_data_1.csv
curl https://github.com/DOH-JDJ0303/binfx-hub/raw/refs/heads/main/docs/presentations/2026/International_Influenza_Workshop/pt2_data_2.csv -o pt2_data_2.csv
```

**3.2 Create and activate venv_test_2**

{% capture answer_content %}
```bash
python3 -m venv venv_test_2
source venv_test_2/bin/activate
```
{% endcapture %}

{% include answer.html id="3.2" content=answer_content %}

**3.3 Install pinned dependencies**

{% capture answer_content %}
```bash
pip install "numpy<2.0" "pandas==1.5.0"
```
{% endcapture %}

{% include answer.html id="3.3" content=answer_content %}

**3.4 Run script**

```bash
python3 pt2_script.py
```

If successful, it should print a summary of three dataframes: `Dataframe 1`, `Dataframe 2`, and `Combined Dataframes`.

**Question 3.4.1 Did the script work?**

{% include radio-lab.html id="3.4.1" %}

#### The disruption (venv)

**3.5 Install `scanpy` with `pip`**

One of the other bioinformaticians in your lab is having trouble installing the Python module `scanpy`. They ask if you are able to install it on your machine.

{% capture answer_content %}
```bash
pip install scanpy
```
{% endcapture %}

{% include answer.html id="3.5" content=answer_content %}

**3.6 Back to your test script**

With that out of the way, you get back to running your test script:

```bash
python3 ./pt2_script.py
```

**Question 3.6.1 Did the script work?**

{% include radio-lab.html id="3.6.1" %}

**If not, why?**

{% include textbox.html %}

{% capture answer_content %}
Check your `pandas` version using:

```bash
pip list | grep pandas
```

Does this match the `v1.5.0` you installed in step 3?

`pip` can silently change the version of existing modules (in this case, `pandas`) when installing new packages (in this case, `scanpy`). This can break dependencies and render older scripts unusable (in this case, `pt2_script.py`)!
{% endcapture %}

{% include answer.html id="3.6.1" content=answer_content %}

</div>

<div class="exercise-block" markdown="1">

#### Testing a new script (micromamba)

> The following should be performed from your base environment, not the `py311_env` created in Exercise 1. You can return to your base environment using `micromamba deactivate`.

**3.7 Create and activate a new `micromamba` environment**

Use `micromamba` to create and activate a new environment called `mamba_test_2`.

{% capture answer_content %}
```bash
micromamba create -n mamba_test_2 python=3.10 -y
micromamba activate mamba_test_2
```
{% endcapture %}

{% include answer.html id="3.7" content=answer_content %}

**3.8 Install the pinned dependencies with `micromamba`**

Install the same dependencies as before (`pandas` v1.5.0 and `numpy` < v2.0), but with `micromamba`.

{% capture answer_content %}
```bash
micromamba install -y -c conda-forge "numpy<2.0" "pandas=1.5.0"
```
{% endcapture %}

{% include answer.html id="3.8" content=answer_content %}

**3.9 Run the test script**

```bash
python3 ./pt2_script.py
```

**Question 3.9.1 Did the script work?**

{% include radio-lab.html id="3.9.1" %}

#### The disruption (micromamba)

**3.10 Install `scanpy` with `micromamba`**

Your co-worker is back and they want you to try installing `scanpy` again, but this time using `micromamba`.

> Hint: Inspect the installation summary before confirming `[Y]` or denying `[n]` the installation.

{% capture answer_content %}
```bash
micromamba install -c conda-forge -c bioconda scanpy
```
{% endcapture %}

{% include answer.html id="3.10" content=answer_content %}

**Question 3.10.1 Did you confirm `[Y]` or deny `[n]` the installation? Why?**

{% include textbox.html %}

**3.11 Run the test script**

Try the test script one last time after making your decision about `scanpy`:

```bash
python3 ./pt2_script.py
```

**Question 3.11.1 Did the script work?**

{% include radio-lab.html id="3.11.1" %}

**Question 3.11.2 Do you regret your decision from step 3.10?**

{% include radio-lab.html id="3.11.2" %}

{% capture answer_content %}
`micromamba` warned us that installing `scanpy` would require updating to a new version of `pandas`. This allowed us to avoid silently breaking the `pandas v1.5.0` dependency of `pt2_script.py`.
{% endcapture %}

{% include answer.html id="3.11" content=answer_content %}

</div>