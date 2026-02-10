---
layout: page
title: Computer Setup (WSL)
nav_order: 4
---

{% capture section_overview_1 %}

Before installing WSL, confirm your Windows version meets the minimum requirements.

{% endcapture %}

{% capture section_body_1 %}

## **Prerequisites**

### 1.1 Check your Windows version

Select <kbd>⊞ Win</kbd> + <kbd>R</kbd>, type `winver`, and click **OK**.

<div class="alert alert-warning">
<strong>Requirement:</strong> Windows 10 version 2004+ (Build 19041+) or Windows 11.<br>
Update via <strong>Start → Settings → Windows Update → Check for updates</strong> if needed.
</div>

### 1.2 What is WSL?

WSL (Windows Subsystem for Linux) lets you run a full Linux environment directly on Windows without a virtual machine or dual-boot setup. **WSL2** is the recommended version — it uses a real Linux kernel and offers full system-call compatibility.

Key benefits:
- Run Linux command-line tools (bash, grep, sed, awk, etc.)
- Install and run bioinformatics software natively
- Access the Windows filesystem from Linux and vice-versa

{% endcapture %}



{% capture section_overview_2 %}

Install WSL2 and the Ubuntu 20.04 distribution via PowerShell.

{% endcapture %}

{% capture section_body_2 %}

## **Install WSL2 and Ubuntu**

### 2.1 Open PowerShell as Administrator

Right-click the **Start** button and select **Windows PowerShell (Admin)** or **Terminal (Admin)**.

![Open PowerShell as Administrator](https://cdcgov.github.io/MIRA/articles/images/powershell_open.png)

### 2.2 Install WSL

Run the following command in PowerShell:

<pre><code class="language-powershell">wsl --install</code></pre>

<div class="alert alert-info">
<strong>Tip:</strong> To paste into a terminal, use <strong>right-click</strong> instead of <kbd>Ctrl</kbd>+<kbd>V</kbd>.
</div>

<div class="alert alert-warning">
If this command errors out, you may need to enable
<a href="https://cdcgov.github.io/MIRA/articles/troubleshooting.html#virtualization-error">virtualization</a>.
</div>

### 2.3 Restart your computer

Restart now before continuing to the next step.

### 2.4 Install Ubuntu 20.04

Reopen PowerShell **as Administrator** and run:

<pre><code class="language-powershell">wsl --set-default-version 2
wsl --install -d Ubuntu-20.04</code></pre>

<div class="alert alert-warning">
If either command errors out, see the
<a href="https://cdcgov.github.io/MIRA/articles/troubleshooting.html#wsl-install-error">WSL troubleshooting guide</a>.
</div>

An Ubuntu terminal should open automatically:

![Ubuntu setup prompt](https://cdcgov.github.io/MIRA/articles/images/ubuntu_setub_1.png)

{% endcapture %}



{% capture section_overview_3 %}

Create your Linux user account inside the new Ubuntu installation.

{% endcapture %}

{% capture section_body_3 %}

## **User Account Setup**

### 3.1 Create your WSL user account

When the Ubuntu terminal opens for the first time:

1. Enter a **username** (exclusive to WSL) and press <kbd>Enter</kbd>.
2. Enter a **password** and press <kbd>Enter</kbd>.

<div class="alert alert-danger">
<strong>Important:</strong> Choose a memorable password. If you forget it, you will need to reinstall Ubuntu.
</div>

A prompt will appear similar to:

![WSL command prompt](https://cdcgov.github.io/MIRA/articles/images/commandprompt_wsl.png)

where `nbx0` is replaced by your username and `L349232` by your computer name.

### 3.2 Restart your computer

Restart one more time to finalize the setup.

{% endcapture %}



{% capture section_overview_4 %}

Verify WSL is working and learn how to access it day-to-day.

{% endcapture %}

{% capture section_body_4 %}

## **Post-Install Verification**

### 4.1 Open Ubuntu

Search for **Ubuntu** in the Windows taskbar and click the app icon:

![Open Ubuntu from taskbar](https://cdcgov.github.io/MIRA/articles/images/ubuntu_open.png)

### 4.2 Verify your installation

Run the following commands to confirm everything is working:

<pre><code class="language-bash"># Check Ubuntu version
lsb_release -a

# Check your username
whoami

# Check WSL version from PowerShell (open a separate PowerShell window)
# wsl --list --verbose</code></pre>

### 4.3 Verify Linux mount in File Explorer

Windows 11 (and updated Windows 10) should automatically mount Linux in File Explorer.

![Linux in File Explorer](https://cdcgov.github.io/MIRA/articles/images/linux_file_explorer.png)

<div class="alert alert-info">
If you <strong>do not</strong> see "Linux" in File Explorer, you need to
<a href="https://cdcgov.github.io/MIRA/articles/troubleshooting.html#map-network-drive">map the WSL network drive</a>.
</div>

### 4.4 Understanding your file system

Inside WSL you have two main locations:

| Path | Description |
|------|-------------|
| `/home/<username>/` | Your Linux home directory (fast, native Linux filesystem) |
| `/mnt/c/` | Your Windows C: drive mounted inside Linux |

<div class="alert alert-info">
<strong>Best practice:</strong> Store project files in your Linux home directory (<code>~/</code>) for best performance. Access Windows files via <code>/mnt/c/</code> when needed.
</div>

### 4.5 Useful references

- [Microsoft WSL Install Guide](https://docs.microsoft.com/en-us/windows/wsl/install)
- [WSL Troubleshooting](https://cdcgov.github.io/MIRA/articles/troubleshooting.html)
- [WSL FAQ](https://learn.microsoft.com/en-us/windows/wsl/faq)

{% endcapture %}

{% include activity.html variant="1" title="Part 1: Prerequisites" overview=section_overview_1 content=section_body_1 %}
{% include activity.html variant="2" title="Part 2: Install WSL2 and Ubuntu" overview=section_overview_2 content=section_body_2 %}
{% include activity.html variant="3" title="Part 3: User Account Setup" overview=section_overview_3 content=section_body_3 %}
{% include activity.html variant="1" title="Part 4: Post-Install Verification" overview=section_overview_4 content=section_body_4 %}
