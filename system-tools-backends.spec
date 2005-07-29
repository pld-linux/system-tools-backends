Summary:	GNOME System Tools backends
Summary(pl):	Backendy GNOME System Tools (narzêdzi systemowych GNOME)
Name:		system-tools-backends
Version:	1.3.1
Release:	1
License:	LGPL
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/system-tools-backends/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	20cc1c5663264ca8225d2aef2bc84de2
URL:		http://www.gnome.org/projects/gst/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	intltool >= 0.33
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backends for GNOME System Tools.

%description -l pl
Backendy dla GNOME System Tools (narzêdzi systemowych GNOME).

%prep
%setup -q

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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang system-tools-backends

%clean
rm -rf $RPM_BUILD_ROOT

%files -f system-tools-backends.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/setup-tool-backends
%dir %{_datadir}/setup-tool-backends/files
%attr(755,root,root) %{_datadir}/setup-tool-backends/files/*
%dir %{_datadir}/setup-tool-backends/scripts
%attr(755,root,root) %{_datadir}/setup-tool-backends/scripts/*
%{_pkgconfigdir}/*.pc
%{_aclocaldir}/*.m4
