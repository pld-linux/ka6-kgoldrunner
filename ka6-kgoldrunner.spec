#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.08.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kgoldrunner
Summary:	kgoldrunner
Name:		ka6-%{kaname}
Version:	24.08.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	fd760873317b6d16aa06b7d7463e70eb
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka6-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KGoldrunner is an action game where the hero runs through a maze,
climbs stairs, dig holes and dodges enemies in order to collect all
the gold nuggets and escape to the next level. Your enemies are also
after the gold.

%description -l pl.UTF-8
KGoldrunner jest grą akcji, gdzie bohater biegnie przez labirynt,
wchodzi po schodach, kopie doły i ucieka wrogom wcelu zebrania grudek
złota i przejścia do następnego poziomu. Twoi wrogowie również szukają
złota.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgoldrunner
%{_desktopdir}/org.kde.kgoldrunner.desktop
%{_iconsdir}/hicolor/*x*/apps/kgoldrunner.png
%{_datadir}/kgoldrunner
%{_datadir}/metainfo/org.kde.kgoldrunner.appdata.xml
%{_datadir}/qlogging-categories6/kgoldrunner.categories
%{_datadir}/knsrcfiles/kgoldrunner.knsrc
%{_datadir}/qlogging-categories6/kgoldrunner.renamecategories
