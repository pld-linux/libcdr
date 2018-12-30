#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	A library providing ability to interpret and import Corel Draw drawings
Summary(pl.UTF-8):	Biblioteka umożliwiająca interpretowanie i importowanie rysunków Corel Draw
Name:		libcdr
Version:	0.1.5
Release:	1
License:	MPL v2.0
Group:		Libraries
Source0:	https://dev-www.libreoffice.org/src/libcdr/%{name}-%{version}.tar.xz
# Source0-md5:	3040295f7a027c5bcdffbdb5bbdfd00a
URL:		https://wiki.documentfoundation.org/DLP/Libraries/libcdr
BuildRequires:	doxygen
BuildRequires:	boost-devel >= 1.41.0
BuildRequires:	lcms2-devel >= 2.0
BuildRequires:	libicu-devel
BuildRequires:	librevenge-devel >= 0.0.1
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	librevenge >= 0.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libcdr is library providing ability to interpret and import Corel Draw
drawings into various applications. You can find it being used in
libreoffice.

%description -l pl.UTF-8
Libcdr to biblioteka umożliwiająca interpretowanie i importowanie
rysunków Corel Draw do wielu aplikacji. Jest wykorzystywana przez
libreoffice.

%package devel
Summary:	Development files for libcdr
Summary(pl.UTF-8):	Pliki nagłówkowe dla libcdr
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lcms2-devel >= 2.0
Requires:	libicu-devel
Requires:	librevenge-devel >= 0.0.1
Requires:	libstdc++-devel >= 6:4.7
Requires:	zlib-devel

%description devel
This package contains the header files for developing applications
that use libcdr.

%description devel -l pl.UTF-8
Pen pakiet zawiera pliki nagłówkowe do tworzenia aplikacji opartych na
libcdr.

%package static
Summary:	Static libcdr library
Summary(pl.UTF-8):	Statyczna biblioteka libcdr
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcdr library.

%description static -l pl.UTF-8
Statyczna biblioteka libcdr.

%package apidocs
Summary:	libcdr API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libcdr
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API and internal documentation for libcdr library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libcdr.

%package tools
Summary:	Tools to transform Corel Draw drawings into other formats
Summary(pl.UTF-8):	Programy przekształcania rysunków Corel Draw do innych formatów
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform Corel Draw drawings into other formats. Currently
supported: XHTML, raw.

%description tools -l pl.UTF-8
Narzędzia do przekształcania rysunków Corel Draw do innych formatów.
Aktualnie obsługiwane są XHTML i raw.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcdr-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcdr-0.1.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdr-0.1.so
%{_includedir}/libcdr-0.1
%{_pkgconfigdir}/libcdr-0.1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcdr-0.1.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/%{name}

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cdr2raw
%attr(755,root,root) %{_bindir}/cdr2xhtml
%attr(755,root,root) %{_bindir}/cdr2text
%attr(755,root,root) %{_bindir}/cmx2raw
%attr(755,root,root) %{_bindir}/cmx2xhtml
%attr(755,root,root) %{_bindir}/cmx2text
