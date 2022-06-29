%define major 5
%define libname %mklibname KF5Solid %{major}
%define devname %mklibname KF5Solid -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: solid
Version:	5.95.0
Release:	2
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 hardware access library
URL: http://kde.org/
License: GPL
Group: System/Libraries
# (tpg) sort cores
Patch0: sort_cores.patch
BuildRequires: cmake(ECM)
BuildRequires: media-player-info
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libplist-2.0)
BuildRequires: pkgconfig(libimobiledevice-1.0)
BuildRequires: pkgconfig(mount)
BuildRequires: flex
BuildRequires: bison
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: udisks
Requires: %{libname} = %{EVRD}
Requires: media-player-info

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

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1
%cmake_kde5 \
	-DWITH_NEW_POWER_ASYNC_API=ON \
	-DWITH_NEW_POWER_ASYNC_FREEDESKTOP=ON \
	-DWITH_NEW_SOLID_JOB=ON

%build
%ninja -C build

%install
%ninja_install -C build

L="$(pwd)/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=$(echo $i |cut -d/ -f5)
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/solid.categories
%{_datadir}/qlogging-categories5/solid.renamecategories
%{_bindir}/solid-hardware5
%{_bindir}/solid-power
%{_libdir}/qt5/qml/org/kde/solid

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Solid
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
