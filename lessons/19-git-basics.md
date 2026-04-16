---
layout: page
title: Git Basics with VS Code
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/19-git-basics/
---

This exercise walks you through the basic Git workflow using VS Code's **Source Control** tab and GitHub's web interface. By the end, you will have cloned a repository, created a branch, made changes, and merged them back.

---

## Prerequisites

- [VS Code](https://code.visualstudio.com/) installed
- [Git](https://git-scm.com/) installed
- A GitHub account with access to your institute's repository

---

## 1. Clone the Repository

1. Open VS Code.
2. Click the **Source Control** tab in the left sidebar (the icon that looks like a branching graph).
3. If no folder is open, you will see a **Clone Repository** button. Click it.
4. Paste your institute's repository URL (e.g., `https://github.com/your-org/your-repo.git`) into the input box that appears at the top of the window.
5. Choose a local folder to clone into and click **Select as Repository Destination**.
6. When prompted, click **Open** to open the cloned repository in VS Code.

<!-- TODO: Screenshot of Source Control tab showing "Clone Repository" button -->

<!-- TODO: Screenshot of repository URL input box at top of VS Code -->

---

## 2. Create a Branch

1. In the **Source Control** tab, click the **...** (more actions) menu at the top of the panel.
2. Navigate to **Branch** > **Create Branch...**.
3. Name your branch something descriptive, e.g., `update-readme-yourname`.
4. Press **Enter** — VS Code will create the branch and switch to it automatically.
5. You can confirm the active branch by looking at the bottom-left corner of the VS Code status bar.

<!-- TODO: Screenshot of Source Control "..." menu with Branch > Create Branch highlighted -->

<!-- TODO: Screenshot of branch name input box -->

<!-- TODO: Screenshot of status bar showing new branch name -->

---

## 3. Edit the README

1. Click the **Explorer** tab in the left sidebar to view your files.
2. Open the `README.md` file.
3. Add a line with your name and today's date, for example:

   ```markdown
   ## Contributors
   - Your Name (2026-04-16)
   ```

4. Save the file (`Ctrl+S` / `Cmd+S`).

<!-- TODO: Screenshot of edited README in VS Code editor -->

---

## 4. Stage and Commit

1. Click the **Source Control** tab in the left sidebar.
2. You should see `README.md` listed under the **Changes** section.
3. Hover over `README.md` and click the **+** (Stage Changes) icon to move it to the **Staged Changes** section.
4. Type a commit message in the **Message** text box at the top of the Source Control panel, e.g., `Add contributor name to README`.
5. Click the **Commit** button (checkmark icon) to commit your staged changes.

<!-- TODO: Screenshot of Source Control tab showing README.md under "Changes" with the + icon highlighted -->

<!-- TODO: Screenshot of Source Control tab with README.md under "Staged Changes" and a commit message entered -->

---

## 5. Push to GitHub

1. After committing, the **Commit** button in the Source Control tab will change to **Publish Branch** (since this is a new branch).
2. Click **Publish Branch** to push your branch to GitHub.
3. If prompted, authenticate with GitHub and select the remote to publish to.

<!-- TODO: Screenshot of "Publish Branch" button in Source Control tab -->

---

## 6. Create a Pull Request and Merge (GitHub Website)

1. Open your repository on [github.com](https://github.com).
2. You should see a banner saying your branch was recently pushed. Click **Compare & pull request**.
3. Review the changes, add a title and description if needed, then click **Create pull request**.
4. Once the pull request is created and any reviewers have approved, click **Merge pull request**.
5. Click **Confirm merge**.
6. Optionally, delete the branch on GitHub by clicking **Delete branch**.

<!-- TODO: Screenshot of "Compare & pull request" banner on GitHub -->

<!-- TODO: Screenshot of "Create pull request" page -->

<!-- TODO: Screenshot of "Merge pull request" button -->

---

## 7. Pull the Merged Changes Locally

1. In VS Code, click the **Source Control** tab.
2. Click the **...** menu and navigate to **Branch** > **Checkout to...**, then select `main`.
3. Click the **...** menu again and select **Pull** to pull the latest changes from GitHub.
4. Your local `main` branch now includes the merged changes.

<!-- TODO: Screenshot of "Checkout to..." menu showing main branch -->

<!-- TODO: Screenshot of Pull option in Source Control "..." menu -->

---

You have now completed a full Git workflow — clone, branch, edit, commit, push, and merge. This is the foundation for collaborating on code with your team.
