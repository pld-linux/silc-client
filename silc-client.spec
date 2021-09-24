# TODO: irssi plugin (--with-silc-plugin=%{_libdir}/irssi)
#
# Conditional build:
%bcond_with	perl	 # Perl support (requires perl-Irssi)

Summary:	Secure Internet Live Conferencing client
Summary(pl.UTF-8):	Klient SIRC (Secure Internet Live Conferencing)
Name:		silc-client
Version:	1.1.11
Release:	2
License:	GPL v2
Group:		Applications/Communications
#Source0Download: http://silcnet.org/client.html
Source0:	http://downloads.sourceforge.net/silc/%{name}-%{version}.tar.bz2
# Source0-md5:	cd47e57d61e7acf38d4283e6e98f2625
Patch0:		%{name}-libs.patch
Patch1:		%{name}-format.patch
URL:		http://silcnet.org/client.html
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
%{?with_perl:BuildRequires:	perl-devel >= 1:5.6.1}
BuildRequires:	pkgconfig
# silc >= 1.1, silcclient >= 1.1.1
BuildRequires:	silc-toolkit-devel >= 1.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SILC (Secure Internet Live Conferencing) is a secure conferencing
network. Silc is the SILC client which is used to connect to SILC
server and the SILC network. The silc client resembles IRC clients to
make the using easier for new users.

%description -l pl.UTF-8
SILC (Secure Internet Live Conferencing) to sieć do bezpiecznych
konferencji internetowych na żywo. Silc to klient SILC służący do
łączenia się z serwerem i siecią SILC. Klient silc przypomina
programy klienckie IRC, aby ułatwić korzystanie nowym użytkownikom.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# missing files in dist, but we don't need them, just stub
install -d lib/silcutil/symbian
touch lib/silcutil/symbian/Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd apps/irssi
%{__libtoolize}
%{__aclocal} -I.
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../..
%configure \
	--with-helpdir=%{_datadir}/%{name}/help \
	%{!?with_perl:--without-perl} \
	%{?with_perl:--with-perl-lib=vendor}
#	--with-silc-plugin=%{_libdir}/irssi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# interesting files packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README README.PLUGIN TODO doc/FAQ
%attr(755,root,root) %{_bindir}/silc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/silc.conf
%{_datadir}/silc
%if %{with perl}
# TODO: BR: perl-Irssi
%{perl_vendorarch}/Irssi/Silc.pm
%dir %{perl_vendorarch}/auto/Irssi/Silc
%attr(755,root,root) %{perl_vendorarch}/auto/Irssi/Silc/Silc.so
%endif
%{_mandir}/man1/silc.1*
