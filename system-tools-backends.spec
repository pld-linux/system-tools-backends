Summary:	GNOME System Tools backends
Summary(pl.UTF-8):	Backendy GNOME System Tools (narzędzi systemowych GNOME)
Name:		system-tools-backends
Version:	2.2.1
Release:	2
License:	LGPL
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/system-tools-backends/2.2/%{name}-%{version}.tar.bz2
# Source0-md5:	ee8a0f412e47748285672f9825647cd2
URL:		http://www.gnome.org/projects/gst/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	intltool >= 0.33
BuildRequires:	perl-Net-DBus >= 0.33.3-1
Requires:	perl-Net-DBus >= 0.33.3-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backends for GNOME System Tools.

%description -l pl.UTF-8
Backendy dla GNOME System Tools (narzędzi systemowych GNOME).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-stb-group=adm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus*/system.d/*
%{_datadir}/dbus-1/services/*.service

%dir %{_datadir}/%{name}-2.0
%dir %{_datadir}/%{name}-2.0/files
%dir %{_datadir}/%{name}-2.0/scripts
%attr(755,root,root) %{_datadir}/%{name}-2.0/files/*
%attr(755,root,root) %{_datadir}/%{name}-2.0/scripts/*.pl
%{_datadir}/%{name}-2.0/scripts/*.pm
%{_datadir}/%{name}-2.0/scripts/Init
%{_datadir}/%{name}-2.0/scripts/Network
%{_datadir}/%{name}-2.0/scripts/Shares
%{_datadir}/%{name}-2.0/scripts/Time
%{_datadir}/%{name}-2.0/scripts/Users
%{_datadir}/%{name}-2.0/scripts/Utils
%{_pkgconfigdir}/*.pc
