# snugrec

Fit an app window to a video shape (16:9, 9:16, 1:1, 4:3) and record it, ready to upload.
No cropping, no black bars, no editing afterwards.

```
$ snugrec chrome
Window: Google-chrome | Docs - Google Chrome
Preset: youtube (window 16:9, video 1920x1080, 60fps, audio mic)
Recording to ~/Videos/google-chrome-youtube-2026-10-01-201500.mkv  (press q to stop)
```

## What it does

1. You pick a window: by name (`snugrec firefox`) or from a list (`snugrec`).
2. You pick a preset: YouTube, Shorts, square and others. Enter takes the default.
3. snugrec resizes the window to the exact shape of the preset, as large as your screen allows.
   It removes the title bar and keeps the window on top.
4. ffmpeg records only that window and scales it to the video size, for example 1920x1080.
5. Press `q` to stop. The title bar comes back.

The recording follows the window, so you can move it while you record.

## Install

```bash
curl -fLo ~/.local/bin/snugrec https://raw.githubusercontent.com/Amitind/snugrec/main/snugrec
chmod +x ~/.local/bin/snugrec
```

Needs: KDE Plasma on X11, `ffmpeg`, `xprop`, `qdbus` (qdbus-qt6), `pactl`, `fzf`.

```bash
sudo dnf install ffmpeg xprop qt6-qttools fzf pulseaudio-utils     # Fedora
sudo apt install ffmpeg x11-utils qdbus-qt6 fzf pulseaudio-utils   # Debian, Ubuntu
```

## Usage

```bash
snugrec                       # pick window and preset from lists
snugrec chrome                # window by class or title
snugrec -p shorts discord     # preset by name, no list
snugrec -a both chrome        # audio: mic | sys | both | none
snugrec -f 30 chrome          # frames per second
snugrec chrome demo.mkv       # choose the output file
snugrec -r chrome             # resize only, do not record
snugrec -e                    # edit the config
snugrec -h                    # help
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

The first run creates `~/.config/snugrec/config` with comments. Open it with `snugrec -e`.

```bash
PRESETS=(
  "youtube|16:9|1920x1080"
  "shorts|9:16|1080x1920"
  "mine|21:9|2560x1080"      # add your own: name|window|video
)
DEFAULT_PRESET=youtube
ASK_PRESET=yes        # no: always use DEFAULT_PRESET
FPS=60
AUDIO=mic             # mic | sys | both | none
ENCODER=libx264       # or h264_nvenc for NVIDIA GPUs
QUALITY=18            # lower is better and bigger
OUT_DIR=~/Videos
CONTAINER=mkv
NO_BORDER=yes
KEEP_ABOVE=yes
RESTORE_AFTER=yes
```

Delete the file to get the defaults back.

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
