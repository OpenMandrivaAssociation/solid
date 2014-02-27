%define major 4
%define libname %mklibname KF5Solid %{major}
%define devname %mklibname KF5Solid -d
%define debug_package %{nil}

Name: solid
Version: 4.96.0
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

%files
%{_libdir}/qml/org/kde/solid
%{_datadir}/dbus-1/interfaces/*.xml

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Solid
%{_libdir}/qt5/mkspecs/modules/*
