Summary:	GNOME System Tools backends
Summary(pl.UTF-8):	Backendy GNOME System Tools (narzędzi systemowych GNOME)
Name:		system-tools-backends
Version:	2.8.3
Release:	1
License:	LGPL
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/system-tools-backends/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	403bf4b7c82455d995d6aa54613246c2
Patch0:		%{name}-logindefs.patch
Patch1:		%{name}-incompatible-gpasswd.patch
URL:		http://www.gnome.org/projects/gst/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.1.2
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	perl-Net-DBus >= 0.33.5
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.92
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	dbus >= 1.1.2
Requires:	perl-Net-DBus >= 0.33.5
Requires:	polkit >= 0.92
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backends for GNOME System Tools.

%description -l pl.UTF-8
Backendy dla GNOME System Tools (narzędzi systemowych GNOME).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
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
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/polkit-1/actions/org.freedesktop.SystemToolsBackends.policy
%dir %{_datadir}/%{name}-2.0
%dir %{_datadir}/%{name}-2.0/files
%dir %{_datadir}/%{name}-2.0/scripts
%attr(755,root,root) %{_datadir}/%{name}-2.0/files/general_isdn_ppp_options
%attr(755,root,root) %{_datadir}/%{name}-2.0/files/general_pppoe_ppp_options
%attr(755,root,root) %{_datadir}/%{name}-2.0/scripts/SystemToolsBackends.pl
%{_datadir}/%{name}-2.0/scripts/*.pm
%{_datadir}/%{name}-2.0/scripts/Init
%{_datadir}/%{name}-2.0/scripts/Network
%{_datadir}/%{name}-2.0/scripts/Shares
%{_datadir}/%{name}-2.0/scripts/Time
%{_datadir}/%{name}-2.0/scripts/Users
%{_datadir}/%{name}-2.0/scripts/Utils
%{_datadir}/%{name}-2.0/files
%{_pkgconfigdir}/system-tools-backends-2.0.pc
