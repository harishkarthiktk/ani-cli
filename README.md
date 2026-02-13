<p align=center>
<br>
<a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
<a href="#Linux"><img src="https://img.shields.io/badge/os-linux-brightgreen">
<a href="#MacOS"><img src="https://img.shields.io/badge/os-mac-brightgreen">
<a href="#Android"><img src="https://img.shields.io/badge/os-android-brightgreen">
<a href="#Windows"><img src="https://img.shields.io/badge/os-windows-yellowgreen">

<br>
<h1 align="center">
<a href="https://discord.gg/aqu7GpqVmR"><img src="https://invidget.switchblade.xyz/aqu7GpqVmR"></a>
<a href="matrix.md"><img src="/.assets/matrix-logo.svg" height=110></a>
<br>
<a href="https://github.com/port19x"><img src="https://img.shields.io/badge/lead-port19x-lightblue"></a>
<a href="https://github.com/CoolnsX"><img src="https://img.shields.io/badge/maintainer-CoolnsX-blue"></a>
<a href="https://github.com/justchokingaround"><img src="https://img.shields.io/badge/maintainer-justchokingaround-blue"></a>
<a href="https://github.com/Derisis13"><img src="https://img.shields.io/badge/maintainer-Derisis13-blue"></a>
<a href="https://github.com/71zenith"><img src="https://img.shields.io/badge/maintainer-71zenith-blue"></a>
<a href="https://github.com/ykhan21"><img src="https://img.shields.io/badge/maintainer-ykhan21-blue"></a>

</p>

<h3 align="center">
A cli to browse and watch anime (alone AND with friends). This tool scrapes the site <a href="https://allmanga.to/">allmanga.</a>
</h3>

<h1 align="center">
	Showcase
</h1>

[ani-cli-demo.webm](https://user-images.githubusercontent.com/44473782/224679247-0856e652-f187-4865-bbcf-5a8e5cf830da.webm)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [FAQ](#faq)
- [Contributing](./CONTRIBUTING.md)
- [Disclaimer](./disclaimer.md)

## Installation

[![Packaging status](https://repology.org/badge/vertical-allrepos/ani-cli.svg?minversion=4.0)](https://repology.org/project/ani-cli/versions)

See the **[Installation Guide](./INSTALL.md)** for detailed instructions on installing ani-cli and its dependencies on all supported platforms (Linux, macOS, Windows, Android, WSL).

### Quick Start

**Linux:**
```sh
# Debian/Ubuntu
sudo apt install ani-cli

# Fedora
sudo dnf copr enable derisis13/ani-cli
sudo dnf install ani-cli

# Arch
yay -S ani-cli
```

**macOS:**
```sh
brew install curl grep aria2 ffmpeg git fzf yt-dlp
brew install --cask iina
git clone "https://github.com/pystardust/ani-cli.git" && cd ./ani-cli
cp ./ani-cli "$(brew --prefix)"/bin
```

**Windows:**
```sh
scoop bucket add extras
scoop install ani-cli fzf ffmpeg mpv
```

**Android:**
```sh
pkg install ani-cli
```

For detailed installation instructions, dependency lists, troubleshooting, and uninstallation steps, see the [Installation Guide](./INSTALL.md).

## Usage

```sh
# Search and watch
ani-cli <anime_name>

# Continue from history
ani-cli -c

# Download episode
ani-cli -d <anime_name>

# Download all episodes
ani-cli -d -e all <anime_name>

# Download to specific folder
ani-cli -d ./Downloads <anime_name>

# Watch with VLC
ani-cli -v <anime_name>

# Watch dubbed version
ani-cli --dub <anime_name>

# Specify quality
ani-cli -q 1080 <anime_name>

# Watch together with friends (Syncplay)
ani-cli -s <anime_name>
```

For more options, run `ani-cli --help`.

## Features

- **Watch anime** from the terminal
- **Download episodes** for offline viewing
- **Multiple players** supported (mpv, iina, vlc)
- **Quality selection** (best, worst, or specific resolution)
- **History tracking** - continue where you left off
- **Episode ranges** - download or watch multiple episodes
- **Dubbed support** - switch between sub and dub
- **Skip intros** - automatic intro skipping (with ani-skip)
- **Syncplay** - watch with friends
- **Cross-platform** - Linux, macOS, Windows, Android, WSL

## Dependencies

ani-cli requires the following dependencies:

### Required
- grep, sed, curl, fzf
- mpv OR iina OR vlc

### For Downloading
- aria2c, yt-dlp, ffmpeg

### Optional
- ani-skip, syncplay, rofi, patch

See the [Installation Guide](./INSTALL.md) for platform-specific installation commands for all dependencies.

### Ani-Skip

Ani-skip is a script to automatically skip anime opening sequences. For install instructions visit [ani-skip](https://github.com/synacktraa/ani-skip).

**Note:** Ani-skip only works with mpv and does not work under Windows.

## FAQ

<details>
	
**Can I change subtitle language or turn them off?**
- No, the subtitles are baked into the video.

**Can I watch dub?**
- Yes, use `--dub`.

**Can I change dub language?**
- No.

**Can I change media source?**
- No (unless you can scrape that source yourself).

**Can I use vlc?**
- Yes, use `--vlc` or `export ANI_CLI_PLAYER=vlc`.

**Can I adjust resolution?**
- Yes, use `-q resolution`, for example `ani-cli -q 1080`.

**How can I download?**
- Use `-d`, it will download into your working directory or to the folder specified: `ani-cli -d ./Downloads <anime>`.

**Can I change download folder?**
- Yes, set the `ANI_CLI_DOWNLOAD_DIR` to your desired location, or use `ani-cli -d <path> <anime>`.

**How can I bulk download?**
- Use `-d -e all` to download all episodes, or `-d -e firstepisode-lastepisode` for a range, for example `ani-cli onepiece -d -e 1-1000`.

**All features are documented in `ani-cli --help`.**

</details>

## Homies

* [animdl](https://github.com/justfoolingaround/animdl): Ridiculously efficient, fast and light-weight (supports most sources: allmanga, zoro ...) (Python)
* [jerry](https://github.com/justchokingaround/jerry): stream anime with anilist tracking and syncing, with discord presence (Shell)
* [anipy-cli](https://github.com/sdaqo/anipy-cli): ani-cli rewritten in python (Python)
* [mangal](https://github.com/metafates/mangal): Download & read manga from any source with anilist sync (Go)
* [lobster](https://github.com/justchokingaround/lobster): Watch movies and series from the terminal (Shell)
* [mov-cli](https://github.com/mov-cli/mov-cli): Watch everything from your terminal. (Python)
* [dra-cla](https://github.com/CoolnsX/dra-cla): ani-cli equivalent for korean dramas (Shell)
* [redqu](https://github.com/port19x/redqu):  A media centric reddit client (Clojure)
* [doccli](https://github.com/TowarzyszFatCat/doccli):  A cli to watch anime with POLISH subtitles (Python)
* [GoAnime](https://github.com/alvarorichard/GoAnime): A CLI tool to browse, play, and download anime in Portuguese (Go)
* [Curd](https://github.com/Wraient/curd): A CLI tool to watch anime with Anilist, Discord RPC, Skip Intro/Outro/Filler/Recap (Go)
* [FastAnime](https://github.com/Benex254/FastAnime): browser anime experience from the terminal (Python)
* [ani-skip](https://github.com/KilDesu/ani-skip): Automatically skip opening and ending sequences for IINA on MacOS (Typescript, official IINA plugin API)
