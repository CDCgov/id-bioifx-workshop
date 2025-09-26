# Bioinformatics Workshop Site

Static training site built with Jekyll (GitHub Pages compatible). This README provides explicit steps to clone, install dependencies, run locally, and verify.

## 1. Prerequisites

Install (macOS):
1. Xcode Command Line Tools (if not already):
   xcode-select --install
2. Homebrew (optional but recommended): https://brew.sh
3. Ruby (3.x recommended). Use one:
   - System (macOS 3.x+ on newer releases)
   - Or via Homebrew:
     brew install ruby
     echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
4. Bundler gem (after Ruby in PATH):
   gem install bundler

Verify:
ruby -v
gem -v
bundler -v

## 2. Clone Repository

Replace YOUR-USER if forking.

git clone https://github.com/YOUR-USER/id-bioifx-workshop.git
cd id-bioifx-workshop/bioinformatics-workshop

(Optional: keep a clean upstream remote)
git remote add upstream https://github.com/ORIGINAL-OWNER/id-bioifx-workshop.git

## 3. Install Gems

bundle install

This installs the github-pages gem (which pins Jekyll + plugins) and any development extras.

If you change the Gemfile later, re-run:
bundle install

## 4. Run Local Development Server

bundle exec jekyll serve --livereload

Default URL:
http://127.0.0.1:4000/

If this becomes a project site with a base path (e.g. repo-name), set baseurl in _config.yml and then access:
http://127.0.0.1:4000/repo-name/

Stop server: Ctrl+C

## 5. Clean & Rebuild (when things look stale)

bundle exec jekyll clean
bundle exec jekyll serve --livereload

Or one-line:
bundle exec jekyll clean && bundle exec jekyll build

## 6. Editing Content

- Lessons: /lessons/*.md (each file must start with YAML front matter: ---)
- Global config: _config.yml
- Shared includes: _includes/
- Layouts: _layouts/
- Styles: assets/css/style.css
- Palette: _data/colors.yml (only approved hex codes)
- Scripts: assets/js/

After saving changes, the livereload server auto-regenerates.

## 7. Copy Code Buttons & Collapsibles

Automatically added to fenced code blocks via assets/js/copy-code.js.
Use Markdown fenced blocks:
```python
print("Hello")