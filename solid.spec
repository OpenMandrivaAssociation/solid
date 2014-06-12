%define major 5
%define libname %mklibname KF5Solid %{major}
%define devname %mklibname KF5Solid -d
%define debug_package %{nil}

Name: solid
Version: 4.100.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 hardware access library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(libudev)
BuildRequires: flex bison
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
Requires: %{libname} = %{EVRD}
%if "%_lib" == "lib64"
BuildRequires: devel(libKF5DBusAddons(64bit))
BuildRequires: devel(libHUpnp(64bit))
%else
BuildRequires: devel(libKF5DBusAddons)
BuildRequires: devel(libHUpnp)
%endif

%description
The KDE Frameworks 5 hardware access library.

%package -n %{libname}
Summary: The KDE Frameworks 5 hardware access library
Group: System/Libraries

%description -n %{libname}
The KDE Frameworks 5 hardware access library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang
%{_bindir}/solid-hardware5
%{_libdir}/qml/org/kde/solid

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Solid
%{_libdir}/qt5/mkspecs/modules/*
