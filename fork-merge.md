# Fork Maintenance Guide

This guide explains how to maintain your own fork of ani-cli when you don't plan to create pull requests to the original repository.

## Why Fork?

**Forking lets you:**
- Create a personal, independent version of ani-cli
- Make custom modifications without affecting the original
- Optionally pull updates from the original when beneficial
- Maintain control over which changes you accept

**Why NOT contribute back via PR?**
- You may have personal customizations not suitable for general use
- You want complete control over the codebase
- You're maintaining a specialized variant
- You simply want to experiment freely

## Overview

Your fork becomes your **primary codebase** - a personal version that you maintain independently. You can still pull updates from the original repository when desired.

## Initial Setup

### 1. Fork on GitHub

**Why:** Creates your own copy under your GitHub account where you have full write access.

- Go to https://github.com/pystardust/ani-cli
- Click the "Fork" button
- Choose your account/organization

### 2. Clone Your Fork

**Why:** You clone YOUR fork (not the original) so your commits push to your fork by default.

```bash
# Clone YOUR fork (not the original)
git clone https://github.com/YOUR-USERNAME/ani-cli.git
cd ani-cli

# Add original repo as "upstream" remote
# Why: This gives you access to updates from the original without changing your default push target
git remote add upstream https://github.com/pystardust/ani-cli.git

# Verify your remotes
git remote -v
# Should show:
# origin    https://github.com/YOUR-USERNAME/ani-cli.git (fetch/push)
# upstream  https://github.com/pystardust/ani-cli.git (fetch/push)
```

## Remote Structure

**Two remotes exist for different purposes:**

- **origin** = Your fork (where you push your personal changes)
  - Why: This is your personal copy where you have full control
  
- **upstream** = Original pystardust/ani-cli (where you pull updates from)
  - Why: You can fetch updates from the original without affecting your workflow

**Why two remotes?** 
- Separates where you push (your fork) from where you might pull updates (original)
- Allows you to work independently while staying optionally connected to improvements

## Maintenance Workflow

### Pulling Updates from Original Repo

**Why do this?** To benefit from bug fixes, security patches, and new features developed by the original maintainers without losing your customizations.

```bash
# Fetch latest changes from original repo
# Why: Downloads updates without applying them yet (safe to inspect first)
git fetch upstream

# Checkout your local master branch
# Why: Ensures you're on the right branch before merging
git checkout master

# Merge upstream changes into your local branch
# Why: Combines original updates with your customizations
git merge upstream/master

# Push the merged changes to your fork
# Why: Updates your GitHub fork with the merged changes
git push origin master
```

### Making Your Own Changes

**Why:** Your fork is independent - you can modify anything without permission or affecting others.

```bash
# Edit files as needed...

# Stage and commit
vim ani-cli              # Make your edits
git add ani-cli
git commit -m "Your custom changes"

# Push to YOUR fork only
# Why: origin is your fork, so this goes to your personal version
git push origin master
```

## When to Sync with Upstream

**Why periodically sync?** 
- Original repo gets bug fixes you don't want to miss
- Security patches protect you from vulnerabilities
- New features may be useful for your custom version
- Dependency updates ensure compatibility
- Prevents technical debt from accumulating

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
- Why do this? Complete isolation from upstream decisions/changes

## Quick Sync Alias

**Why:** Typing the full sync command repeatedly is tedious. An alias saves time and reduces errors.

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

**Why conflicts happen:** When you modify code that upstream also modified, Git can't automatically decide which version to keep.

```bash
git fetch upstream
git checkout master
git merge upstream/master

# If conflicts occur:
# 1. Edit the conflicting files
# 2. Choose which changes to keep (yours or upstream)
#    Why: You're the maintainer - you decide what works for your fork
# 3. Stage resolved files: git add <file>
# 4. Complete merge: git commit
# 5. Push to your fork: git push origin master
```

**Why handle conflicts promptly?**
- Conflicts get harder to resolve the longer you wait
- Regular small syncs prevent massive conflict pile-ups
- Keeps your fork functional and up-to-date

## Common Scenarios

### Scenario 1: Update Your Fork with Latest Changes

**Why:** You want the latest bug fixes without losing your customizations.

```bash
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
```

### Scenario 2: Your Custom Changes + Upstream Updates

**Why:** You're actively developing your own features while still benefiting from upstream improvements.

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

**Why:** You want total isolation - no connection to upstream whatsoever. Good for experimental variants or completely different directions.

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

**Why does GitHub care about activity?**
- GitHub may hide or mark inactive forks as "stale"
- Regular activity shows the project is maintained
- Ensures your fork remains discoverable and functional

GitHub may mark forks as "stale" if inactive. To keep it active:

1. **Regular commits** - Even small updates
   - Why: Shows the fork is actively maintained
   
2. **Periodic syncs** - Pull from upstream occasionally
   - Why: Demonstrates ongoing engagement with the project
   
3. **Enable Actions** - If using GitHub Actions, they keep the repo active
   - Why: Automated activity counts toward repo health
   
4. **Update README** - Add your own documentation
   - Why: Clarifies your fork's purpose and differences

## Summary

- **Fork** = Your personal version (full control)
- **Upstream** = Source of optional updates (your choice to pull)
- **Why two remotes?** Separates your work from optional external updates
- **Why sync periodically?** Benefit from fixes while keeping your customizations
- **Why maintain activity?** Keeps fork healthy and functional on GitHub

**Your fork remains independent and customized to your needs** - you decide what changes to accept and when.
