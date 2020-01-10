%define	oname	binio
%define	major	1
%define	libname	%mklibname %{oname} %{major}
%define	devname	%mklibname -d %{oname}

Summary:	Binary I/O stream class library
Name:		libbinio
Version:	1.4
Release:	20
License:	LGPLv2+
Group:		System/Libraries
Url:		http://libbinio.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libbinio/%{name}-%{version}.tar.bz2
Patch1:		libbinio-1.4-string-conversion.patch
Patch2:		libbinio-1.4-gcc4.4.patch

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
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libbinio.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_infodir}/*.info*
%{_libdir}/pkgconfig/*

