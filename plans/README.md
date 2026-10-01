# simple-recorder plans

## Active: polish before first release

**Now (no decision needed)**
- [x] Start-up check: lists all problems, reason, distro install line (tested with missing fzf/xprop + wayland)
- [x] README: "What you need" table, Fedora/Debian/Arch lines, qdbus path note
- [x] Recording screen: aligned header, blinking dot, yellow warnings after 3 s, end summary; NO_COLOR and non-tty tested
- [x] ENCODER=auto: probes nvenc, else libx264. 7 start-up drops on nvenc, 0 after
- [x] SEPARATE_AUDIO: <name>.mic.m4a / <name>.system.m4a via -map (tested with both)

**After decisions (questions asked 2026-10-01)**
- [ ] Config format (INI-style vs TOML vs bash) and a parser with warnings for unknown or old keys
- [ ] Config grouped: basic on top, advanced below; every line shows its default
- [ ] `srec setup` wizard: runs on first start, asks the main choices, writes the config
- [ ] `srec config` (edit), `srec config reset`
- [ ] Mic device choice

**Design**
- [ ] Logo and OG image: 3 concepts in `design/` (A crop frame recommended, red #E10600, Nimbus Sans). Pick one, then use it in README and npm

## Backlog
- User presets and combos (`srec presets` to list, create, delete)
- Separate configs per use (covered by user presets, so probably never)
- Wayland support (wf-recorder or gpu-screen-recorder), other desktops (GNOME)
- Live mute of mic or system sound while recording
- Pause and resume (SIGTSTP/SIGCONT, idea from scrast)
