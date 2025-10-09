# Dependabot Configuration

This repository uses [Dependabot](https://docs.github.com/en/code-security/dependabot) to automatically keep dependencies up-to-date.

## What Dependabot Monitors

The `.github/dependabot.yml` configuration file specifies three package ecosystems:

### 1. Ruby Gems (Bundler)
- **Location**: Root `Gemfile`
- **Purpose**: Jekyll and GitHub Pages dependencies
- **Schedule**: Weekly (Mondays)
- **Grouping**: Jekyll-related dependencies are grouped together for easier review

### 2. GitHub Actions
- **Location**: `.github/workflows/`
- **Purpose**: CI/CD workflow dependencies
- **Schedule**: Weekly (Mondays)

### 3. Python Packages (pip)
- **Location**: `scripts/requirements.txt`
- **Purpose**: Google Forms automation scripts (Google API clients)
- **Schedule**: Weekly (Mondays)
- **Grouping**: Google API packages are grouped together

## How It Works

1. **Automated PRs**: Dependabot automatically creates pull requests when updates are available
2. **Security**: Security updates are prioritized and may be created outside the regular schedule
3. **Limits**: Maximum 5 open PRs per ecosystem to avoid overwhelming maintainers
4. **Labels**: PRs are automatically labeled by dependency type (`dependencies`, `ruby`, `python`, `github-actions`)
5. **Commit Messages**: Conventional commits format with `chore(deps):` prefix

## Reviewing Dependabot PRs

When reviewing Dependabot pull requests:

1. **Check the changelog**: Review what changed in the new version
2. **Test locally**: For Jekyll/Python changes, test locally before merging
3. **Security updates**: Prioritize and merge security updates quickly
4. **Grouped updates**: Multiple minor/patch updates may be grouped in a single PR

### Testing Jekyll Updates Locally

```bash
bundle update
bundle exec jekyll serve
```

### Testing Python Script Updates

```bash
cd scripts
pip install -r requirements.txt
python3 test_parser.py
```

## Troubleshooting

If Dependabot encounters errors:

1. **Check the log**: Visit the Dependabot update log (requires write access)
2. **Verify file syntax**: Ensure `dependabot.yml` is valid YAML
3. **Check permissions**: Dependabot needs read access to dependency files
4. **Manual testing**: Test updates locally if automated checks fail

## Configuration Changes

To modify Dependabot behavior, edit `.github/dependabot.yml`:

- [Configuration options documentation](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file)
- After changes, Dependabot will automatically use the new configuration on next run
- Validate YAML syntax: `ruby -e "require 'yaml'; YAML.load_file('.github/dependabot.yml')"`

## Disabling Dependabot

To temporarily disable Dependabot updates:

1. Go to repository Settings → Security & analysis
2. Under "Dependabot version updates", click "Disable"
3. Or delete/rename `.github/dependabot.yml`

## Related Documentation

- [Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates)
- [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)
- [Configuring Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates)
