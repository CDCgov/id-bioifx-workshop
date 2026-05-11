---
layout: page
title: Git Basics with VS Code
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/19-git-basics/
---

This exercise walks you through the basic Git workflow using VS Code's **Source Control** tab and GitHub's web interface. By the end, you will have cloned a repository, created a branch, made changes, and merged them back.

---
<p style="color: #015CAE; font-size: 19px;">Content developed by Ben Rambo-Martin</p>
## Prerequisites

- [VS Code](https://code.visualstudio.com/) installed
- [Git](https://git-scm.com/) installed
- A GitHub account with access to your institute's repository

---

## 1. Clone the Repository

1. Open VS Code.
2. Click the **Source Control** tab in the left sidebar (the icon that looks like a branching graph).
   ![VS Code Source Control tab on the left sidebar displaying the Clone Repository button, with the interface ready for repository cloning](../../assets/images/vscode-git-source-control.png)
3. If no folder is open, you will see a **Clone Repository** button. Click it.
   ![VS Code Source Control tab showing the Clone Repository button](../../assets/images/vscode-git-source-control-clone.png)
4. Paste your institute's repository URL (e.g., `https://github.com/cdcent/your-repo.git`) into the input box that appears at the top of the window.
   ![](../../assets/images/vscode-git-source-control-clone-repo.png)
5. Choose a local folder to clone into and click **Select as Repository Destination**. Below, I have created a folder on my Desktop called github-repos to store all my cloned repositories.
   ![](../../assets/images/vscode-git-source-control-clone-repo-location.png)
6. When prompted, click **Open** to open the cloned repository in VS Code. It will ask you if you trust the publisher of the repository — click **Yes, I trust the authors**.
   ![](../../assets/images/vscode-git-source-control-clone-repo-landing.png)
---

## 2. Create a Branch

1. In the **Source Control** tab, click the "branch" icon beside "main" at the top of the **REPOSITORIES** panel.
   ![](../../assets/images/vscode-git-source-control-branch.png)
2. Your cursor will move to the input box at the top of the window. Type in a name for your new branch, hit `Enter`.
   ![](../../assets/images/vscode-git-source-control-branch-create.png)
3.  VS Code will create the branch and switch to it automatically. "Publish" the branch to GitHub by clicking the **Publish Branch** button that appears in the status bar at the bottom of the window.
   ![](../../assets/images/vscode-git-source-control-branch-publish.png)

------

## 3. Edit the README

1. Click the **Explorer** tab in the left sidebar to view your files.
2. Click the `README.md` file to open it.
3. Make a change in the file, for example:
   ![](../../assets/images/vscode-git-source-control-branch-edit-readme1.png)
   

   | Line 16: "Scientist Maintainers" to "Chilean Scientists"
   | Line 23: "CDC Collaborators" to "CDC Scientists"

   ![](../../assets/images/vscode-git-source-control-branch-edit-readme2.png)

4. Save the file (`Ctrl+S` / `Cmd+S`).

---

## 4. Stage, Commit, and Push Changes

1. Click the **Source Control** tab in the left sidebar.
2. You should see `README.md` listed under the **Changes** section. Clicking on this file will display a "diff" view showing your changes. Red highlights indicate removed text, and green highlights indicate added text.
3. Hover over `README.md` and click the **+** (Stage Changes) icon to move it to the **Staged Changes** section.
4. Type a commit message in the **Message** text box at the top of the Source Control panel, e.g., `updated heading of local and cdc contributors`.
5. Click the **Commit** button (checkmark icon) to commit your staged changes.
   ![](../../assets/images/vscode-git-source-control-branch-commit.png)
6. The blue button will now say **Sync Changes**. Click it to push your commit to GitHub. You may be prompted to sign in to GitHub if you haven't already.
   ![](../../assets/images/vscode-git-source-control-branch-commit-push.png)

---

## 5. Create a Pull Request and Merge (GitHub Website, not VS Code)

1. Open your web browser and navigate to your repository on [github.com](https://github.com).
2. Click on the **Branches** tab, then find your branch in the list and click the three dots next to it and click **New pull request**.
   ![](../../assets/images/github-branches-link.png)
   ![](../../assets/images/github-branches-link-pull-request.png)
3. Review the changes, add a title and description if needed, then click **Create pull request**.
   ![](../../assets/images/github-branches-link-pull-request-create.png)
4. For these workshop repos, CDC administrators will complete the merge.

---

## 7. Pull the Merged Changes Locally

1. Back in VS Code, click the **Source Control** tab. Click the "branch" icon at the top of the **REPOSITORIES** panel to switch branches. Select `main` to switch back to the main branch.
   ![](../../assets/images/vscode-git-source-control-branch-main.png)
2. Click **Sync Changes** to pull the latest changes from GitHub, which will include the merged changes from your branch. 
   ![](../../assets/images/vscode-git-source-control-branch-main-sync.png)
> Tip: Click the "sync" icon regularly to keep your local repository up to date with GitHub, especially if others are also making changes.

---

You have now completed a full Git workflow — clone, branch, edit, commit, push, and merge. This is the foundation for collaborating on code with your team.
