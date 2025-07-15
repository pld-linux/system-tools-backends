Summary:	GNOME System Tools backends
Summary(pl.UTF-8):	Backendy GNOME System Tools (narzędzi systemowych GNOME)
Name:		system-tools-backends
Version:	2.10.2
Release:	5
License:	LGPL v2+
Group:		Applications/System
Source0:	https://download.gnome.org/sources/system-tools-backends/2.10/%{name}-%{version}.tar.bz2
# Source0-md5:	edae148b31342aecae035051adc70c74
Patch0:		%{name}-logindefs.patch
Patch1:		%{name}-incompatible-gpasswd.patch
URL:		https://gitlab.gnome.org/Archive/system-tools-backends
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.1.2
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	perl-base
# to avoid building internal Net::DBus module
BuildRequires:	perl-Net-DBus >= 0.33.5
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.94
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	dbus >= 1.1.2
Requires:	dbus-glib >= 0.74
Requires:	glib2 >= 1:2.16.0
Requires:	perl-Net-DBus >= 0.33.5
Requires:	polkit >= 0.94
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backends for GNOME System Tools.

%description -l pl.UTF-8
Backendy dla GNOME System Tools (narzędzi systemowych GNOME).

%package devel
Summary:	Development files for GNOME System Tools backends
Summary(pl.UTF-8):	Pliki programistyczne dla backendów narzędzi systemowych GNOME
Group:		Development/Libraries
# doesn't require base; the only file is pkg-config specific, so let's require it
Requires:	pkgconfig

%description devel
This package contains files needed for GNOME System Tools backends
related development.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne przy programowaniu związanym z
backendami GNOME System Tools (narzędzi systemowych GNOME).

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-stb-group=adm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerun -- system-tools-backends < 2.8.0
%service system-tools-backends stop
/sbin/chkconfig --del system-tools-backends

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/system-tools-backends
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.SystemToolsBackends.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.SystemToolsBackends.service
%{_datadir}/dbus-1/system-services/org.freedesktop.SystemToolsBackends.*.service
%{_datadir}/polkit-1/actions/org.freedesktop.SystemToolsBackends.policy
%dir %{_datadir}/%{name}-2.0
%dir %{_datadir}/%{name}-2.0/files
%{_datadir}/%{name}-2.0/files/general_gprs_chatscript
%{_datadir}/%{name}-2.0/files/general_isdn_ppp_options
%{_datadir}/%{name}-2.0/files/general_pppoe_ppp_options
%dir %{_datadir}/%{name}-2.0/scripts
%attr(755,root,root) %{_datadir}/%{name}-2.0/scripts/SystemToolsBackends.pl
%{_datadir}/%{name}-2.0/scripts/*.pm
%{_datadir}/%{name}-2.0/scripts/Init
%{_datadir}/%{name}-2.0/scripts/Network
%{_datadir}/%{name}-2.0/scripts/Shares
%{_datadir}/%{name}-2.0/scripts/Time
%{_datadir}/%{name}-2.0/scripts/Users
%{_datadir}/%{name}-2.0/scripts/Utils

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/system-tools-backends-2.0.pc
