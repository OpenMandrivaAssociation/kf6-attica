%undefine _debugsource_package

%define libname %mklibname KF6Attica
%define devname %mklibname KF6Attica -d
%define git 20230411

Name: kf6-attica
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/attica/-/archive/master/attica-master.tar.bz2
Summary: Qt library that implements the Open Collaboration Services API
URL: https://invent.kde.org/frameworks/attica
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6WidgetsTools)
BuildRequires: cmake(EGL)
BuildRequires: cmake(XKB)
BuildRequires: cmake(VulkanHeaders)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Widgets)
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
%{_libdir}/qt6/mkspecs/modules/qt_Attica.pri
%{_libdir}/qt6/doc/KF6Attica.*

%files -n %{libname}
%{_libdir}/libKF6Attica.so*
