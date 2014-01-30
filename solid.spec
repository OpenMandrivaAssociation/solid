%define major 5
%define libname %mklibname KF5Solid %{major}
%define devname %mklibname KF5Solid -d
%define debug_package %{nil}

Name: solid
Version: 4.95.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/4.95.0/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 hardware access library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: qmake5
Requires: %{libname} = %{EVRD}
%if "%_lib" == "lib64"
BuildRequires: devel(libKF5DBusAddons(64bit))
%else
BuildRequires: devel(libKF5DBusAddons)
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

%files
%{_libdir}/qml/org/kde/solid
%{_datadir}/dbus-1/interfaces/*.xml

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Solid
