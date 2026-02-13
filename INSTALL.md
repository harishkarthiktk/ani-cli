# Installation Guide

This guide contains all installation instructions and dependencies for ani-cli.

## Table of Contents

- [Quick Install](#quick-install)
- [Dependencies](#dependencies)
- [Platform Installation](#platform-installation)
  - [Linux](#linux)
  - [macOS](#macos)
  - [Windows](#windows)
  - [Android](#android)
  - [WSL](#wsl)
- [Install from Source](#install-from-source)
- [Uninstall](#uninstall)
- [Troubleshooting](#troubleshooting)

## Quick Install

[![Packaging status](https://repology.org/badge/vertical-allrepos/ani-cli.svg?minversion=4.0)](https://repology.org/project/ani-cli/versions)

### Linux (Native Packages)

**Debian 13/unstable:**
```sh
sudo apt install ani-cli
```

**Fedora:**
```sh
# Enable RPM Fusion first: https://rpmfusion.org/Configuration
sudo dnf copr enable derisis13/ani-cli
sudo dnf install ani-cli
```

**Arch:**
```sh
yay -S ani-cli
# or: yay -S ani-cli-git
```

**Gentoo:**
```sh
sudo eselect repository enable guru
sudo emaint sync -r guru
sudo emerge -a ani-cli
# or: sudo emerge -a =app-misc/ani-cli-9999
```

**OpenSuse:**
```sh
# Add Packman repository first: https://en.opensuse.org/Additional_package_repositories#Packman
zypper addrepo https://download.copr.fedorainfracloud.org/results/derisis13/ani-cli/opensuse-tumbleweed-x86_64/ ani-cli
zypper dup
zypper install ani-cli
```

### macOS (Homebrew)

```sh
brew install curl grep aria2 ffmpeg git fzf yt-dlp
brew install --cask iina

git clone "https://github.com/pystardust/ani-cli.git" && cd ./ani-cli
cp ./ani-cli "$(brew --prefix)"/bin
cd .. && rm -rf ./ani-cli
```

### Windows (Scoop)

```sh
scoop bucket add extras
scoop install ani-cli
scoop install fzf ffmpeg mpv yt-dlp aria2
```

### Android (Termux)

```sh
pkg up -y
pkg install ani-cli
# For Android 14+: pkg install termux-am
```

For detailed platform-specific instructions, see [Platform Installation](#platform-installation) below.

## Dependencies

### Required Dependencies

These are always required for ani-cli to function:

- **grep** - Text pattern search
- **sed** - Stream editor for text manipulation
- **curl** - HTTP client for API requests
- **fzf** - Interactive fuzzy finder for the UI

### Media Players (Required - Choose One)

At least one media player must be installed:

- **mpv** - Default video player (Linux, Windows, Android)
- **iina** - mpv replacement for macOS (recommended over mpv on Mac)
- **vlc** - Alternative video player (all platforms)

### Download Tools (Required for `-d` Download Flag)

Required only if you want to download episodes:

- **aria2c** - Download manager for MP4 files
- **yt-dlp** - m3u8 stream downloader
- **ffmpeg** - m3u8 downloader (fallback when yt-dlp unavailable)

### Optional Dependencies

- **ani-skip** - Automatically skip anime intros/outros (mpv only)
- **syncplay** - Watch anime synchronously with friends
- **rofi** - Alternative to fzf for the interactive menu (use with `--rofi` flag)
- **patch** - Required for self-updating (`ani-cli -U`)
- **git** - Required for installing from source
- **logger** - For episode logging on Linux/macOS

## Platform Installation

### Linux

Native packages automatically install all required dependencies.

#### Manual Installation

If your distribution doesn't have a native package, install dependencies manually:

**Debian/Ubuntu:**
```sh
sudo apt install grep sed curl mpv fzf aria2 ffmpeg
# Optional: sudo apt install syncplay vlc
```

**Fedora:**
```sh
sudo dnf install grep sed curl mpv fzf aria2 ffmpeg
# Optional: sudo dnf install syncplay vlc
```

**Arch:**
```sh
sudo pacman -S grep sed curl mpv fzf aria2 ffmpeg yt-dlp
# Optional: sudo pacman -S syncplay vlc ani-skip rofi
```

Then install from source (see [Install from Source](#install-from-source)).

### macOS

#### Prerequisites

1. Install [Homebrew](https://docs.brew.sh/Installation)

2. Install dependencies:
```sh
brew install curl grep aria2 ffmpeg git fzf yt-dlp
brew install --cask iina
# Optional: brew install --cask syncplay
```

Note: iina is recommended over mpv on macOS for better integration with the OS.

#### Install ani-cli

```sh
git clone "https://github.com/pystardust/ani-cli.git" && cd ./ani-cli
cp ./ani-cli "$(brew --prefix)"/bin
cd .. && rm -rf ./ani-cli
```

### Windows

Windows requires Git Bash (from Git for Windows) to run ani-cli.

#### Setup Instructions

1. **Install Scoop package manager:**
   - Visit https://scoop.sh/ and follow the quickstart guide

2. **Install Windows Terminal:**
```powershell
scoop bucket add extras
scoop install extras/windows-terminal
```
   - On Windows 11, it's preinstalled

3. **Install Git:**
```powershell
scoop install git
```

4. **Configure Windows Terminal:**
   - Open Windows Terminal
   - Click the dropdown beside the new tab button
   - Go to `Settings > Profiles > Add a new profile`
   - Click `+ New empty profile`
   - Set Name: "Git Bash"
   - Set Command line: `%GIT_INSTALL_ROOT%\bin\bash.exe -i -l`
   - Set Icon: `%GIT_INSTALL_ROOT%\mingw64\share\git\git-for-windows.ico`
   - Set Starting Directory: `%USERPROFILE%`

5. **Install ani-cli:**
```sh
scoop bucket add extras
scoop install ani-cli
```

6. **Install dependencies:**
```sh
scoop install fzf ffmpeg mpv
# For downloads:
scoop install yt-dlp aria2
# Optional: scoop install vlc
```

7. **Update ani-cli:**
```sh
ani-cli -U
```

#### Windows Known Issues

- **Stuck in "Search anime:"**: Use Windows Terminal, not Git Bash terminal (mintty)
- **"No such file or directory" errors**: Make sure you're running in Git Bash, not PowerShell/CMD
- **curl issues**: ani-cli works best with curl 7.86.0+. Update via scoop if needed

### Android

#### Termux Package (Recommended)

1. Install [Termux](https://termux.com/)

2. Run:
```sh
pkg up -y
pkg install ani-cli
```

3. For Android 14+, also install:
```sh
pkg install termux-am
```

4. Install players separately via Play Store or F-Droid:
   - mpv or VLC as APKs

Note: Termux cannot check if APK players are installed, so a warning may appear during dependency checks.

#### Manual Installation

If you prefer not to use the Termux package:

```sh
pkg install grep sed curl fzf
# Install ani-cli from source (see below)
```

### WSL

1. Install ani-cli using your Linux distribution's instructions above

2. **Important**: Install the media player (mpv/vlc) on **Windows**, not WSL
   - Use Scoop on Windows: `scoop install mpv`
   - Ensure the player is on Windows PATH

3. See [this comment](https://github.com/pystardust/ani-cli/issues/1266#issuecomment-1926945757) for detailed WSL setup

## Install from Source

This method works for any unix-like operating system and is a baseline for porting efforts.

### Prerequisites

Install all [dependencies](#dependencies) for your platform first.

### Installation

```sh
git clone "https://github.com/pystardust/ani-cli.git"
sudo cp ani-cli/ani-cli /usr/local/bin
rm -rf ani-cli
```

### Post-Installation

Verify installation:
```sh
ani-cli --help
```

## Uninstall

### Linux

**apt:**
```sh
sudo apt remove ani-cli
sudo rm -f /etc/apt/trusted.gpg.d/ani-cli.asc /etc/apt/sources.list.d/ani-cli-debian.list
```

**dnf:**
```sh
sudo dnf remove ani-cli
dnf copr disable derisis13/ani-cli
# Optionally remove RPM Fusion
```

**zypper:**
```sh
zypper remove ani-cli
zypper removerepo ani-cli
# Optionally remove packman-essentials
```

**AUR:**
```sh
yay -R ani-cli
```

**Manual:**
```sh
sudo rm "/usr/local/bin/ani-cli"
```

### macOS

```sh
rm "$(brew --prefix)/bin/ani-cli"
```

### Windows

```sh
scoop uninstall ani-cli
```

Or manually in Git Bash (as administrator):
```sh
rm "/usr/bin/ani-cli"
```

### Android

**Termux package:**
```sh
pkg remove ani-cli
```

**Manual:**
```sh
rm "$PREFIX/bin/ani-cli"
```

## Troubleshooting

### Common Issues

1. **"No results found"**
   - Update to latest version: `sudo ani-cli -U` (Linux/Mac/Android) or `ani-cli -U` (Windows)
   - If issue persists, open a GitHub issue

2. **Missing dependencies**
   - Run `ani-cli --help` to see dependency warnings
   - Install missing tools according to [Dependencies](#dependencies)

3. **Windows: fzf not working**
   - Make sure you're using Windows Terminal, not Git Bash terminal (mintty)
   - Or run: `export MSYS=enable_pcon` before ani-cli

4. **Download issues**
   - Ensure yt-dlp or ffmpeg is installed for m3u8 streams
   - Ensure aria2c is installed for MP4 downloads

### Getting Help

- Read the [FAQ](../README.md#faq) in README
- Check [GitHub Issues](https://github.com/pystardust/ani-cli/issues)
- Join the [Discord](https://discord.gg/aqu7GpqVmR)
- Visit the [Matrix space](../matrix.md)

### Verification

After installing, verify all dependencies:
```sh
ani-cli --help
```

The script will check for required dependencies on startup and warn you if any are missing.
