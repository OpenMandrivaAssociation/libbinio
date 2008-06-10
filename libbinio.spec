%define	oname	binio

Summary:	Binary I/O stream class library
Name:		libbinio
Version:	1.4
Release:	%mkrel 5
Source0:	http://prdownloads.sourceforge.net/libbinio/%{name}-%{version}.tar.bz2
Patch0:		libbinio-1.4-no-long-long.patch
Patch1:		libbinio-1.4-string-conversion.patch
URL:		http://libbinio.sourceforge.net/
License:	LGPLv2+
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The binary I/O stream class library presents a platform-independent
way to access binary data streams in C++.

The library is hardware independent in the form that it transparently
converts between the different forms of machine-internal binary data
representation.

It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

%define	major	1
%define	libname	%mklibname %{oname} %{major}
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

%define	libdev	%mklibname -d %{oname}
%package -n	%{libdev}
Summary:	Development files for %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname -d %{oname} 1}

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

%define libstat %mklibname -d -s %{oname}
%package -n	%{libstat}
Summary:	Static library for %{name}
Group:		Development/C++
Requires:	%{libdev} = %{version}
Provides:	%{name}-static-devel = %{version}-%{release}
Obsoletes:	%{mklibname -s -d %{oname} 1}

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
%patch0 -p1 -b .nolonglong
%patch1 -p1 -b .stringconversion

%build
autoreconf -i
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%post -n %{libdev}
%_install_info %{name}.info

%postun -n %{libdev}
%_remove_install_info %{name}.info

%files -n %{libname}
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%{_libdir}/libbinio.so.%{major}*

%files -n %{libdev}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_infodir}/*.info*
%{_libdir}/pkgconfig/*

%files -n %{libstat}
%defattr(-,root,root)
%{_libdir}/*.a

