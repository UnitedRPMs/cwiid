%global commit0 d1f387c613181b4a2a4444aba9692c2164de9aea

Name:           cwiid
Version:        3.0.0
Release:        1%{?dist}
Summary:        Wiimote interface library

Group:          System Environment/Libraries
License:        GPLv2+
URL:            https://github.com/azzra/python3-wiimote

Source:		https://github.com/azzra/python3-wiimote/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  bluez-libs-devel 
BuildRequires:  gawk 
BuildRequires:  bison 
BuildRequires:  flex
BuildRequires:  autoconf 
BuildRequires:  automake
BuildRequires:	gcc gcc-c++
BuildRequires:	python3-devel


%description
Cwiid is a library that enables your application to communicate with
a wiimote using a bluetooth connection.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}, bluez-libs-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        python3
Summary:        Python binding for %{name}
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}

%description    python3
python3 binding for %{name}

%prep
%autosetup -n python3-wiimote-%{commit0}

%build
    aclocal
    autoconf
%configure \
    --disable-ldconfig --docdir="%{_pkgdocdir}" CC="gcc %{optflags}" --disable-static 
make %{?_smp_mflags}

%install
    pushd libcwiid
    %make_install
popd
pushd python
python3 setup.py install --root=%{buildroot} --optimize=1
popd


find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm $RPM_BUILD_ROOT/%{_libdir}/*.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS NEWS README.md COPYING ChangeLog
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files python3
%{python3_sitearch}/*

%changelog

* Sat Jun 08 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.0-1
- Initial build
