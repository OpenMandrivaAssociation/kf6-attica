#undefine _debugsource_package

%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define major %(echo %{version} |cut -d. -f1-2)

%define libname %mklibname KF6Attica
%define devname %mklibname KF6Attica -d
#define git 20240217

Name: kf6-attica
Version: 6.20.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/attica/-/archive/master/attica-master.tar.bz2#/attica-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/attica-%{version}.tar.xz
%endif
Summary: Qt library that implements the Open Collaboration Services API
URL: https://invent.kde.org/frameworks/attica
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: qmake-qt6
BuildRequires: python
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6WidgetsTools)
BuildRequires: cmake(EGL)
BuildRequires: cmake(VulkanHeaders)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6CoreTools)
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: pkgconfig(xkbcommon)
# for QCH
BuildRequires: qt6-qtbase-sql-sqlite
BuildRequires: doxygen
Requires: %{libname} = %{EVRD}

%description
Qt library that implements the Open Collaboration Services API

%package -n %{libname}
Summary: Qt library that implements the Open Collaboration Services API
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Qt library that implements the Open Collaboration Services API

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Qt library that implements the Open Collaboration Services API

%prep
%autosetup -p1 -n attica-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/*

%files -n %{devname}
%{_includedir}/KF6/Attica
%{_libdir}/cmake/KF6Attica
%{_libdir}/pkgconfig/KF6Attica.pc

%files -n %{libname}
%{_libdir}/libKF6Attica.so*
