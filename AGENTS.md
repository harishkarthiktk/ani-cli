# AGENTS.md

Guidelines for AI agents working on the ani-cli repository.

## Project Overview

ani-cli is a POSIX-compliant shell script (#!/bin/sh) for browsing and watching anime from the terminal. It scrapes allmanga.to and supports multiple platforms (Linux, macOS, Windows, Android, WSL).

## Build & Lint Commands

### Required Before Commit
```bash
# Run shellcheck
shellcheck -s sh -o all -e 2250 ./ani-cli

# Run shfmt (formatter)
shfmt -i 4 -ci -d ./ani-cli

# Check syntax
sh -n ./ani-cli

# Verify executable bit
chmod +x ./ani-cli
test -x "./ani-cli"

# Ensure no awk is used
! grep awk "./ani-cli"
```

### CI/CD Workflows
- **Shellcheck + Shfmt**: Linting and formatting validation
- **Executable Bit**: Ensures ani-cli is executable
- **No Awk Allowed**: Verifies no awk commands are added
- **Version Bump**: Requires version_number update on changes

## Code Style Guidelines

### Language & Compatibility
- **Target**: POSIX sh (#!/bin/sh), NOT bash
- **Avoid**: bashisms, awk (strictly forbidden), arrays, [[ ]], local keyword
- **Use**: POSIX-compliant features only

### Formatting (enforced by shfmt)
- **Indentation**: 4 spaces (not tabs)
- **Case statements**: Indented (use `-ci` flag)
- **Line endings**: Unix-style (LF)

### Naming Conventions
- **Functions**: snake_case, lowercase (e.g., `play_episode`, `get_links`)
- **Variables**: lowercase with underscores (e.g., `player_function`, `ep_list`)
- **Global constants**: UPPER_CASE for environment variable names

### Functions & Variables
```sh
# Good
my_function() {
    variable_name="value"
    curl "$url" || die "Failed to fetch URL"
}

# Bad - bashisms
function my_function() {
    local var="value"  # 'local' is not POSIX
}
```

### Error Handling & Output
- Use `die()` function for fatal errors
- Always quote variables: `"$variable"` not `$variable`
- Use `printf` instead of `echo` for portability
- Redirect errors to stderr: `>&2`

### Control Flow
```sh
case "$var" in
    pattern1)
        do_something
        ;;
esac

if [ "$condition" = "value" ]; then
    action
fi
```

### External Commands
- **Preferred**: grep, sed, curl, cut, tr, head, tail, wc
- **Forbidden**: awk (strictly prohibited)
- **Allowed**: fzf (UI), mpv/iina/vlc (players), aria2c/yt-dlp/ffmpeg (downloads)

### Version Management
**CRITICAL**: Bump `version_number` in ani-cli on every change:
```sh
version_number="4.10.4"  # Increment on each PR
```

## Pull Request Requirements

1. **Appease the linter**: Pass shellcheck and shfmt
2. **Bump the version**: Update version_number
3. **Adjust documentation**: Update README/INSTALL.md if applicable
4. **No extra dependencies**: Unless absolutely necessary
5. **Link issues**: Reference fixed issues

## Testing Changes

```bash
# Make script executable
chmod +x ./ani-cli

# Syntax check
bash -n ./ani-cli

# Test help and version
./ani-cli --help
./ani-cli --version

# Debug mode
ANI_CLI_PLAYER=debug ./ani-cli "anime name"
sh -x ./ani-cli args
```

## File Structure

```
ani-cli/              # Main script (POSIX sh)
ani-cli.1             # Man page
README.md             # Main documentation
INSTALL.md            # Installation guide
CONTRIBUTING.md       # Contribution guidelines
hacking.md            # Developer guide for scraping
.github/workflows/    # CI/CD configuration
```

## Environment Variables

- `ANI_CLI_MODE` - sub/dub
- `ANI_CLI_DOWNLOAD_DIR` - Download location
- `ANI_CLI_QUALITY` - best/worst/360/480/720/1080
- `ANI_CLI_PLAYER` - mpv/iina/vlc/debug/download
- `ANI_CLI_EXTERNAL_MENU` - 0=fzf, 1=rofi
- `ANI_CLI_HIST_DIR` - History file location
- `ANI_CLI_SKIP_INTRO` - Enable ani-skip

## Security Notes

- Never commit secrets or API keys
- Validate all user inputs
- Use `--data-urlencode` with curl for user input
- Be cautious with shell injection via filenames/URLs

## Resources

- [POSIX Shell Specification](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html)
- [Shellcheck Wiki](https://github.com/koalaman/shellcheck/wiki)
- [hacking.md](./hacking.md) - Scraping guide
- [CONTRIBUTING.md](./CONTRIBUTING.md) - PR guidelines
