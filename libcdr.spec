#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	A library providing ability to interpret and import Corel Draw drawings
Summary(pl.UTF-8):	Biblioteka umożliwiająca interpretowanie i importowanie rysunków Corel Draw
Name:		libcdr
Version:	0.0.8
Release:	1
License:	GPL v2+ or LGPL v2+ or MPL v1.1
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz
# Source0-md5:	9dde223b674b57fd90e6b78e9f39bcb9
URL:		http://www.freedesktop.org/wiki/Software/libcdr
BuildRequires:	doxygen
BuildRequires:	lcms2-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libwpd-devel >= 0.9
BuildRequires:	libwpg-devel >= 0.2
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
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
Requires:	libstdc++-devel
Requires:	libwpd-devel >= 0.9
Requires:	libwpg-devel >= 0.2
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
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--disable-werror

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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libcdr-0.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcdr-0.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdr-0.0.so
%{_includedir}/libcdr-0.0
%{_pkgconfigdir}/libcdr-0.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcdr-0.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cdr2raw
%attr(755,root,root) %{_bindir}/cdr2xhtml
%attr(755,root,root) %{_bindir}/cmx2raw
%attr(755,root,root) %{_bindir}/cmx2xhtml
