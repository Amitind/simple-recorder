# simple-recorder

Fit an app window to a video shape (16:9, 9:16, 1:1, 4:3) and record it, ready to upload.
No cropping, no black bars, no editing afterwards.

Command: `srec` (or the long name `simple-recorder`).

```
$ srec chrome

  Window   google-chrome | Docs - Google Chrome
  Preset   youtube window 16:9 video 1920x1080 at 60 fps
  Audio    microphone
  Encoder  h264_nvenc (NVIDIA GPU)
  File     ~/Videos/simple-recorder/google-chrome-youtube-2026-10-01-201500.mkv

  ● REC  00:01:12    18MB   60.0 fps  7 dropped   1.00x   q to stop
```

## What it does

1. You pick a window: by name (`srec firefox`) or from a list (`srec`).
2. You pick a preset: YouTube, Shorts, square and others. Enter takes the default.
3. srec resizes the window to the exact shape of the preset, as large as your screen allows.
   It removes the title bar, brings the window to the front and keeps it on top,
   so a window you click cannot cover the recording.
4. ffmpeg records only that window and scales it to the video size, for example 1920x1080.
5. Press `q` to stop. The title bar comes back and on-top goes back to how it was.

The recording follows the window, so you can move it while you record.

## Install

```bash
npm install -g simple-recorder
```

Or without npm:

```bash
curl -fLo ~/.local/bin/srec https://raw.githubusercontent.com/Amitind/simple-recorder/main/srec
chmod +x ~/.local/bin/srec
```

## What you need

| Need | Why | Fedora | Debian, Ubuntu | Arch |
|---|---|---|---|---|
| KDE Plasma 6 on X11 | KWin resizes the window; X11 lets ffmpeg record one window | | | |
| `ffmpeg` with x11grab and pulse | records and encodes | `ffmpeg` (RPM Fusion) | `ffmpeg` | `ffmpeg` |
| `xprop` | lists the open windows | `xprop` | `x11-utils` | `xorg-xprop` |
| `qdbus` | sends the resize script to KWin | `qt6-qttools` | `qdbus-qt6` | `qt6-tools` |
| `fzf` | the pick lists | `fzf` | `fzf` | `fzf` |
| `pactl` | finds the system sound device | `pulseaudio-utils` | `pulseaudio-utils` | `libpulse` |

```bash
sudo dnf install ffmpeg xprop qt6-qttools fzf pulseaudio-utils      # Fedora (ffmpeg from RPM Fusion)
sudo apt install ffmpeg x11-utils qdbus-qt6 fzf pulseaudio-utils    # Debian, Ubuntu
sudo pacman -S ffmpeg xorg-xprop qt6-tools fzf libpulse             # Arch
```

- Wayland does not work yet. On the login screen, pick "Plasma (X11)".
- PipeWire works too (through its PulseAudio layer, the default on current distros).
- On Fedora, the stock `ffmpeg-free` has no libx264. Install `ffmpeg` from
  [RPM Fusion](https://rpmfusion.org/Configuration) (`sudo dnf swap ffmpeg-free ffmpeg --allowerasing`).
- Debian and Ubuntu put qdbus at `/usr/lib/qt6/bin/qdbus`. srec finds it there.

If something is missing, srec lists every problem at once with the install command for your distro.

## Usage

```bash
srec                       # pick window and preset from lists
srec chrome                # window by class or title
srec -p shorts discord     # preset by name, no list
srec -a both chrome        # audio: mic | sys | both | none
srec -f 30 chrome          # frames per second
srec chrome demo.mkv       # choose the output file
srec -r chrome             # resize only, do not record
srec -e                    # edit the config
srec -h                    # help
```

## Presets

| Preset | Window | Video | For |
|---|---|---|---|
| youtube (default) | 16:9 | 1920x1080 | YouTube |
| youtube-4k | 16:9 | 3840x2160 | YouTube 4K |
| youtube-720p | 16:9 | 1280x720 | smaller files |
| shorts | 9:16 | 1080x1920 | YouTube Shorts, Reels, TikTok |
| square | 1:1 | 1080x1080 | Instagram, X |
| classic | 4:3 | 1440x1080 | slides, old formats |
| exact-1080p | 1920x1080 | 1920x1080 | no scaling (needs a free 1920x1080 area) |

A ratio window (16:9) becomes the largest window of that shape that fits between your panels.
The video is then scaled to the preset size. For sharp, unscaled video, use an exact size
and set your panels to auto-hide.

## Config

The first run creates `~/.config/simple-recorder/config` with comments. Open it with `srec -e`.

```bash
PRESETS=(
  "youtube|16:9|1920x1080"
  "shorts|9:16|1080x1920"
  "mine|21:9|2560x1080"      # add your own: name|window|video
)
DEFAULT_PRESET=youtube
ASK_PRESET=yes        # no: always use DEFAULT_PRESET
FPS=60
MIC=yes               # microphone
SYSTEM_AUDIO=no       # sound your computer plays
ASK_AUDIO=yes         # show the audio list each run
SEPARATE_AUDIO=no     # yes: also save mic and system sound as their own .m4a files
ENCODER=auto          # NVIDIA GPU if it works, else libx264 (CPU)
QUALITY=18            # lower is better and bigger
OUT_DIR=~/Videos/simple-recorder
CONTAINER=mkv
NO_BORDER=yes
KEEP_ABOVE=yes        # no: only bring the window to the front
RESTORE_AFTER=yes
```

Delete the file to get the defaults back.

## Smooth recording

- `ENCODER=auto` uses the NVIDIA GPU encoder when it works, which leaves the CPU free for the app.
- ffmpeg drops a few frames (about 5 to 20) while it starts. After that, the dropped count
  turns yellow if more frames are lost, and the speed turns yellow below 0.95x.
- With no audio, the file has no audio track at all.

## Limits

- KDE Plasma on X11 only. Wayland and other desktops are not supported yet.
- Two windows of the same app with the same title are both resized.
- A minimized window is restored first, because X11 cannot record a minimized window.
- Check that nothing private is visible before you record.

## How it works

One bash script. A KWin script (sent over D-Bus) resizes the window inside the screen's free area.
ffmpeg `x11grab -window_id` records the window, and PulseAudio/PipeWire records the sound.

Similar tools: [FFmpeg-Screen-Recorder](https://github.com/magiclen/FFmpeg-Screen-Recorder)
(pads the video to 16:9 instead of resizing the window), [shellrec](https://github.com/vifirsanova/shellrec),
[bashcaster](https://github.com/alphapapa/bashcaster). For a full GUI, use [OBS Studio](https://obsproject.com).

## License

MIT
