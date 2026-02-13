# Fork Maintenance Guide

This guide explains how to maintain a personal fork of ani-cli when you want to keep it completely disconnected from the original repository, never contribute back, but still benefit from upstream updates.

## Your Goal: Independent Fork with Optional Upstream Sync

**You want to:**
- Maintain a completely independent version of ani-cli
- Never create pull requests or contribute back to the original
- Periodically pull updates from the original repo INTO your fork
- Keep your customizations while benefiting from upstream improvements

**Why this approach?**
- **Complete independence**: Your fork is yours alone - no obligations to upstream
- **Freedom to customize**: Change anything without worrying about compatibility with original
- **Selective updates**: Choose which upstream improvements to incorporate
- **No coordination overhead**: Don't need to discuss changes, follow project conventions, or wait for approvals
- **Stable base**: Original repo provides bug fixes and features you can optionally adopt

## Initial Setup

### 1. Fork on GitHub

Creates your own isolated copy with full control:

```bash
# Go to https://github.com/pystardust/ani-cli
# Click "Fork" → Choose your account
```

### 2. Clone Your Fork

Clone YOUR fork (becomes your primary workspace):

```bash
git clone https://github.com/YOUR-USERNAME/ani-cli.git
cd ani-cli
```

### 3. Add Upstream (One-Way Read-Only)

Add original repo ONLY for reading updates (you'll never push here):

```bash
# Add upstream as read-only source of updates
git remote add upstream https://github.com/pystardust/ani-cli.git

# Verify: origin is your fork, upstream is original
git remote -v
# origin    https://github.com/YOUR-USERNAME/ani-cli.git (fetch/push)
# upstream  https://github.com/pystardust/ani-cli.git (fetch)
```

## The One-Way Sync Model

**Visual representation:**
```
Original Repo (pystardust/ani-cli)
        ↓ (you pull updates FROM here)
        ↓
Your Fork (YOUR-USERNAME/ani-cli)
        ↑ (you push your changes here)
        ↑
   Your Local Machine
```

**Key principle:** Updates flow DOWNSTREAM from original to your fork. Your changes never flow upstream.

## Daily Workflow

### Making Your Own Changes

Work on your fork independently:

```bash
# Edit files
vim ani-cli

# Commit to your fork
./ani-cli --help  # Test your changes
git add ani-cli
git commit -m "My custom feature"
git push origin master  # Only goes to YOUR fork
```

**Why push only to origin?**
- `origin` is YOUR fork - you have full control
- You never push to upstream (original repo) - you don't have permission and don't want to
- Your changes stay isolated in your fork

### Periodic Upstream Sync

Every month or when you notice important updates, pull from original:

```bash
# Fetch latest from original (read-only)
git fetch upstream

# See what changed (optional review)
git log upstream/master --oneline -10

# Merge into your local branch
git checkout master
git merge upstream/master

# Resolve any conflicts (choose your version when in doubt)
# Test the merged code
./ani-cli --help

# Push merged result to your fork
git push origin master
```

**Why this workflow?**
- Fetches updates without disturbing your work
- Lets you review changes before merging
- Merges upstream improvements into your codebase
- Your customizations are preserved (unless they conflict)
- Conflicts = you decide which version wins

## Conflict Resolution Philosophy

When merging upstream creates conflicts, you have three options:

1. **Accept upstream changes** - Abandon your customization for their improvement
2. **Keep your changes** - Reject their modification, keep yours
3. **Merge manually** - Combine both changes intelligently

**Your priority order:**
1. Does upstream fix a bug you're affected by? → Take upstream
2. Does upstream break your customization? → Keep yours
3. Can both coexist? → Merge them

Example:
```bash
git merge upstream/master
# CONFLICT in ani-cli

# View conflict markers
vim ani-cli

# Decide: keep yours, take theirs, or combine
git checkout --ours ani-cli      # Keep YOUR version
git checkout --theirs ani-cli    # Take UPSTREAM version
# OR manually edit to combine

git add ani-cli
git commit
git push origin master
```

## Automation Options

### Option 1: Manual Sync (Recommended)

Full control over when and what to sync:

```bash
# Add this alias to ~/.gitconfig
git config --global alias.sync-upstream '!git fetch upstream && git checkout master && git merge upstream/master && git push origin master'

# Use it monthly


git sync-upstream
```

**Why manual?** 
- Review changes before applying
- Test merged code works
- Decide conflict resolution case-by-case
- Avoid surprise breakages

### Option 2: Automated Daily Fetch

If you want to stay current automatically:

```bash
# Create a script ~/bin/sync-ani-cli.sh
#!/bin/bash
cd ~/ani-cli || exit 1
git fetch upstream
git checkout master
git merge upstream/master --no-edit || exit 1
git push origin master
```

Add to crontab for weekly runs:
```bash
0 9 * * 1 ~/bin/sync-ani-cli.sh  # Every Monday at 9am
```

**Why automate?**
- Stay current with minimal effort
- Always have latest bug fixes
- But: may introduce untested changes

## What If You Never Sync?

**Consequences of never pulling from upstream:**
- **Bug accumulation**: Known bugs in original remain in your fork
- **Security issues**: Unpatched vulnerabilities persist
- **Compatibility drift**: Dependencies change, your fork breaks
- **Feature gap**: Miss useful new features
- **Maintenance burden**: You fix problems already solved upstream

**When to skip syncing:**
- Your fork works perfectly for your use case
- Original repo direction diverges from your needs
- You don't need new features
- Breaking changes outweigh benefits

**Recommendation:** Sync at least quarterly, even if just to review changes.

## Keeping Your Fork Alive

GitHub may flag forks as "stale" if inactive. To prevent this:

1. **Regular commits** (even small fixes)
2. **Enable GitHub Actions** (if present, they create activity)
3. **Update README** (add your own documentation)
4. **Star your own fork** (counts as activity)

**Why keep it active?**
- GitHub doesn't hide/archiv inactive forks
- Shows project is maintained
- Easier to find when you need it

## Common Questions

### Q: Can I completely disconnect from upstream?

**Yes.** Remove the upstream remote:
```bash
git remote remove upstream
```

Your fork becomes fully independent. You'll miss upstream updates but have zero dependencies.

### Q: What if upstream makes a breaking change?

**Don't merge it.** You're not obligated to accept any upstream changes:
```bash
git fetch upstream
# Review changes
git log upstream/master --oneline
# Decide not to merge this time
# Your fork stays on current version
```

### Q: Can I cherry-pick specific upstream commits?

**Yes.** Instead of full merge, pick specific improvements:
```bash
git fetch upstream
# Get commit hash from upstream
git cherry-pick abc123def
# Only applies that specific change
git push origin master
```

### Q: What about the license?

Forking respects the GPL v3.0 license. You must:
- Keep the license file
- Attribute original authors
- Share any distributed modifications under same license

Your independence is legal and encouraged!

## Summary

**Your Setup:**
- Fork = Your personal, independent version
- Upstream = Read-only source of optional updates
- One-way flow: upstream → your fork

**Your Workflow:**
1. Work on your fork freely (push to origin)
2. Periodically fetch from upstream (monthly recommended)
3. Review and merge upstream changes selectively
4. Resolve conflicts in favor of your needs
5. Never push to upstream (you don't have access anyway)

**Your Philosophy:**
- Independence over contribution
- Selective adoption of upstream improvements
- Your customizations take priority
- Original repo is a resource, not a dependency

**Bottom Line:** Your fork is YOURS. Use upstream as a convenience, not an obligation.
