Summary:	Secure Internet Live Conferencing
Summary(pl.UTF-8):   SIRC - bezpieczne konferencje na żywo poprzez internet
Name:		silc-client
Version:	0.6
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://silcnet.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	e81887e2864454f2194be22b006953f1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	perl-base >= 1:5.6.1
URL:		http://silcnet.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A: SILC (Secure Internet Live Conferencing) is a protocol which
provides secure conferencing services in the Internet over insecure
channel. SILC is IRC like although internally they are very different.
Biggest similarity between SILC and IRC is that they both provide
conferencing services and that SILC has almost same commands as IRC.
Other than that they are nothing alike.

%description -l pl.UTF-8
SILC (Secure Internet Live Conferencing) to protokół dostarczający
bezpiecznych usług w Internecie poprzez niezabezpieczone łącza. SILC
jest podobny do IRC ponieważ tak samo jak IRC dostarcza usług
konferencyjnych - cała reszta jest odmnienna od znanej z IRC.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-helpdir=%{_datadir}/%{name}/help \
	--with-simdir=%{_libdir}/%{name}/modules \
	--with-etcdir=%{_sysconfdir}/%{name} \
	--with-logsdir=/tmp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_sitearch}

%{makeinstall} \
	helpdir=$RPM_BUILD_ROOT%{_datadir}/%{name}/help \
	silc_etcdir=$RPM_BUILD_ROOT%{_sysconfdir}/%{name} \
	silc_modulesdir=$RPM_BUILD_ROOT%{_libdir}/%{name}/modules \
	docdir=$RPM_BUILD_ROOT%{_docdir}

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/silcd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README TODO doc/FAQ doc/example_silc.conf
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%attr(755,root,root) %{_libdir}/%{name}/modules/*.so

%{_datadir}/%{name}
