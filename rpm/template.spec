%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-microstrain-inertial-driver
Version:        4.2.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS microstrain_inertial_driver package

License:        MIT
URL:            https://github.com/LORD-MicroStrain/microstrain_inertial
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-diagnostic-aggregator
Requires:       ros-rolling-diagnostic-updater
Requires:       ros-rolling-geometry-msgs
Requires:       ros-rolling-lifecycle-msgs
Requires:       ros-rolling-microstrain-inertial-msgs
Requires:       ros-rolling-nav-msgs
Requires:       ros-rolling-nmea-msgs
Requires:       ros-rolling-rclcpp-lifecycle
Requires:       ros-rolling-rosidl-default-runtime
Requires:       ros-rolling-rtcm-msgs
Requires:       ros-rolling-sensor-msgs
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-std-srvs
Requires:       ros-rolling-tf2
Requires:       ros-rolling-tf2-geometry-msgs
Requires:       ros-rolling-tf2-ros
Requires:       ros-rolling-ros-workspace
BuildRequires:  GeographicLib-devel
BuildRequires:  curl
BuildRequires:  eigen3-devel
BuildRequires:  git
BuildRequires:  jq
BuildRequires:  libcurl-devel
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-cpplint
BuildRequires:  ros-rolling-diagnostic-updater
BuildRequires:  ros-rolling-geometry-msgs
BuildRequires:  ros-rolling-lifecycle-msgs
BuildRequires:  ros-rolling-microstrain-inertial-msgs
BuildRequires:  ros-rolling-nav-msgs
BuildRequires:  ros-rolling-nmea-msgs
BuildRequires:  ros-rolling-rclcpp-lifecycle
BuildRequires:  ros-rolling-ros-environment
BuildRequires:  ros-rolling-rosidl-default-generators
BuildRequires:  ros-rolling-rtcm-msgs
BuildRequires:  ros-rolling-sensor-msgs
BuildRequires:  ros-rolling-std-msgs
BuildRequires:  ros-rolling-std-srvs
BuildRequires:  ros-rolling-tf2
BuildRequires:  ros-rolling-tf2-geometry-msgs
BuildRequires:  ros-rolling-tf2-ros
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-rolling-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-rolling-rosidl-interface-packages(member)

%if 0%{?with_weak_deps}
Supplements:    ros-rolling-rosidl-interface-packages(all)
%endif

%description
The ros_mscl package provides a driver for the LORD/Microstrain inertial
products.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Thu Apr 04 2024 Rob Fisher <rob.fisher@parker.com> - 4.2.0-1
- Autogenerated by Bloom

* Tue Apr 02 2024 Rob Fisher <rob.fisher@parker.com> - 4.1.0-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Rob Fisher <rob.fisher@parker.com> - 3.2.1-2
- Autogenerated by Bloom

