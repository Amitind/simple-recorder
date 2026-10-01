# simple-recorder

One bash script, `srec` (also installed as `simple-recorder`). KDE Plasma 6 on X11: KWin script over qdbus resizes the window, ffmpeg `x11grab -window_id` records it. MIT, SemVer, Keep a Changelog.

## Layout
- `srec`: the whole tool. Config keys come from the `SPEC` table (`key|default|check|group|comment`), built-in presets from `BUILTIN_PRESETS`. `default_config()` generates the INI file from both, so add a setting in `SPEC` only.
- `packaging/`: Fedora RPM spec and build/COPR steps. `marketing/`: logo, icon, og image (light and dark). `plans/README.md`: open work, release steps, history.
- `.github/workflows/release-assets.yml`: attaches `srec` + `SHA256SUMS` to each release, fails if `VERSION=` does not match the tag.

## Rules
- `shellcheck srec` must be clean before a commit.
- Under `set -o pipefail`, never `cmd | grep -q` (SIGPIPE false failure). Use `grep -q x <<<"$(cmd)"` or `[[ $(cmd) == *x* ]]`.
- Colors only when `[ -t 1 ]` and `NO_COLOR` unset. Non-tty output has no live line and no terminal title.
- Bad config values warn with the line number and fall back to the default. A typo never stops a recording.
- Never overwrite an output file (`name-2.mkv` instead).
- npm package ships only `srec` (`files` in package.json). Check with `npm pack --dry-run`.

## Testing
- Never resize or record real app windows. Use a throwaway window: `kdialog --title srec-test --msgbox test &`, then `srec -p youtube -a none srec-test out.mkv`.
- Drive tty-only paths (live line, title, wizard) through `python3 -c 'import pty,sys; pty.spawn(sys.argv[1:])'` (no `script` binary here). For the setup wizard, put a fake `fzf` first in PATH.
- Point `XDG_CONFIG_HOME` at a temp dir for config tests, so the real config stays untouched.
- Write test files to a temp dir and delete them after.

## Release
Steps live in `plans/README.md` (changelog, `npm version`, push + tag, `gh release create`, `npm publish`, COPR). Push, tag, release and publish only when the maintainer says so.
