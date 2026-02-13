# Fork Maintenance Guide

This guide explains how to maintain your own fork of ani-cli when you don't plan to create pull requests to the original repository.

## Overview

Your fork becomes your **primary codebase** - a personal version that you maintain independently. You can still pull updates from the original repository when desired.

## Initial Setup

### 1. Fork on GitHub
- Go to https://github.com/pystardust/ani-cli
- Click the "Fork" button
- Choose your account/organization

### 2. Clone Your Fork

```bash
# Clone YOUR fork (not the original)
git clone https://github.com/YOUR-USERNAME/ani-cli.git
cd ani-cli

# Add original repo as "upstream" remote
git remote add upstream https://github.com/pystardust/ani-cli.git

# Verify your remotes
git remote -v
# Should show:
# origin    https://github.com/YOUR-USERNAME/ani-cli.git (fetch/push)
# upstream  https://github.com/pystardust/ani-cli.git (fetch/push)
```

## Remote Structure

- **origin** = Your fork (where you push your personal changes)
- **upstream** = Original pystardust/ani-cli (where you pull updates from)

## Maintenance Workflow

### Pulling Updates from Original Repo

When you want to incorporate updates from the original repository:

```bash
# Fetch latest changes from original repo
git fetch upstream

# Checkout your local master branch
git checkout master

# Merge upstream changes into your local branch
git merge upstream/master

# Push the merged changes to your fork
git push origin master
```

### Making Your Own Changes

```bash
# Edit files as needed...

# Stage and commit
vim ani-cli              # Make your edits
git add ani-cli
git commit -m "Your custom changes"

# Push to YOUR fork only
git push origin master
```

## When to Sync with Upstream

**Periodically pull from upstream** (recommended monthly or when you notice important updates):

- Bug fixes and security patches
- New features you want to use
- Dependency updates
- Compatibility improvements

**Benefits of periodic syncing:**
- Your fork stays current with important fixes
- You can cherry-pick which upstream changes to keep
- Prevents conflicts from piling up over time
- Easier to resolve issues when they arise

**If you NEVER want upstream changes:**
- Don't add the upstream remote
- Your fork becomes completely independent
- You'll maintain your own version entirely

## Quick Sync Alias

Add this to your `~/.gitconfig` for easier syncing:

```ini
[alias]
    sync-upstream = "!git fetch upstream && git checkout master && git merge upstream/master && git push origin master"
```

Then simply run:
```bash
git sync-upstream
```

## Handling Merge Conflicts

If you have conflicts when merging upstream:

```bash
git fetch upstream
git checkout master
git merge upstream/master

# If conflicts occur:
# 1. Edit the conflicting files
# 2. Choose which changes to keep (yours or upstream)
# 3. Stage resolved files: git add <file>
# 4. Complete merge: git commit
# 5. Push to your fork: git push origin master
```

## Common Scenarios

### Scenario 1: Update Your Fork with Latest Changes
```bash
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
```

### Scenario 2: Your Custom Changes + Upstream Updates
```bash
# Make your changes
git add .
git commit -m "Custom feature"
git push origin master

# Later, get upstream updates
git fetch upstream
git merge upstream/master
# Resolve any conflicts if needed
git push origin master
```

### Scenario 3: Completely Independent Fork
```bash
# Don't add upstream remote
# Just work with origin (your fork)
git clone https://github.com/YOUR-USERNAME/ani-cli.git

# Make changes and push to your fork only
git add .
git commit -m "Changes"
git push origin master
```

## Keeping Your Fork Alive

GitHub may mark forks as "stale" if inactive. To keep it active:

1. **Regular commits** - Even small updates
2. **Periodic syncs** - Pull from upstream occasionally
3. **Enable Actions** - If using GitHub Actions, they keep the repo active
4. **Update README** - Add your own documentation

## Summary

- Fork = Your personal version
- Upstream = Source of updates you can optionally pull
- You control what changes to accept from upstream
- Your fork remains independent and customized to your needs
