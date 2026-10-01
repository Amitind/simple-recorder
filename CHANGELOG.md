# Changelog

All notable changes to simple-recorder are listed here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0] - 2026-10-01

### Added
- `srec` and `simple-recorder` commands: fit an app window to a video shape and record it.
- Window picker: match by app name or title, or pick from a list (fzf).
- Presets: youtube, youtube-4k, youtube-720p, shorts (9:16), square, classic (4:3), exact-1080p.
- Audio picker: microphone and system sound are separate switches (`MIC`, `SYSTEM_AUDIO`, `-a`).
- Recording screen: aligned summary of window, preset, audio, encoder and file; one live
  colored status line (blinking dot, yellow on lost frames or slow encoding); a summary at the end.
  Colors turn off with `NO_COLOR` or when the output is not a terminal.
- Terminal title shows `● REC 00:01:23  app  preset  size` while recording, so the tab or
  taskbar shows it too. The old title comes back when the recording ends.
- Start-up check: lists every missing tool at once, why it is needed, and the install command
  for Fedora, Debian/Ubuntu or Arch.
- Config file at `~/.config/simple-recorder/config` in `key = value` format with `[preset.NAME]`
  sections. Every setting is listed with its default, grouped Basic and Advanced. Unknown
  settings, bad values and broken presets give a warning with the line number.
- `srec setup`: step-by-step choice of preset, audio, microphone, fps, separate audio and folder.
  Runs on first start.
- `srec config` opens the config; `srec config reset` writes a fresh one and keeps the old as `.bak`.
- Your own presets (`## Your presets` in the config) are listed first. Changed built-in presets
  show as "edited". `srec config reset` asks whether to keep them.
- Logo, icon and social preview image in `marketing/` (SVG and PNG, light and dark).
- `mic_device`: record a chosen microphone instead of the system default.
- Window border and on-top state are restored after recording.
- An output file that already exists is never overwritten: srec records to `name-2.mkv` instead.
- Fedora RPM spec in `packaging/` (build it yourself, or from COPR).
- Encoders: `ENCODER=auto` (default) uses h264_nvenc (NVIDIA GPU) when it works, else libx264 (CPU).
- `SEPARATE_AUDIO=yes` also saves the mic and the system sound as their own `.m4a` files (off by default).

[Unreleased]: https://github.com/Amitind/simple-recorder/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/Amitind/simple-recorder/releases/tag/v0.1.0
