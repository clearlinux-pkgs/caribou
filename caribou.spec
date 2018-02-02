#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : caribou
Version  : 0.4.21
Release  : 6
URL      : https://download.gnome.org/sources/caribou/0.4/caribou-0.4.21.tar.xz
Source0  : https://download.gnome.org/sources/caribou/0.4/caribou-0.4.21.tar.xz
Summary  : The Caribou virtual on-screen keyboard library
Group    : Development/Tools
License  : LGPL-2.1
Requires: caribou-bin
Requires: caribou-python3
Requires: caribou-data
Requires: caribou-lib
Requires: caribou-locales
Requires: caribou-python
BuildRequires : clutter-dev
BuildRequires : gettext
BuildRequires : gobject-introspection-data
BuildRequires : gobject-introspection-dev
BuildRequires : intltool
BuildRequires : libgee-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxklavier)
BuildRequires : pkgconfig(xtst)
BuildRequires : pygobject-dev
BuildRequires : pygobject-python
BuildRequires : python3-dev

%description
Description
===========
Caribou is an input assistive technology intended for switch and
pointer users.

%package bin
Summary: bin components for the caribou package.
Group: Binaries
Requires: caribou-data

%description bin
bin components for the caribou package.


%package data
Summary: data components for the caribou package.
Group: Data

%description data
data components for the caribou package.


%package dev
Summary: dev components for the caribou package.
Group: Development
Requires: caribou-lib
Requires: caribou-bin
Requires: caribou-data
Provides: caribou-devel

%description dev
dev components for the caribou package.


%package lib
Summary: lib components for the caribou package.
Group: Libraries
Requires: caribou-data

%description lib
lib components for the caribou package.


%package locales
Summary: locales components for the caribou package.
Group: Default

%description locales
locales components for the caribou package.


%package python
Summary: python components for the caribou package.
Group: Default
Requires: caribou-python3

%description python
python components for the caribou package.


%package python3
Summary: python3 components for the caribou package.
Group: Default
Requires: python3-core

%description python3
python3 components for the caribou package.


%prep
%setup -q -n caribou-0.4.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507149611
%configure --disable-static --disable-schemas-compile PYTHON=/usr/bin/python3
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1507149611
rm -rf %{buildroot}
%make_install
%find_lang caribou

%files
%defattr(-,root,root,-)
/usr/lib64/gnome-settings-daemon-3.0/gtk-modules/caribou-gtk-module.desktop

%files bin
%defattr(-,root,root,-)
/usr/bin/caribou-preferences
/usr/libexec/antler-keyboard
/usr/libexec/caribou

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Caribou-1.0.typelib
/usr/share/antler/dark-key-border.svg
/usr/share/antler/style.css
/usr/share/caribou/layouts/fullscale/de.xml
/usr/share/caribou/layouts/fullscale/us.xml
/usr/share/caribou/layouts/scan/us.xml
/usr/share/caribou/layouts/tablet/de.xml
/usr/share/caribou/layouts/tablet/us.xml
/usr/share/caribou/layouts/touch/ara.xml
/usr/share/caribou/layouts/touch/de.xml
/usr/share/caribou/layouts/touch/fr.xml
/usr/share/caribou/layouts/touch/il.xml
/usr/share/caribou/layouts/touch/us.xml
/usr/share/dbus-1/services/org.gnome.Caribou.Antler.service
/usr/share/dbus-1/services/org.gnome.Caribou.Daemon.service
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.antler.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.caribou.gschema.xml
/usr/share/vala/vapi/caribou-1.0.deps
/usr/share/vala/vapi/caribou-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libcaribou/caribou.h
/usr/lib64/libcaribou.so
/usr/lib64/pkgconfig/caribou-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/gtk-2.0/modules/libcaribou-gtk-module.so
/usr/lib64/gtk-3.0/modules/libcaribou-gtk-module.so
/usr/lib64/libcaribou.so.0
/usr/lib64/libcaribou.so.0.0.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f caribou.lang
%defattr(-,root,root,-)

