Summary:	A simple two-player tennis game
Summary(pl.UTF-8):	Prosta gra w tenisa dla dwóch graczy
Name:		tennix
Version:	0.7.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://icculus.org/tennix/releases/%{name}-%{version}.tar.gz
# Source0-md5:	a0ef7a49b31d1755c46869333f756051
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-path.patch
URL:		http://icculus.org/tennix/
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tennix! a simple two-player tennis game. It features simple image
loading (with all game graphics being customizable by simply editing
them with a graphics editor like The GIMP), sound effects, stadium
audience sounds, and ball shadows.

%description -l pl.UTF-8
Tennix! jest prostą grą w tenisa dla dwóch graczy. Cechuje ją
proste ładowanie obrazków (które z łatwością można modyfikować
za pomocą programów graficznych takich jak GIMP), efekty
dźwiękowe, odgłosy widowni oraz cieniowanie piłki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DVERSION=\\\"%{version}\\\" `sdl-config --cflags`" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install tennix.desktop $RPM_BUILD_ROOT%{_desktopdir}
install data/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

install tennix.tnx $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
