---
title: Developer Guide
permalink: /developer-guide/
layout: default
---
<!-- filepath: /Users/nbx0/repos/id-bioifx-workshop/DEVELOPER_GUIDE.md -->
# Developer Guide

<details class="collapsible-md">
  <summary>1. Local Environment Setup</summary>
  <div class="collapsible-inner" markdown="1">

### MacOS Setup:
1.1. Xcode Command Line Tools:
   ```bash
   xcode-select --install
   ```

1.2. Ruby 3.x via [Homebrew](https://brew.sh):
   ```bash
   brew install ruby
   echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
   ```
1.3. Bundler:
   ```bash
   gem install bundler
   ```
1.4. Verify:
```bash
ruby -v
bundler -v
gem -v
```

---
<br>
### Windows (WSL2) Setup
Use WSL2 with Ubuntu (recommended for parity with deployment Linux environment).

1.1. Enable WSL + Virtual Machine Platform (PowerShell as Admin):
   ```powershell
   wsl --install
   ```
   (Reboot if prompted. Launch "Ubuntu" once to finalize.)

1.2. Update packages inside Ubuntu terminal:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
1.3. Install build/toolchain + Ruby (Ubuntu repos often fine for Jekyll dev):
   ```bash
   sudo apt install -y build-essential ruby-full git curl
   ```
   (If you need a newer Ruby than the distro ships, install rbenv:)
   ```bash
   sudo apt install -y libssl-dev zlib1g-dev libreadline-dev libffi-dev
   git clone https://github.com/rbenv/rbenv.git ~/.rbenv
   echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
   echo 'eval "$(rbenv init - bash)"' >> ~/.bashrc
   git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
   exec $SHELL
   rbenv install 3.3.0
   rbenv global 3.3.0
   ```
1.4. (Optional) Isolate gems in user space:
   ```bash
   echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
   echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```
1.5. Install Bundler:
   ```bash
   gem install bundler
   ```
1.6. Verify:
   ```bash
   ruby -v
   which ruby
   gem -v
   bundler -v
   ```
1.7. Clone repo inside the Linux filesystem (NOT /mnt/c/) for speed:
   ```bash
   cd ~
   git clone https://github.com/YOUR-USER/id-bioifx-workshop.git
   cd id-bioifx-workshop
   ```
1.8. Install gems & serve:
   ```bash
   bundle install
   bundle exec jekyll serve --livereload
   ```
1.9. Access site from Windows browser at:
   http://localhost:4000/id-bioifx-workshop/

---
<br>
### Clean + rebuild when stale:
```bash
bundle exec jekyll clean && bundle exec jekyll build
```
  </div>
</details>



<details class="collapsible-md">
  <summary>2. Adding a New Lesson</summary>
  <div class="collapsible-inner" markdown="1">

### 2.1 Filename
Use an existing numeric prefix style:
```
lessons/21-new-topic.md
```

### 2.2 Minimum Front Matter
```yaml
---
title: New Topic
description: Short single-sentence summary (optional for SEO)
nav_order: 21
layout: lesson
# published: false   # (uncomment to hide without deleting)
# tags: [optional, future]
---
```

### 2.3 Body Content Template
Recommended scaffold:
```markdown
# {{ page.title }}

## Overview
Introductory context.

**Learning Objectives**
- Objective 1
- Objective 2

## Practical

```bash
# example command
some_tool --flag value
```

### 2.4 No Manual Nav Edits Required
Prev/next links and header dropdown are derived automatically from `nav_order` values across `site.pages`.

  </div>
</details>

<details class="collapsible-md">
  <summary>3. Adding a Workshop</summary>
  <div class="collapsible-inner" markdown="1">

Create a markdown file in `_workshops/`:
```yaml
---
title: "2026 | Example City, Country"
workshop_order: 3
location: Example City, Country
event_date: 2026-05-14
layout: workshop
---
Body content...
```
The navigation and listing page `workshops.md` enumerate `site.workshops` sorted by `workshop_order`—no other file edit needed.
  </div>
</details>

<details class="collapsible-md">
  <summary>4. Dropdowns and Q&A Elements</summary>
  <div class="collapsible-inner" markdown="1">

### 4.1 Dropdown (Collapsible) Content (Markdown-preserving)
Use the `details.collapsible-md` pattern to safely include tables / markdown.
```html
<details class="collapsible-md">
  <summary>Section Title</summary>
  <div class="collapsible-inner" markdown="1">

Markdown **content**, including tables:

| Col A | Col B |
|-------|-------|
|  1    |  2    |

  </div>
</details>
```
Notes:
- `markdown="1"` tells Kramdown to parse inner markdown.
- CSS ensures aesthetic + accessible spacing.

### 4.2 Q&A Element (Centralized Bank)
Add or edit a question in `_data/qa.yml`:
```yaml
example-identifier:
  question: "What does FASTQ store in addition to nucleotide sequence?"
  answers: 
    - "Per-base quality scores (and identifier headers)."
    - "quality scores"
  hint: "Think about sequencing confidence."
  success: "Correct! ✅"
  failure: "Not quite. Try again."
  show_hint_after: 2

```
Embed in the markdown page:

{% raw %}
```bash
{% include qa.html id="example-identifier" %}
```
{% endraw %}
Which renders on the site as:
{% include qa.html id="example-identifier" %}

The include renders interactive reveal / hint controls with accessible labeling.
  </div>
</details>

<details class="collapsible-md">
  <summary>5. Github Pages Deployment</summary>
  <div class="collapsible-inner" markdown="1">

A GitHub Actions workflow (`.github/workflows/tagged-release-pages.yml`) builds and publishes on tags matching `v*`. Steps:
1. Bump / commit changes.
2. Create and push tag:
   ```bash
   git tag v0.1.3
   git push origin v0.1.3
   ```
3. Action installs Ruby 3.3, runs `bundle exec jekyll build`, uploads artifact.
  </div>
</details>

<details class="collapsible-md">
  <summary>6. Accessibility & Color</summary>
  <div class="collapsible-inner" markdown="1">

CDC Brand color hexes are defined in `_data/colors.yml` (referenced manually in `assets/css/style.css`). Copy buttons and collapsibles use ARIA labels and high-contrast backgrounds. Continue to test with keyboard + aXe.
  </div>
</details>

<details class="collapsible-md">
  <summary>7. Full Repository Tree (Annotated)</summary>
  <div class="collapsible-inner" markdown="1">

```
.
├── _config.yml              # Jekyll site configuration (collections, plugins, metadata)
├── Gemfile / Gemfile.lock   # Ruby gem dependencies (github-pages pins Jekyll)
├── README.md                # High-level project overview & basic setup
├── DEVELOPER_GUIDE.md       # (This guide) contributor/developer instructions
├── LICENSE                  # Project license
├── CONTRIBUTING.md          # Contribution policies
├── CODE_OF_CONDUCT.md       # Community standards (if present / name may vary)
├── DISCLAIMER.md            # Legal disclaimer
├── open_practices.md        # Additional policy document
├── rules_of_behavior.md     # Behavior / security rules
├── index.md                 # Landing page
├── search.md                # Search interface page (client-side search js)
├── workshops.md             # Workshops index listing collection items
├── lessons/                 # All lesson markdown files
│   ├── 01-objectives.md     # nav_order: 1 (example active lesson)
│   ├── ...                  # sequential lesson files (some unpublished 02–05)
│   └── 20-databases.md      # last current lesson
├── _workshops/              # Workshops collection sources
│   ├── 2026-bangkok-thailand.md
│   └── 2026-santiago-chile.md
├── _layouts/                # Page layouts (wrap content)
│   ├── default.html         # Base layout, header/footer + optional prev/next
│   ├── lesson.html          # Lesson-specific additions (inherits structure)
│   └── workshop.html        # Workshop layout (meta fields)
├── _includes/               # Reusable partials
│   ├── head.html            # <head> metadata, SEO, styles
│   ├── nav.html             # Primary navigation (dynamic lessons/workshops)
│   ├── footer.html          # Footer links (dynamic as needed)
│   ├── qa.html              # Q&A include rendering centralized questions
│   ├── copy-button.html     # (Legacy) not needed with JS auto buttons
│   └── collapsible.html     # (Legacy) superseded by native <details>
├── _data/                   # Structured YAML data
│   ├── qa.yml               # Q&A question bank
│   ├── colors.yml           # Approved color palette tokens
│   └── navigation.yml       # (Legacy) not in active use
├── assets/
│   ├── css/
│   │   ├── style.css        # Custom global styles & component design
│   │   └── syntax.css       # Rouge syntax highlight overrides
│   └── js/
│       ├── copy-code.js     # Injects copy buttons into <pre><code>
│       ├── collapsible.js   # (Optional) behavior for legacy collapsible include
│       ├── navigation.js    # Enhancements / accessible nav (future)
│       └── search.js        # Client-side search (tokenize, score, highlight)
├── scripts/
│   └── md2docx.sh           # Pandoc helper for markdown → docx export
├── .github/workflows/
│   └── tagged-release-pages.yml  # Tag-triggered build & deploy pipeline
└── _site/                   # Generated output (ignored in commits ideally)
```
  </div>
</details>

<details class="collapsible-md">
  <summary>8. Common Tasks Cheat Sheet</summary>
  <div class="collapsible-inner" markdown="1">


| Task | Command |
|------|---------|
| Install deps | `bundle install` |
| Serve locally | `bundle exec jekyll serve --livereload` |
| Clean & rebuild | `bundle exec jekyll clean && bundle exec jekyll build` |
| Add lesson | Create file in `lessons/` with front matter (see §2) |
| Deprecate lesson | Add `published: false` in front matter |
| Add workshop | Add file in `_workshops/` with `workshop_order` |
| New Q&A | Append to `_data/qa.yml` and include via `qa.html` |


  </div>
</details>


