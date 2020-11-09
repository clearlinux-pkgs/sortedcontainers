#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sortedcontainers
Version  : 2.3.0
Release  : 17
URL      : https://files.pythonhosted.org/packages/14/10/6a9481890bae97da9edd6e737c9c3dec6aea3fc2fa53b0934037b35c89ea/sortedcontainers-2.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/14/10/6a9481890bae97da9edd6e737c9c3dec6aea3fc2fa53b0934037b35c89ea/sortedcontainers-2.3.0.tar.gz
Summary  : Sorted Containers -- Sorted List, Sorted Dict, Sorted Set
Group    : Development/Tools
License  : Apache-2.0
Requires: sortedcontainers-license = %{version}-%{release}
Requires: sortedcontainers-python = %{version}-%{release}
Requires: sortedcontainers-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : tox
BuildRequires : tox-python

%description
========================
        
        `Sorted Containers`_ is an Apache2 licensed `sorted collections library`_,
        written in pure-Python, and fast as C-extensions.
        
        Python's standard library is great until you need a sorted collections
        type. Many will attest that you can get really far without one, but the moment
        you **really need** a sorted list, sorted dict, or sorted set, you're faced
        with a dozen different implementations, most using C-extensions without great
        documentation and benchmarking.
        
        In Python, we can do better. And we can do it in pure-Python!

%package license
Summary: license components for the sortedcontainers package.
Group: Default

%description license
license components for the sortedcontainers package.


%package python
Summary: python components for the sortedcontainers package.
Group: Default
Requires: sortedcontainers-python3 = %{version}-%{release}

%description python
python components for the sortedcontainers package.


%package python3
Summary: python3 components for the sortedcontainers package.
Group: Default
Requires: python3-core
Provides: pypi(sortedcontainers)

%description python3
python3 components for the sortedcontainers package.


%prep
%setup -q -n sortedcontainers-2.3.0
cd %{_builddir}/sortedcontainers-2.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604941000
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sortedcontainers
cp %{_builddir}/sortedcontainers-2.3.0/LICENSE %{buildroot}/usr/share/package-licenses/sortedcontainers/e79dc019b36c084ccc00738699f7c50030a3a0b6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sortedcontainers/e79dc019b36c084ccc00738699f7c50030a3a0b6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
