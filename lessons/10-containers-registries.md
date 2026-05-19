---
layout: page
title: Containers and Registries
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/10-containers-registries/
---
<p style="color: #015CAE; font-size: 19px;">Content developed by Ben Rambo-Martin</p>

## Slides

<iframe
  src="{{ site.baseurl }}/presentations/Presentation6_container_registries.html"
  width="100%"
  height="600px"
  frameborder="0"
  allowfullscreen>
</iframe>

<a href="{{ site.baseurl }}/presentations/Presentation6_container_registries.html" download>Click to Download Slides</a>

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

## Practical Exercises

These exercises walk you through installing Docker Desktop, configuring resources, running containers in different modes, and learning how volumes work.

All `docker` commands can be run from the terminal in VS Code.

---

### Exercise 1 — Install and Configure Docker Desktop
{: .mt-4}

<div class="exercise-block" markdown="1">

#### 1.1 Install Docker Desktop

1. Download Docker Desktop from [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Run the installer.
   - **Windows:** ensure **Use WSL 2 instead of Hyper-V** is checked.
   - **macOS:** choose the correct chip (Apple Silicon or Intel).
   - **Linux:** Docker Desktop is optional — you can install the Docker Engine directly instead (see [docs.docker.com/engine/install](https://docs.docker.com/engine/install/)).
3. After installation, Docker Desktop will start automatically. On Windows you may need to log out and back in.

#### 1.2 Verify the Backend

**Click your operating system below for platform-specific instructions:**

<details class="os-select" markdown="1">
<summary><strong>Windows</strong></summary>

Open Docker Desktop → **Settings** → **General** and confirm:

- ✅ **Use the WSL 2 based engine** is enabled

Then open **Settings** → **Resources** → **WSL integration** and confirm:

- ✅ Your Ubuntu distribution is toggled **on**

</details>

<details class="os-select" markdown="1">
<summary><strong>macOS</strong></summary>

Docker Desktop on macOS uses a built-in Linux VM automatically — no extra configuration is needed. Open Docker Desktop → **Settings** → **General** and confirm it is running.

</details>

<details class="os-select" markdown="1">
<summary><strong>Linux</strong></summary>

If using Docker Engine (no Desktop), verify the daemon is running:

```bash
sudo systemctl status docker
```

If using Docker Desktop for Linux, open it and confirm it is running.

</details>

Verify from your terminal (all platforms):

```bash
docker info 2>/dev/null | grep -i "storage driver\|operating system\|server version"
```

You should see output referencing your Linux distribution (or the Docker VM) and `overlay2` storage.

#### 1.3 Allocate Resources

**Click your operating system below for platform-specific instructions:**

<details class="os-select" markdown="1">
<summary><strong>Windows (WSL2)</strong></summary>

Docker Desktop on WSL2 shares memory and CPU with the WSL2 VM.

First, check how much RAM and how many CPUs your host machine has. Open **PowerShell** and run:

```powershell
# Total physical memory (GB)
[math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB)

# Total logical processors
(Get-CimInstance Win32_ComputerSystem).NumberOfLogicalProcessors
```

Use these numbers to calculate \~80% for each (e.g., 16 GB → 13 GB, 8 CPUs → 6).

Now edit (or create) the WSL config file **from PowerShell or cmd**:

```
notepad %USERPROFILE%\.wslconfig
```

Add the following (replace the values with your \~80% calculations):

```ini
[wsl2]
memory=13GB
processors=6
```

For example, on a machine with 16 GB RAM and 8 CPUs, the above allocates \~80% of each.

Save the file, then restart WSL from PowerShell:

```
wsl --shutdown
```

Reopen your WSL2 terminal and verify:

```bash
nproc        # available CPUs
free -g      # available memory in GB
```

</details>

<details class="os-select" markdown="1">
<summary><strong>macOS</strong></summary>

Open Docker Desktop → **Settings** → **Resources** → **Advanced**.

Set CPUs and Memory to \~80% of your system (e.g., 6 CPUs and 13 GB on a 8-core / 16 GB machine).

Click **Apply & Restart**.

Verify from your terminal:

```bash
docker info 2>/dev/null | grep -i "cpus\|memory"
```

</details>

<details class="os-select" markdown="1">
<summary><strong>Linux</strong></summary>

Docker Engine on Linux uses host resources directly — no VM layer, no resource limits by default. Your containers can access all available CPUs and memory.

Verify:

```bash
nproc        # available CPUs
free -g      # available memory in GB
```

</details>

</div>

---

### Exercise 2 — Running Containers: Detached, Ephemeral, and Interactive
{: .mt-4}

<div class="exercise-block" markdown="1">

In this exercise you will run the same Ubuntu container three different ways and observe the differences.

#### 2.1 Check Baseline Resource Usage

Before running anything, check that Docker is running and note your resource baseline:

```bash
docker info 2>/dev/null | grep -iE "cpus|memory"
```

#### 2.2 Run a Container in Detached (Background) Mode

Start an Ubuntu container that allocates a large block of memory in the background:

```bash
docker run -d --name mem-test --shm-size=512m ubuntu:24.04 \
  bash -c "dd if=/dev/zero of=/dev/shm/blob bs=1M count=500 && sleep 300"
```

<details class="collapsible-md" markdown="1">
<summary><strong>FYI: What is <code>dd</code> and <code>--shm-size</code>?</strong></summary>

`dd` (data duplicator) copies data block-by-block. Here it reads 500 one-megabyte blocks of zeros (`if=/dev/zero`) and writes them to `/dev/shm/blob` (`of=`), a RAM-backed filesystem inside the container — effectively allocating 500 MB of memory. The container then sleeps for 5 minutes so you can observe the usage.

`--shm-size=512m` increases the container's shared memory (`/dev/shm`) from Docker's default of 64 MB to 512 MB. **You will rarely need this flag in practice** — it is only required here because we are deliberately writing a large file to `/dev/shm` to simulate memory usage. Normal bioinformatics workflows do not use `/dev/shm` and do not need this flag.

</details>

Check that the container is running:

```bash
docker ps
```

Check host resource usage again with `docker stats`:

```bash
docker stats --no-stream
```

Compare the memory usage to your baseline.

#### 2.3 Stop and Remove the Detached Container

```bash
docker stop mem-test && docker rm mem-test
```

Verify the container is gone:

```bash
docker ps -a | grep mem-test
```

Check that no containers are running:

```bash
docker ps
```

The list should be empty — only the header row is printed.

#### 2.4 Run the Same Workload Ephemerally

The `--rm` flag tells Docker to automatically delete the container when it exits. This is the most common mode in bioinformatics — no leftover containers to clean up.

```bash
docker run --rm --name mem-test-ephemeral --shm-size=512m ubuntu:24.04 \
  bash -c "dd if=/dev/zero of=/dev/shm/blob bs=1M count=500 && echo 'Done — container will self-destruct'"
```

After the command finishes, verify the container no longer exists:

```bash
docker ps -a | grep mem-test-ephemeral
```

Nothing is returned — the container was automatically removed.

#### 2.5 Run the Same Container Interactively

The `-it` flags give you an interactive terminal inside the container:

```bash
docker run --rm -it --shm-size=512m ubuntu:24.04 bash
```

You are now **inside** the container. 

Your prompt will look like:

> `root@ac1d39fb4bc6:/#` 

"ac1d39fb4bc6" is a randomly generated `hostname` docker assigned the container. You will have a different string of characters.

Try some commands:

```bash
# Check the OS
echo "os INFORMATION:"
cat /etc/os-release | head -3
echo "------------------------"

# Run the same memory workload manually
echo "dd COMMAND OUTPUT:"
dd if=/dev/zero of=/dev/shm/blob bs=1M count=500 && echo "Done"
echo "------------------------"

# See what's in the filesystem
echo "ls COMMAND OUTPUT:"
ls /
echo "------------------------"

# Exit the container (it will be removed because of --rm)
exit


```

After exiting, verify the container is gone:

```bash
docker ps -a
```

Although the container is removed, the **image** (`ubuntu:24.04`) is still stored on your host. Docker caches images so they don't need to be downloaded again:

```bash
docker images
```

You should see `ubuntu` with tag `24.04` listed — it will be reused the next time you run a container from that image.

#### 2.6 The Docker Daemon Uses Resources Even When Idle

Even with **no containers running**, the Docker daemon (and on macOS/Windows, its Linux VM) consumes CPU and memory on your host.

Check processes on your host **with Docker Desktop running** and no containers:

<details class="os-select" markdown="1">
<summary><strong>Windows (WSL2)</strong></summary>

From **PowerShell** (not WSL):

```powershell
# Check the WSL2 VM memory usage
Get-Process vmmem -ErrorAction SilentlyContinue | Select-Object Name, @{N='Memory (MB)';E={[math]::Round($_.WorkingSet64/1MB)}}

# Check Docker Desktop processes
Get-Process *docker* | Select-Object Name, @{N='Memory (MB)';E={[math]::Round($_.WorkingSet64/1MB)}}
```

The `vmmem` process is the WSL2 VM — it often holds **several GB** of memory even when idle.

</details>

<details class="os-select" markdown="1">
<summary><strong>macOS</strong></summary>

```bash
# Check Docker VM memory usage (in MB)
ps aux | grep -i "com.docker" | grep -v grep | awk '{sum += $6} END {printf "Docker total: %d MB\n", sum/1024}'
```

</details>

<details class="os-select" markdown="1">
<summary><strong>Linux</strong></summary>

```bash
# Check dockerd and containerd memory usage
ps -eo pid,rss,comm | grep -E "dockerd|containerd" | awk '{printf "%s\t%d MB\t%s\n", $1, $2/1024, $3}'
```

</details>

**Recommendation:** When you are not using containers, quit Docker Desktop (macOS/Windows) or stop the Docker service (Linux) to free those resources:

- **macOS:** Right-click the Docker icon in the menu bar → **Quit Docker Desktop**
- **Windows:** Right-click the Docker icon in the system tray → **Quit Docker Desktop**. Then also shut down WSL2 from PowerShell — the `vmmem` process will continue holding memory even after Docker Desktop is closed:
  ```
  wsl --shutdown
  ```
- **Linux:** 
  ```bash 
  sudo systemctl stop docker
  ```

Restart it when you need containers again.

</div>

---

### Exercise 3 — Understanding Volumes
{: .mt-4}

<div class="exercise-block" markdown="1">

Containers are **ephemeral** by default — any files created inside a container disappear when it is removed. **Volumes** (bind mounts) let you connect a host directory to a path inside the container so data persists.

#### 3.1 Without a Volume — Data Does NOT Persist

Run a container that creates a file, then exits:

```bash
docker run --rm ubuntu:24.04 \
  bash -c "echo 'hello from inside the container' > /tmp/output.txt && cat /tmp/output.txt"
```

You will see `hello from inside the container` printed. But the file is gone — it only existed inside the container:

```bash
ls /tmp/output.txt 2>/dev/null || echo "File does not exist on host"
```

#### 3.2 With a Volume — Data Persists on the Host

Create a working directory and mount it into the container with `-v`:

```bash
mkdir -p ~/container-test

docker run --rm -v ~/container-test:/data ubuntu:24.04 \
  bash -c "echo 'hello from inside the container' > /data/output.txt && cat /data/output.txt"
```

Now check the host — the file persists:

```bash
cat ~/container-test/output.txt
```

You should see `hello from inside the container`.

#### 3.3 Writing Output to a Mounted Volume

A more realistic example — generate data inside the container and save it to the host:

```bash
docker run --rm -v ~/container-test:/data ubuntu:24.04 \
  bash -c "date > /data/timestamp.txt && hostname >> /data/timestamp.txt && echo 'Wrote timestamp and hostname'"
```

Inspect the output on the host:

```bash
cat ~/container-test/timestamp.txt
```

Notice the hostname is the **container ID**, not your host — confirming the command ran inside the container, but the output file is on your host.

#### 3.4 Interactive Exploration of Volumes

Enter a container interactively with the volume mounted:

```bash
docker run --rm -it -v ~/container-test:/data ubuntu:24.04 bash
```

Inside the container:

```bash
# See the mounted directory
echo "\`ls /data\` COMMAND OUTPUT:"
ls /data
echo "---------------"

# The files you created earlier are here
echo "\`cat /data/output.txt\` COMMAND OUTPUT:"
cat /data/output.txt
echo "---------------"

# Create another file
echo "\`echo "created interactively" > /data/interactive.txt\` COMMAND RUN"
echo "created interactively" > /data/interactive.txt
echo "---------------"

# Exit
exit


```

Verify on the host:

```bash
cat ~/container-test/interactive.txt
```

#### 3.5 Clean Up

```bash
rm -r ~/container-test
```

</div>

---

### Summary

| Mode | Flags | Container after exit | Use case |
|------|-------|---------------------|----------|
| Detached | `-d` | Remains (must `docker rm`) | Long-running services |
| Ephemeral | `--rm` | Automatically removed | Pipeline steps, one-off tasks |
| Interactive | `--rm -it` | Automatically removed | Debugging, exploring tools |

| Volume | Flag | Data after exit |
|--------|------|-----------------|
| No mount | *(none)* | Lost |
| Bind mount | `-v /host/path:/container/path` | Persists on host |
