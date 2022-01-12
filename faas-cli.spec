#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : faas-cli
Version  : 0.13.13
Release  : 42
URL      : https://github.com/openfaas/faas-cli/archive/0.13.13/faas-cli-0.13.13.tar.gz
Source0  : https://github.com/openfaas/faas-cli/archive/0.13.13/faas-cli-0.13.13.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT
Requires: faas-cli-bin = %{version}-%{release}
Requires: faas-cli-license = %{version}-%{release}
BuildRequires : buildreq-golang
BuildRequires : pypi(requests)

%description
Go package for expanding variables in a string using ${var} syntax. Includes support for bash string replacement functions.

%package bin
Summary: bin components for the faas-cli package.
Group: Binaries
Requires: faas-cli-license = %{version}-%{release}

%description bin
bin components for the faas-cli package.


%package license
Summary: license components for the faas-cli package.
Group: Default

%description license
license components for the faas-cli package.


%prep
%setup -q -n faas-cli-0.13.13
cd %{_builddir}/faas-cli-0.13.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641948412
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}  || go build -v -mod=vendor -ldflags='-X github.com/openfaas/faas-cli/version.Version=%{version}' -o ./faas-cli -buildmode=pie


%install
export SOURCE_DATE_EPOCH=1641948412
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/faas-cli
cp %{_builddir}/faas-cli-0.13.13/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/318d55ea7882b3b33bd94122474ff2c381496498
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/Azure/go-ansiterm/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/836ef1b46953afdb78ce3929bc6831ca83620b65
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/alexellis/go-execute/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/d85cff4a6cc09e9e3feb490e39a489a5628a36f7
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/20b06a68cf65738d43afa04acce0126f341c77f8
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/docker/docker/NOTICE %{buildroot}/usr/share/package-licenses/faas-cli/5476f2f91673ef040f1956907e7f45e72d5e11ee
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/drone/envsubst/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/572256a27f3a290c6c908d8259769ee9793f287e
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/7080652cc78cd9855d39e324529a3b5f3745dcd6
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/9174f93c54ad0022bbb9b445480cfb6b4217226a
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/konsorten/go-windows-terminal-sequences/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/e2ee43b586677eaafd7dd7af25adff48adfa7cf3
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/mitchellh/go-homedir/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/5ad2002bc8d2b22e2034867d159f71ba6258e18f
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/morikuni/aec/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/3faf341fbc32621fe1ac089ae2ab7a23980fc189
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/openfaas/faas-provider/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/f1ae47fecc13bcdc9beb6dc74be71d0fd4e34bbd
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/openfaas/faas/gateway/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/fc3fc032d02290b035bbf80a8a085da61cf75c3f
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/ryanuber/go-glob/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/f25ad3680192d554da0315f90fa71f63278a5326
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/a1c7852c717fed2c9a0284ed112ea66013230da6
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/faas-cli/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
cp %{_builddir}/faas-cli-0.13.13/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/b3c86ae465b21f7323059db335158b48187731c7
cp %{_builddir}/faas-cli-0.13.13/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/faas-cli-0.13.13/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/faas-cli-0.13.13/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/faas-cli/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/faas-cli-0.13.13/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/faas-cli/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
true
## install_append content
install -d %{buildroot}/usr/bin
install -p -m 755 ./faas-cli %{buildroot}/usr/bin/faas-cli
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/faas-cli

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/faas-cli/20b06a68cf65738d43afa04acce0126f341c77f8
/usr/share/package-licenses/faas-cli/318d55ea7882b3b33bd94122474ff2c381496498
/usr/share/package-licenses/faas-cli/3faf341fbc32621fe1ac089ae2ab7a23980fc189
/usr/share/package-licenses/faas-cli/5476f2f91673ef040f1956907e7f45e72d5e11ee
/usr/share/package-licenses/faas-cli/572256a27f3a290c6c908d8259769ee9793f287e
/usr/share/package-licenses/faas-cli/5ad2002bc8d2b22e2034867d159f71ba6258e18f
/usr/share/package-licenses/faas-cli/7080652cc78cd9855d39e324529a3b5f3745dcd6
/usr/share/package-licenses/faas-cli/836ef1b46953afdb78ce3929bc6831ca83620b65
/usr/share/package-licenses/faas-cli/9174f93c54ad0022bbb9b445480cfb6b4217226a
/usr/share/package-licenses/faas-cli/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/faas-cli/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/faas-cli/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/faas-cli/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/faas-cli/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/faas-cli/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/faas-cli/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
/usr/share/package-licenses/faas-cli/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/faas-cli/d85cff4a6cc09e9e3feb490e39a489a5628a36f7
/usr/share/package-licenses/faas-cli/e2ee43b586677eaafd7dd7af25adff48adfa7cf3
/usr/share/package-licenses/faas-cli/f1ae47fecc13bcdc9beb6dc74be71d0fd4e34bbd
/usr/share/package-licenses/faas-cli/f25ad3680192d554da0315f90fa71f63278a5326
/usr/share/package-licenses/faas-cli/fc3fc032d02290b035bbf80a8a085da61cf75c3f
