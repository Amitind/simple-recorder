# Changelog

All notable changes to simple-recorder are listed here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- `srec` and `simple-recorder` commands: fit an app window to a video shape and record it.
- Window picker: match by app name or title, or pick from a list (fzf).
- Presets: youtube, youtube-4k, youtube-720p, shorts (9:16), square, classic (4:3), exact-1080p.
- Audio picker: microphone and system sound are separate switches (`MIC`, `SYSTEM_AUDIO`, `-a`).
- Recording screen: aligned summary of window, preset, audio, encoder and file; one live
  colored status line (blinking dot, yellow on lost frames or slow encoding); a summary at the end.
  Colors turn off with `NO_COLOR` or when the output is not a terminal.
- Start-up check: lists every missing tool at once, why it is needed, and the install command
  for Fedora, Debian/Ubuntu or Arch.
- Config file at `~/.config/simple-recorder/config`, created on first run. Built-in defaults
  fill any setting the config leaves out.
- Window border and on-top state are restored after recording.
- Encoders: `ENCODER=auto` (default) uses h264_nvenc (NVIDIA GPU) when it works, else libx264 (CPU).
- `SEPARATE_AUDIO=yes` also saves the mic and the system sound as their own `.m4a` files (off by default).
