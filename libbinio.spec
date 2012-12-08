%define	oname	binio
%define	major	1
%define	libname	%mklibname %{oname} %{major}
%define	libdev	%mklibname -d %{oname}
%define libstat %mklibname -d -s %{oname}

Summary:	Binary I/O stream class library
Name:		libbinio
Version:	1.4
Release:	10
License:	LGPLv2+
Group:		System/Libraries
URL:		http://libbinio.sourceforge.net/
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

%package -n	%{libdev}
Summary:	Development files for %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{libdev}
The binary I/O stream class library presents a platform-independent
way to access binary data streams in C++.

The library is hardware independent in the form that it transparently
converts between the different forms of machine-internal binary data
representation.

It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

This package contains C++ header files, the shared library symlink and
the developer documentation for %{name}.

%package -n	%{libstat}
Summary:	Static library for %{name}
Group:		Development/C++
Requires:	%{libdev} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n %{libstat}
The binary I/O stream class library presents a platform-independent
way to access binary data streams in C++.

The library is hardware independent in the form that it transparently
converts between the different forms of machine-internal binary data
representation.

It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

This package contains the static library of %{name}.

%prep
%setup -q
%patch1 -p1 -b .stringconversion
%patch2 -p1

%build
autoreconf -i
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libbinio.so.%{major}*

%files -n %{libdev}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_infodir}/*.info*
%{_libdir}/pkgconfig/*

%files -n %{libstat}
%{_libdir}/*.a

