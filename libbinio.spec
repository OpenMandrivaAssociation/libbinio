%define	oname	binio
%define	major	1
%define	libname	%mklibname %{oname} %{major}
%define	devname	%mklibname -d %{oname}

Summary:	Binary I/O stream class library
Name:		libbinio
Version:	1.5
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://libbinio.sourceforge.net/
Source0:	https://github.com/adplug/libbinio/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

%description
The binary I/O stream class library presents a platform-independent
way to access binary data streams in C++.

The library is hardware independent in the form that it transparently
converts between the different forms of machine-internal binary data
representation.

It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

%package -n	%{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n	%{libname}
The binary I/O stream class library presents a platform-independent
way to access binary data streams in C++.

The library is hardware independent in the form that it transparently
converts between the different forms of machine-internal binary data
representation.

It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

This package contains the shared library needed to run applications
based on %{name}.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}binio1 < 1.4-11

%description -n %{devname}
This package contains C++ header files, the shared library symlink and
the developer documentation for %{name}.

%prep
%setup -q
%autopatch -p1
autoreconf -i

%build
%configure \
	--disable-static
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libbinio.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_infodir}/*.info*
%{_libdir}/pkgconfig/*

