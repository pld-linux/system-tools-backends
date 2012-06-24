#
# TODO:
# - make %files section
# - test it
# - add pld th backends
#
Summary:	GNOME System Tools backends
Summary(pl):	Backendy GNOME System Tools (narz�dzi systemowych GNOME)
Name:		system-tools-backends
Version:	1.9.3
Release:	3
License:	LGPL
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/system-tools-backends/1.9/%{name}-%{version}.tar.bz2
# Source0-md5:	4ad33a82d18a990723393a9aa9677d35
Patch0:		%{name}-ac.patch
Patch1:		%{name}-m4.patch
URL:		http://www.gnome.org/projects/gst/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	intltool >= 0.33
BuildRequires:	perl-Net-DBus >= 0.33.3-0.2
Requires:	perl-Net-DBus >= 0.33.3-0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backends for GNOME System Tools.

%description -l pl
Backendy dla GNOME System Tools (narz�dzi systemowych GNOME).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus*/system.d/*
%{_aclocaldir}/*.m4
%{_datadir}/dbus-1/services/*.service
%dir %{_datadir}/%{name}-2.0
%dir %{_datadir}/%{name}-2.0/files
%attr(755,root,root) %{_datadir}/%{name}-2.0/files/*
%dir %{_datadir}/%{name}-2.0/scripts
%attr(755,root,root) %{_datadir}/%{name}-2.0/scripts/*.pl
%{_datadir}/%{name}-2.0/scripts/*.pm
%{_datadir}/%{name}-2.0/scripts/Init
%{_datadir}/%{name}-2.0/scripts/Network
%{_datadir}/%{name}-2.0/scripts/Shares
%{_datadir}/%{name}-2.0/scripts/Time
%{_datadir}/%{name}-2.0/scripts/Users
%{_datadir}/%{name}-2.0/scripts/Utils
%{_pkgconfigdir}/*.pc
