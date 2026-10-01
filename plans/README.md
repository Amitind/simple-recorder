# simple-recorder plans

## Active: after 0.1.0

**Next (in order)**
- [x] npm publish 0.1.0 (2026-10-01, 4 files: srec, package.json, README, LICENSE)
- [ ] npm trusted publishing: link the package to GitHub Actions so releases publish without an OTP
- [ ] Test on a clean Fedora with only the stock `ffmpeg-free` (no libx264; nvenc unconfirmed). If it fails, pick an encoder that it has, or say "RPM Fusion ffmpeg needed" in the spec and README
- [ ] COPR (deferred by Amit 2026-10-01; Fedora account exists): `copr-cli` + token, `copr-cli create`, `copr-cli build`. Steps in `packaging/README.md`. Then add the `dnf copr enable` line to README Install
- [ ] Release workflow `.github/workflows/release-assets.yml` first runs on the next release: check `srec` + `SHA256SUMS` attach
- [ ] `design/` (logo concepts + build script, untracked): commit, gitignore or delete. Amit to decide

**Release steps** (each version)
1. Move `[Unreleased]` in CHANGELOG to `[X.Y.Z] - date`, add the compare link.
2. `npm version X.Y.Z` (syncs `VERSION=` in srec, commits, tags). Bump `Version:` in the spec.
3. `git push && git push --tags`, `gh release create vX.Y.Z --notes-file <changelog section>` (workflow attaches srec).
4. `npm publish --otp=<code>` (until trusted publishing is set up), then COPR build.

## Backlog
- Official Fedora repos (review + sponsor), AUR, Ubuntu PPA
- `srec presets` to list, create, delete presets, and combos (preset + audio + fps). Your presets already work in the config
- Wayland support (wf-recorder or gpu-screen-recorder), other desktops (GNOME)
- Live mute of mic or system sound while recording
- Pause and resume (SIGTSTP/SIGCONT, idea from scrast)
- Separate configs per use (covered by user presets, so probably never)

## History
- 2026-10-01 v0.1.0 released on GitHub and npm (repo, tag, release with `srec` + `SHA256SUMS`, social preview og-light.png). Start-up check, recording screen, terminal title, encoder auto, separate audio, INI config with validation, setup wizard, config reset, your presets + edited marker, never-overwrite, Fedora RPM spec (local build tested), logo A1 + E in `marketing/`, shellcheck clean
