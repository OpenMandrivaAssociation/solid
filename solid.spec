%define major 5
%define libname %mklibname KF5Solid %{major}
%define devname %mklibname KF5Solid -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: solid
Version:	5.40.0
Release:	1
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
BuildRequires: flex
BuildRequires: bison
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

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang
%{_bindir}/solid-hardware5
%{_libdir}/qt5/qml/org/kde/solid

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Solid
%{_libdir}/qt5/mkspecs/modules/*
