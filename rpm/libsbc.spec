Name:       libsbc

Summary:    SBC library
Version:    1.3
Release:    1
Group:      System/Libraries
License:    GPLv2
URL:        https://github.com/sailfishos/sbc
Source0:    %{name}-%{version}.tar.xz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(sndfile) >= 1.0.20
BuildRequires:  fdupes

%description
Bluetooth low-complexity, subband codec (SBC) library


%package tools
Summary:    SBC tools
Group:      System/Applications
Requires:   libsbc = %{version}-%{release}

%description tools
Description: %{summary}

%package devel
Summary:    SBC development headers and libraries
Group:      Development/Libraries
Requires:   libsbc = %{version}-%{release}

%description devel
Description: %{summary}


%prep
%setup -q -n %{name}-%{version}

%build
cd sbc
autoreconf -v -f -i
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
cd sbc
%make_install

%fdupes  %{buildroot}/%{_datadir}
%fdupes  %{buildroot}/%{_includedir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libsbc.so.*

%files tools
%defattr(-,root,root,-)
%{_bindir}/sbcdec
%{_bindir}/sbcenc
%{_bindir}/sbcinfo

%files devel
%defattr(-,root,root,-)
%{_libdir}/libsbc.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/sbc/*.h
