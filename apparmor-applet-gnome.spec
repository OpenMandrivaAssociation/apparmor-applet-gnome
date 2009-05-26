Summary:	An AppArmor applet for Gnome
Name:		apparmor-applet-gnome
Version:	0.9
Epoch:		1
Release:	%mkrel 2
License:	GPL
Group:		Graphical desktop/GNOME
URL:		http://forge.novell.com/modules/xfmod/project/?apparmor
# upstream typo (missing -)
Source0:	apparmorapplet-gnome-%{version}.tar.bz2
Patch0:		apparmorapplet-gnome-0.9-build-fix.patch
BuildRequires:  libpanel-applet-2-devel
BuildRequires:  libaudit-devel
BuildRequires:  libglade2-devel
BuildRequires:  pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
AppArmor is a security framework that proactively protects the operating system
and applications.

This package contains an AppArmor applet for Gnome.


%prep
%setup -q -n apparmorapplet-gnome-%{version}
%patch0 -p1 

%build
%serverbuild

./configure --prefix=%{_prefix} --libexecdir=%{_libexecdir}
%make

%install
rm -rf %{buildroot}

%{makeinstall_std}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_prefix}/lib/bonobo/servers/*
%{_libexecdir}/apparmorapplet
%{_datadir}/pixmaps/*

