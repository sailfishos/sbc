Name:       libsbc

Summary:    SBC library
Version:    1.4
Release:    1
License:    LGPLv2+
URL:        http://www.kernel.org/pub/linux/bluetooth/
Source0:    %{name}-%{version}.tar.xz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(sndfile) >= 1.0.20
BuildRequires:  fdupes

%description
Bluetooth low-complexity, subband codec (SBC) library


%package tools
Summary:    SBC tools
Requires:   libsbc = %{version}-%{release}
License:    GPLv2+

%description tools
Description: %{summary}

%package devel
Summary:    SBC development headers and libraries
Requires:   libsbc = %{version}-%{release}

%description devel
Description: %{summary}


%prep
%autosetup -p1 -n %{name}-%{version}/sbc

%build
autoreconf -v -f -i
%configure --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install

%fdupes  %{buildroot}/%{_datadir}
%fdupes  %{buildroot}/%{_includedir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING.LIB
%{_libdir}/libsbc.so.*

%files tools
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/sbcdec
%{_bindir}/sbcenc
%{_bindir}/sbcinfo

%files devel
%defattr(-,root,root,-)
%{_libdir}/libsbc.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/sbc/*.h
