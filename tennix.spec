Summary:	A simple two-player tennis game
Summary(pl.UTF-8):Prosta gra w tenisa dla dw�ch graczy
Name:		tennix
Version:	0.3.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://thpinfo.com/2007/tennix/%{name}-%{version}.tar.gz
# Source0-md5:	996fb7c303f86f1aff474c96c96f92be
Source1:	%{name}.desktop
Patch0:		%{name}-datadir.patch
Patch1:		%{name}-makefile.patch
URL:		http://thpinfo.com/2007/tennix/
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tennix! a simple two-player tennis game. It features simple image
loading (with all game graphics being customizable by simply editing
them with a graphics editor like The GIMP), sound effects, stadium
audience sounds, and ball shadows.

%description -l pl.UTF-8
Tennix! jest prost� gr� w tenisa dla dw�ch graczy. Cechuje j� proste
�adowanie obrazk�w (kt�re z �atwo�ci� mo�na edytowa� za pomoc�
program�w graficznych takich jak GIMP), efekty d�wi�kowe, odg�osy
widowni oraz cieniowanie pi�ki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{__sed} -i 's@data@%{_datadir}/%{name}@' tennix.h

%build
%{__make} \
	CC="%{__cc}" \
	CXXFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install data/tennix-icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
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
