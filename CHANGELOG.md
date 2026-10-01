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
- Live status line while recording: time, size, fps, frames, dropped frames, speed.
- Config file at `~/.config/simple-recorder/config`, created on first run. Built-in defaults
  fill any setting the config leaves out.
- Window border and on-top state are restored after recording.
- Encoders: libx264 (CPU) and h264_nvenc (NVIDIA GPU).
