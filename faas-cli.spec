#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v3
# autospec commit: c1050fe
#
Name     : faas-cli
Version  : 0.16.21
Release  : 67
URL      : https://github.com/openfaas/faas-cli/archive/0.16.21/faas-cli-0.16.21.tar.gz
Source0  : https://github.com/openfaas/faas-cli/archive/0.16.21/faas-cli-0.16.21.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 MIT
Requires: faas-cli-bin = %{version}-%{release}
Requires: faas-cli-license = %{version}-%{release}
BuildRequires : go
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Package warnings implements error handling with non-fatal errors (warnings).
import path:   "gopkg.in/warnings.v0"
package docs:  https://godoc.org/gopkg.in/warnings.v0
issues:        https://github.com/go-warnings/warnings/issues
pull requests: https://github.com/go-warnings/warnings/pulls

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
%setup -q -n faas-cli-0.16.21
cd %{_builddir}/faas-cli-0.16.21

%build
## build_prepend content
unset CLEAR_DEBUG_TERSE
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701954880
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
make  %{?_smp_mflags}  || go build -v -mod=vendor -ldflags='-X github.com/openfaas/faas-cli/version.Version=%{version}' -o ./faas-cli -buildmode=pie


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1701954880
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/faas-cli
cp %{_builddir}/faas-cli-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/ce62120d32a64c44b0e61ee13b9b5fd2c0cea2a1 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/Azure/go-ansiterm/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/836ef1b46953afdb78ce3929bc6831ca83620b65 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/Masterminds/semver/LICENSE.txt %{buildroot}/usr/share/package-licenses/faas-cli/020acfcf6d6bd6d701d19bd16f49d0bf18441779 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/VividCortex/ewma/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/5fcf3d8a80be9b86a2c442ab938090611e6ee317 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/alexellis/arkade/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/3dbdeb041ef56b91e6c094423ab0c23b1dba025f || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/alexellis/go-execute/v2/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/95dc7028a6518eb427e543f891c774df3b24b0cf || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/alexellis/hmac/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/f1ae47fecc13bcdc9beb6dc74be71d0fd4e34bbd || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/alexellis/hmac/v2/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/f1ae47fecc13bcdc9beb6dc74be71d0fd4e34bbd || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/bep/debounce/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/82a8c1857c790563bd8e518ed775956006f68485 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/cheggaaa/pb/v3/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/f6beca1e369881c362566f026ea1ae521a02c98a || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/containerd/stargz-snapshotter/estargz/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/docker/cli/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/878e7d86573d6c8ff65d2eaab294734b3f4d3d81 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/docker/cli/NOTICE %{buildroot}/usr/share/package-licenses/faas-cli/5476f2f91673ef040f1956907e7f45e72d5e11ee || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/docker/distribution/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/c700a8b9312d24bdc57570f7d6a131cf63d89016 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/docker/docker-credential-helpers/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/f3eab54cb1736b419ef75b8c44bea2b17614bd31 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/20b06a68cf65738d43afa04acce0126f341c77f8 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/docker/docker/NOTICE %{buildroot}/usr/share/package-licenses/faas-cli/5476f2f91673ef040f1956907e7f45e72d5e11ee || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/drone/envsubst/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/572256a27f3a290c6c908d8259769ee9793f287e || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/fatih/color/LICENSE.md %{buildroot}/usr/share/package-licenses/faas-cli/563519fec7769aaec054ee06cb429f39f0fdab89 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/fsnotify/fsnotify/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/135191231608cd88684768718b8a2f439c9e1817 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/go-git/gcfg/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/go-git/go-billy/v5/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/252aed5d0042e1b207cfa34525444999cdb54e3e || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/go-git/go-git/v5/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/12652bf1fa2266f5ad64804acea3a78ab66699a2 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/7080652cc78cd9855d39e324529a3b5f3745dcd6 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/google/go-containerregistry/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/1128f8f91104ba9ef98d37eea6523a888dcfa5de || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/62446e71c226403f1a2e67d0f66ede03e3fbdd2f || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/jbenet/go-context/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/e5e9e009a3997eb17fba187559a605766efeb0ed || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/klauspost/compress/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/0e8f2042647b8140e79c4eb7d233d1b39231db09 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/klauspost/compress/internal/snapref/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/b7b97d84a5f0b778ab971d2afce44f47c8b6e80a || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/klauspost/compress/zstd/internal/xxhash/LICENSE.txt %{buildroot}/usr/share/package-licenses/faas-cli/7be82c1a81e7197640a88df91dc82d64b77c7acd || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/mattn/go-colorable/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/5ca808f075931c5322193d4afd5a3370c824f810 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/mattn/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/5b53018d7f0706e49275a92d36b54cfbfbb71367 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/mattn/go-runewidth/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/5ca808f075931c5322193d4afd5a3370c824f810 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/mitchellh/go-homedir/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/5ad2002bc8d2b22e2034867d159f71ba6258e18f || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/mitchellh/go-wordwrap/LICENSE.md %{buildroot}/usr/share/package-licenses/faas-cli/d676a57141ac47c27699fc8b03e1a2e59abb96ef || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/moby/term/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/20b06a68cf65738d43afa04acce0126f341c77f8 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/morikuni/aec/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/3faf341fbc32621fe1ac089ae2ab7a23980fc189 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/olekukonko/tablewriter/LICENSE.md %{buildroot}/usr/share/package-licenses/faas-cli/7c15369a8295c6d2cd26b41618f5ba81e7e06eca || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/opencontainers/go-digest/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/93ac97c9679b68518f1fd7de627ce2f77f44082d || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/opencontainers/go-digest/LICENSE.docs %{buildroot}/usr/share/package-licenses/faas-cli/979fd7d5c67073b265d96f584aac3de1c419b8e2 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/opencontainers/image-spec/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/298850a6cdb155f54cfa44641df70b36228ed031 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/openfaas/faas-provider/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/f1ae47fecc13bcdc9beb6dc74be71d0fd4e34bbd || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/openfaas/faas/gateway/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/fc3fc032d02290b035bbf80a8a085da61cf75c3f || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/openfaas/go-sdk/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/3abe2ed84bfc0af4a31be3c2cac403105beb0ce0 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/rivo/uniseg/LICENSE.txt %{buildroot}/usr/share/package-licenses/faas-cli/f60d047cd34de4c91b3a045ebf117fe54b3c279e || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/ryanuber/go-glob/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/f25ad3680192d554da0315f90fa71f63278a5326 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/a1c7852c717fed2c9a0284ed112ea66013230da6 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/faas-cli/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/b3c86ae465b21f7323059db335158b48187731c7 || :
cp %{_builddir}/faas-cli-%{version}/vendor/github.com/vbatts/tar-split/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/40759db9edbb7fe30b64cc213f4f20c4618e2932 || :
cp %{_builddir}/faas-cli-%{version}/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/faas-cli-%{version}/vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/faas-cli-%{version}/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/faas-cli-%{version}/vendor/gopkg.in/warnings.v0/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/318dc4af5ea975b426db65053b4f16ca91341d15 || :
cp %{_builddir}/faas-cli-%{version}/vendor/gopkg.in/yaml.v3/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/b74b3b31bc15ad5e94fc1947d682aa3d84132fce || :
cp %{_builddir}/faas-cli-%{version}/vendor/gopkg.in/yaml.v3/NOTICE %{buildroot}/usr/share/package-licenses/faas-cli/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785 || :
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
/usr/share/package-licenses/faas-cli/020acfcf6d6bd6d701d19bd16f49d0bf18441779
/usr/share/package-licenses/faas-cli/0e8f2042647b8140e79c4eb7d233d1b39231db09
/usr/share/package-licenses/faas-cli/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/faas-cli/12652bf1fa2266f5ad64804acea3a78ab66699a2
/usr/share/package-licenses/faas-cli/135191231608cd88684768718b8a2f439c9e1817
/usr/share/package-licenses/faas-cli/20b06a68cf65738d43afa04acce0126f341c77f8
/usr/share/package-licenses/faas-cli/252aed5d0042e1b207cfa34525444999cdb54e3e
/usr/share/package-licenses/faas-cli/298850a6cdb155f54cfa44641df70b36228ed031
/usr/share/package-licenses/faas-cli/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/faas-cli/318dc4af5ea975b426db65053b4f16ca91341d15
/usr/share/package-licenses/faas-cli/3abe2ed84bfc0af4a31be3c2cac403105beb0ce0
/usr/share/package-licenses/faas-cli/3dbdeb041ef56b91e6c094423ab0c23b1dba025f
/usr/share/package-licenses/faas-cli/3faf341fbc32621fe1ac089ae2ab7a23980fc189
/usr/share/package-licenses/faas-cli/40759db9edbb7fe30b64cc213f4f20c4618e2932
/usr/share/package-licenses/faas-cli/5476f2f91673ef040f1956907e7f45e72d5e11ee
/usr/share/package-licenses/faas-cli/563519fec7769aaec054ee06cb429f39f0fdab89
/usr/share/package-licenses/faas-cli/572256a27f3a290c6c908d8259769ee9793f287e
/usr/share/package-licenses/faas-cli/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b
/usr/share/package-licenses/faas-cli/5ad2002bc8d2b22e2034867d159f71ba6258e18f
/usr/share/package-licenses/faas-cli/5b53018d7f0706e49275a92d36b54cfbfbb71367
/usr/share/package-licenses/faas-cli/5ca808f075931c5322193d4afd5a3370c824f810
/usr/share/package-licenses/faas-cli/5fcf3d8a80be9b86a2c442ab938090611e6ee317
/usr/share/package-licenses/faas-cli/62446e71c226403f1a2e67d0f66ede03e3fbdd2f
/usr/share/package-licenses/faas-cli/7080652cc78cd9855d39e324529a3b5f3745dcd6
/usr/share/package-licenses/faas-cli/7be82c1a81e7197640a88df91dc82d64b77c7acd
/usr/share/package-licenses/faas-cli/7c15369a8295c6d2cd26b41618f5ba81e7e06eca
/usr/share/package-licenses/faas-cli/82a8c1857c790563bd8e518ed775956006f68485
/usr/share/package-licenses/faas-cli/836ef1b46953afdb78ce3929bc6831ca83620b65
/usr/share/package-licenses/faas-cli/878e7d86573d6c8ff65d2eaab294734b3f4d3d81
/usr/share/package-licenses/faas-cli/93ac97c9679b68518f1fd7de627ce2f77f44082d
/usr/share/package-licenses/faas-cli/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/faas-cli/95dc7028a6518eb427e543f891c774df3b24b0cf
/usr/share/package-licenses/faas-cli/979fd7d5c67073b265d96f584aac3de1c419b8e2
/usr/share/package-licenses/faas-cli/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/faas-cli/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/faas-cli/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/faas-cli/b74b3b31bc15ad5e94fc1947d682aa3d84132fce
/usr/share/package-licenses/faas-cli/b7b97d84a5f0b778ab971d2afce44f47c8b6e80a
/usr/share/package-licenses/faas-cli/c700a8b9312d24bdc57570f7d6a131cf63d89016
/usr/share/package-licenses/faas-cli/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
/usr/share/package-licenses/faas-cli/ce62120d32a64c44b0e61ee13b9b5fd2c0cea2a1
/usr/share/package-licenses/faas-cli/d676a57141ac47c27699fc8b03e1a2e59abb96ef
/usr/share/package-licenses/faas-cli/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/faas-cli/e5e9e009a3997eb17fba187559a605766efeb0ed
/usr/share/package-licenses/faas-cli/f1ae47fecc13bcdc9beb6dc74be71d0fd4e34bbd
/usr/share/package-licenses/faas-cli/f25ad3680192d554da0315f90fa71f63278a5326
/usr/share/package-licenses/faas-cli/f3eab54cb1736b419ef75b8c44bea2b17614bd31
/usr/share/package-licenses/faas-cli/f60d047cd34de4c91b3a045ebf117fe54b3c279e
/usr/share/package-licenses/faas-cli/f6beca1e369881c362566f026ea1ae521a02c98a
/usr/share/package-licenses/faas-cli/fc3fc032d02290b035bbf80a8a085da61cf75c3f
