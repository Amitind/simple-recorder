# Fedora package

`simple-recorder.spec` builds a noarch RPM. It needs `/usr/bin/ffmpeg`, so Fedora's
`ffmpeg-free` and the RPM Fusion `ffmpeg` both work.

## Build the RPM yourself

```bash
sudo dnf install rpm-build rpmdevtools
git clone https://github.com/Amitind/simple-recorder && cd simple-recorder
rpmdev-setuptree                                    # makes ~/rpmbuild
spectool -g -R packaging/simple-recorder.spec       # downloads the release tarball to ~/rpmbuild/SOURCES
rpmbuild -ba packaging/simple-recorder.spec
sudo dnf install ~/rpmbuild/RPMS/noarch/simple-recorder-*.noarch.rpm
```

`srec` and `simple-recorder` are then in `/usr/bin`. Remove with `sudo dnf remove simple-recorder`.

## Publish on COPR (maintainer)

One time:

1. Make a Fedora account at https://accounts.fedoraproject.org and log in once at
   https://copr.fedorainfracloud.org.
2. `sudo dnf install copr-cli`
3. Copy the API token from https://copr.fedorainfracloud.org/api/ into `~/.config/copr`.
4. Create the project:
   ```bash
   copr-cli create simple-recorder --chroot fedora-43-x86_64 --chroot fedora-44-x86_64 \
     --chroot fedora-rawhide-x86_64 --description "Fit an app window to a video shape and record it"
   ```

Each release (after the `vX.Y.Z` tag is on GitHub and `Version:` in the spec matches):

```bash
spectool -g -R packaging/simple-recorder.spec
rpmbuild -bs packaging/simple-recorder.spec
copr-cli build simple-recorder ~/rpmbuild/SRPMS/simple-recorder-*.src.rpm
```

Users then install with:

```bash
sudo dnf copr enable amitind/simple-recorder
sudo dnf install simple-recorder
```

Use your Fedora account name in place of `amitind` if it differs.
