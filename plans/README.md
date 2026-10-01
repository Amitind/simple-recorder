# simple-recorder plans

## Active: polish before first release

**Now (no decision needed)**
- [x] Start-up check: lists all problems, reason, distro install line (tested with missing fzf/xprop + wayland)
- [x] README: "What you need" table, Fedora/Debian/Arch lines, qdbus path note
- [x] Recording screen: aligned header, blinking dot, yellow warnings after 3 s, end summary; NO_COLOR and non-tty tested
- [x] ENCODER=auto: probes nvenc, else libx264. 7 start-up drops on nvenc, 0 after
- [x] SEPARATE_AUDIO: <name>.mic.m4a / <name>.system.m4a via -map (tested with both)

**Decided 2026-10-01** (INI config, separate audio as files, mic in setup)
- [x] Config: INI `key = value` + `[preset.NAME]`; parser warns with line numbers, falls back to defaults
- [x] Config grouped Basic/Advanced, generated from one SPEC table, each line shows default
- [x] `srec setup` wizard (fzf + read), first start on a terminal
- [x] `srec config`, `srec config reset` (.bak kept)
- [x] mic_device, chosen in setup with friendly names

**Design**
- [x] Round 1: concepts A/B/C. Amit kept A and B, dropped C, asked for "Simple Recorder" and no YouTube tie-in
- [x] Picked 2026-10-01: icon A1 (square crop frame) + wordmark E (crop-name), light and dark, in `marketing/`. Logo in README header
- [ ] Set og-light.png as the GitHub social preview after the repo exists (Settings > Social preview, by hand)

## Backlog
- `srec presets` to list, create, delete presets, and combos (preset + audio + fps). Your presets already work in the config
- Separate configs per use (covered by user presets, so probably never)
- Wayland support (wf-recorder or gpu-screen-recorder), other desktops (GNOME)
- Live mute of mic or system sound while recording
- Pause and resume (SIGTSTP/SIGCONT, idea from scrast)
