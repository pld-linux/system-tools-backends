Summary:	GNOME System Tools backends
Summary(pl.UTF-8):	Backendy GNOME System Tools (narzędzi systemowych GNOME)
Name:		system-tools-backends
Version:	2.6.0
Release:	1
License:	LGPL
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/system-tools-backends/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	faf321012e92b72305878cd684547c54
Source1:	%{name}.init
Patch0:		%{name}-logindefs.patch
Patch1:		%{name}-incompatible-gpasswd.patch
URL:		http://www.gnome.org/projects/gst/
BuildRequires:	PolicyKit-devel >= 0.5
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.1.2
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	libtool
BuildRequires:	perl-Net-DBus >= 0.33.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	PolicyKit
Requires:	dbus >= 1.1.2
Requires:	perl-Net-DBus >= 0.33.5
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
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/system-tools-backends

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add system-tools-backends
%service system-tools-backends restart "system-tools-backends daemon"

%preun
if [ "$1" = "0" ]; then
	%service system-tools-backends stop
	/sbin/chkconfig --del system-tools-backends
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/system-tools-backends
%attr(754,root,root) /etc/rc.d/init.d/system-tools-backends
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/system-tools-backends.conf
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/PolicyKit/policy/system-tools-backends.policy
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
