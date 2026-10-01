Name:           simple-recorder
Version:        0.1.0
Release:        1%{?dist}
Summary:        Fit an app window to a video shape and record it, ready to upload
License:        MIT
URL:            https://github.com/Amitind/simple-recorder
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

# File paths, so ffmpeg-free (Fedora) and ffmpeg (RPM Fusion) both work
Requires:       /usr/bin/ffmpeg
Requires:       /usr/bin/xprop
Requires:       /usr/bin/qdbus-qt6
Requires:       /usr/bin/fzf
Requires:       /usr/bin/pactl

%description
srec resizes an app window to an exact video shape (16:9, 9:16, 1:1, 4:3) and
records it with ffmpeg, so the video needs no cropping or editing.
KDE Plasma on X11.

%prep
%autosetup

%build

%install
install -Dpm 0755 srec %{buildroot}%{_bindir}/srec
ln -s srec %{buildroot}%{_bindir}/simple-recorder

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/srec
%{_bindir}/simple-recorder

%changelog
* Thu Oct 01 2026 Amit Yadav <goforamit16@gmail.com> - 0.1.0-1
- First release
