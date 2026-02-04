---
layout: page
title: Containers and Registries
nav_order: 6
---

{% capture section_overview_1 %}

This section walks through installing <code>venv</code> and <code>micromamba</code> for use in later sections.

{% endcapture %}

{% capture section_body_1 %}

## **Installing Micromamba**

The steps below will install <code>micromamba</code> into your <code>$HOME</code> directory. Skip to [Installing Venv](#installing-venv) if you plan to use an existing installation of <code>micromamba</code>, <code>mamba</code>, <code>conda</code>, or <code>miniconda</code>.

### 1.1 Install Micromamba

Check if <code>micromamba</code> is installed:

<pre><code class="language-bash">micromamba --version</code></pre>

Install <code>micromamba</code>, if needed (no <code>sudo</code> required):

<pre><code class="language-bash">"${SHELL}" &lt;(curl -L micro.mamba.pm/install.sh)</code></pre>

Reset your shell:

<pre><code class="language-bash">source ~/.bashrc</code></pre>

### 1.2 Add bioconda channel (optional)

<pre><code class="language-bash">micromamba config append channels bioconda</code></pre>

## **Installing Venv**

This process checks whether `venv` is available via your system-wide Python. If not, you will install Python (with `venv`) inside a `micromamba` environment (suitable for non-root users).

### 1.3 Check if venv is installed

<pre><code class="language-bash">python3 -m venv --help</code></pre>

### 1.4 Install Python with venv via micromamba (if needed)

<pre><code class="language-bash">micromamba create -n py311_env python=3.11</code></pre>

{% endcapture %}






{% capture section_overview_2 %}

This activity highlights differences in how <code>venv</code> and <code>micromamba</code> create *isolated* environments.

> Attempt each step below before exposing the answer.

{% endcapture%}

{% capture section_body_2 %}
## **Getting Started**

### 2.1 Record the path to your base python3 executable

<pre><code class="language-bash">realpath "$(command -v python3)"</code></pre>

<!-- TEXTBOX -->
{% include textbox.html %}

## **Venv Environments**

### 2.2 Create and activate a new venv

<pre><code class="language-bash">python3 -m venv venv_test_1
source venv_test_1/bin/activate</code></pre>

<div class="alert alert-success">
You can revert to a clean state with: <code>deactivate; rm -rf venv_test_1/</code>
</div>

### 2.3 Determine Python executable location

<pre><code class="language-bash">realpath "$(command -v python3)"</code></pre>

<!-- TEXTBOX -->
{% include textbox.html %}

**Question 2.5.1 Is this the same as the `python3` path in step 2.1?**

<!-- YES / NO BUTTON -->
{% include radio-lab.html id="2.5.1" %}

<!-- ANSWER -->
{% capture answer_content %}
Your venv uses the same Python executable as your base install.
{% endcapture %}

{% include answer.html id="2.5.1" content=answer_content %}

### 2.4 Deactivate environments

<pre><code class="language-bash">deactivate
micromamba deactivate</code></pre>

You should now be in your base environmnet

## **Conda / Mamba Environments**
> The following should be performed from your base environment, not the `py311_env` created in Part 1. You can return to your base environment using `micromamba deactivate`.

### 2.5 Create and activate a new micromamba environment

Create a new `micromamba` environment called `mamba_test_1`:

<pre><code class="language-bash">micromamba create -n mamba_test_1 python=3.11</code></pre>

Activate your new environment:

<pre><code class="language-bash">micromamba activate mamba_test_1</code></pre>

### 2.6 Determine the location of your Python executable again

<pre><code class="language-bash">realpath "$(command -v python3)"</code></pre>

<!-- TEXTBOX -->
{% include textbox.html %}

**Question 2.6.1 Is this the same as the `python3` path in step 2.1?**

<!-- YES / NO BUTTON -->
{% include radio-lab.html id="2.6.1" %}

<!-- ANSWER -->
{% capture answer_content %}
Your `mamba_test_1` environment should use a different Python executable than recorded in step 1. This is because Conda and Mamba install a new Python executable for each environment, making it independent from your base installation.
{% endcapture %}

{% include answer.html id="2.6.1" content=answer_content %} 

{% endcapture %}


{% capture section_overview_3 %}

This section shows how <code>pip</code> can silently alter already-installed packages.

{% endcapture %}

{% capture section_body_3 %}
## **Testing a new script (venv)**

### 3.1 Download the test script and data

<pre><code class="language-bash">curl https://github.com/DOH-JDJ0303/binfx-hub/raw/refs/heads/main/docs/presentations/2026/International_Influenza_Workshop/pt2_script.py -o pt2_script.py
curl https://github.com/DOH-JDJ0303/binfx-hub/raw/refs/heads/main/docs/presentations/2026/International_Influenza_Workshop/pt2_data_1.csv -o pt2_data_1.csv
curl https://github.com/DOH-JDJ0303/binfx-hub/raw/refs/heads/main/docs/presentations/2026/International_Influenza_Workshop/pt2_data_2.csv -o pt2_data_2.csv
</code></pre>

### 3.2 Create and activate venv_test_2

<!-- ANSWER -->
{% capture answer_content %}
<pre><code class="language-bash">python3 -m venv venv_test_2
source venv_test_2/bin/activate</code></pre>
{% endcapture %}

{% include answer.html id="3.2" content=answer_content %} 

### 3.3 Install pinned dependencies

<!-- ANSWER -->
{% capture answer_content %}
<pre><code class="language-bash">pip install "numpy&lt;2.0" "pandas==1.5.0"</code></pre>
{% endcapture %}

{% include answer.html id="3.3" content=answer_content %} 

### 3.4 Run script

<pre><code class="language-bash">python3 pt2_script.py</code></pre>

If successful, it should print a summary of three dataframes: `Dataframe 1`, `Dataframe 2`, and `Combined Dataframes`.

**Question 3.4.1 Did the script work?**

<!-- YES / NO BUTTON -->
{% include radio-lab.html id="3.4.1" %}

## **The disruption (venv)**

### 3.5 Install `scanpy` with `pip`

One of the other bioinformaticians in your lab is having trouble installing the Python module `scanpy`. They ask if you are able to install it on your machine.

<!-- ANSWER -->
{% capture answer_content %}
<pre><code class="language-bash">pip install scanpy"</code></pre>
{% endcapture %}

{% include answer.html id="3.5" content=answer_content %} 

### 3.6 Back to your test script

With that out of the way, you get back to running your test script:

<pre><code class="language-bash">python3 ./pt2_script.py"</code></pre>

**Question 3.6.1 Did the script work?**

<!-- YES / NO BUTTON -->
{% include radio-lab.html id="3.6.1" %}

**If not, why?**

{% include textbox.html %}

<!-- ANSWER -->
{% capture answer_content %}
Check your `pandas` version using:

<pre><code class="language-bash">pip list | grep pandas</code></pre>

Does this match the `v1.5.0` you installed in step 3?

`pip` can silently change the version of existing modules (in this case, `pandas`) when installing new packages (in this case, `scanpy`). This can break dependencies and render older scripts unusable (in this case, `pt2_script.py`)!
{% endcapture %}

{% include answer.html id="3.6.1" content=answer_content %}

## Testing a new script (`micromamba`)
> The following should be performed from your base environment, not the `py311_env` created in Part 1. You can return to your base environment using `micromamba deactivate`.

### 3.7 Create and activate a new `micromamba` environment

Use `micromamba` to create and activate a new environment called `mamba_test_2`.

<!-- ANSWER -->
{% capture answer_content %}
<pre><code class="language-bash">micromamba create -n mamba_test_2 python=3.10 -y
micromamba activate mamba_test_2</code></pre>
{% endcapture %}

{% include answer.html id="3.6.1" content=answer_content %}

### 3.8 Install the pinned dependencies with `micromamba`

Install the same dependencies as before (`pandas` v1.5.0 and `numpy` < v2.0), but with `micromamba`.

<!-- ANSWER -->
{% capture answer_content %}
<pre><code class="language-bash">micromamba install -y -c conda-forge "numpy<2.0" "pandas=1.5.0"</code></pre>
{% endcapture %}

{% include answer.html id="3.6.1" content=answer_content %}

### 3.9 Run the test script

<pre><code class="language-bash">python3 ./pt2_script.py</code></pre>

**Question 3.9.1 Did the script work?**

<!-- YES / NO BUTTON -->
{% include radio-lab.html id="3.9.1" %}

## The disruption (`micromamba`)

### 3.10 Install `scanpy` with `micromamba`

Your co-worker is back and they want you to try installing `scanpy` again, but this time using `micromamba`.

> Hint: Inspect the installation summary before confirming `[Y]` or denying `[n]` the installation.

<!-- ANSWER -->
{% capture answer_content %}
<pre><code class="language-bash">micromamba install -c conda-forge -c bioconda scanpy</code></pre>
{% endcapture %}

{% include answer.html id="3.10" content=answer_content %}


**Question 3.10.1 Did you confirm `[Y]` or deny `[n]` the installation? Why?**
<!-- TEXTBOX -->
{% include textbox.html %}

### 3.11. Run the test script

Try the test script one last time after making your decision about `scanpy`:

<pre><code class="language-bash">python3 ./pt2_script.py</code></pre>

**Question 3.11.1 Did the script work?**

<!-- YES / NO BUTTON -->
{% include radio-lab.html id="3.11.1" %}

**Question 3.11.2 Do you regret your decision from step 3.10?**

<!-- YES / NO BUTTON -->
{% include radio-lab.html id="3.11.2" %}

<!-- ANSWER -->
{% capture answer_content %}
`micromamba` warned us that installing `scanpy` would require updating to a new version of `pandas`. This allowed us to avoid silently breaking the `pandas v1.5.0` dependency of `pt2_script.py`.
{% endcapture %}

{% include answer.html id="3.10" content=answer_content %}

{% endcapture %}

{% include activity.html variant="1" title="Part 1: Installing Venv and Micromamba" overview=section_overview_1 content=section_body_1 %}
{% include activity.html variant="2" title="Part 2: Environment Isolation" overview=section_overview_2 content=section_body_2 %}
{% include activity.html variant="3" title="Part 3: Silent Changes" overview=section_overview_3 content=section_body_3 %}