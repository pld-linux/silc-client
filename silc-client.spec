Summary:	Secure Internet Live Conferencing
Summary(pl):	SIRC - bezpieczne konferencje na ¿ywo poprzez internet
Name:		silc-client
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://silcnet.org/download/%{name}-%{version}.tar.bz2
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	autoconf
URL:		http://silcnet.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A: SILC (Secure Internet Live Conferencing) is a protocol which
provides secure conferencing services in the Internet over insecure
channel. SILC is IRC like although internally they are very different.
Biggest similarity between SILC and IRC is that they both provide
conferencing services and that SILC has almost same commands as IRC.
Other than that they are nothing alike.

%description -l pl
SILC (Secure Internet Live Conferencing) to protokó³ dostarczaj±cy
bezpiecznych us³ug w Internecie poprzez niezabezpieczone ³±cza. SILC
jest podobny do IRC poniewa¿ tak samo jak IRC dostarcza us³ug
konferencyjnych - ca³a reszta jest odmnienna od znanej z IRC.

%prep
%setup -q

%build
aclocal
autoconf
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
      
gzip -9nf CHANGES CREDITS README TODO doc/FAQ doc/example_silc.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/*

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%attr(755,root,root) %{_libdir}/%{name}/modules/*.so

%{_datadir}/%{name}
