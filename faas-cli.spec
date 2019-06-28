#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : faas-cli
Version  : 0.8.19
Release  : 9
URL      : https://github.com/openfaas/faas-cli/archive/0.8.19/faas-cli-0.8.19.tar.gz
Source0  : https://github.com/openfaas/faas-cli/archive/0.8.19/faas-cli-0.8.19.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause GPL-2.0 MIT
Requires: faas-cli-bin = %{version}-%{release}
Requires: faas-cli-license = %{version}-%{release}
Requires: requests
BuildRequires : buildreq-golang
BuildRequires : requests

%description
## faas-cli
[![Go Report Card](https://goreportcard.com/badge/github.com/openfaas/faas-cli)](https://goreportcard.com/report/github.com/openfaas/faas-cli) [![Build Status](https://travis-ci.org/openfaas/faas-cli.svg?branch=master)](https://travis-ci.org/openfaas/faas-cli)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenFaaS](https://img.shields.io/badge/openfaas-serverless-blue.svg)](https://www.openfaas.com)

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
%setup -q -n faas-cli-0.8.19

%build
## build_prepend content
export GOPATH=/go
mkdir -p /go/src/github.com/openfaas/
ln -s /builddir/build/BUILD/faas-cli-%{version} /go/src/github.com/openfaas/faas-cli
cd /go/src/github.com/openfaas/faas-cli
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
go build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/faas-cli
cp LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/LICENSE
cp vendor/github.com/Azure/go-ansiterm/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_Azure_go-ansiterm_LICENSE
cp vendor/github.com/Sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_Sirupsen_logrus_LICENSE
cp vendor/github.com/docker/docker-credential-helpers/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker-credential-helpers_LICENSE
cp vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_LICENSE
cp vendor/github.com/docker/docker/NOTICE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_NOTICE
cp vendor/github.com/docker/docker/contrib/selinux-fedora-24/docker-engine-selinux/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_contrib_selinux-fedora-24_docker-engine-selinux_LICENSE
cp vendor/github.com/docker/docker/contrib/selinux-oraclelinux-7/docker-engine-selinux/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_contrib_selinux-oraclelinux-7_docker-engine-selinux_LICENSE
cp vendor/github.com/docker/docker/contrib/selinux/docker-engine-selinux/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_contrib_selinux_docker-engine-selinux_LICENSE
cp vendor/github.com/docker/docker/contrib/syntax/vim/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_contrib_syntax_vim_LICENSE
cp vendor/github.com/docker/docker/pkg/symlink/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_pkg_symlink_LICENSE.APACHE
cp vendor/github.com/docker/docker/pkg/symlink/LICENSE.BSD %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_pkg_symlink_LICENSE.BSD
cp vendor/github.com/drone/envsubst/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_drone_envsubst_LICENSE
cp vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_inconshreveable_mousetrap_LICENSE
cp vendor/github.com/mitchellh/go-homedir/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_mitchellh_go-homedir_LICENSE
cp vendor/github.com/morikuni/aec/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_morikuni_aec_LICENSE
cp vendor/github.com/openfaas/faas/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_openfaas_faas_LICENSE
cp vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_pkg_errors_LICENSE
cp vendor/github.com/ryanuber/go-glob/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_ryanuber_go-glob_LICENSE
cp vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_spf13_cobra_LICENSE.txt
cp vendor/github.com/spf13/cobra/cobra/cmd/testdata/LICENSE.golden %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_spf13_cobra_cobra_cmd_testdata_LICENSE.golden
cp vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_github.com_spf13_pflag_LICENSE
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_golang.org_x_sys_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/faas-cli/vendor_gopkg.in_yaml.v2_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/faas-cli/vendor_gopkg.in_yaml.v2_LICENSE.libyaml

## install_append content
install -d %{buildroot}/usr/bin
install -p -m 755 /go/src/github.com/openfaas/faas-cli/faas-cli %{buildroot}/usr/bin/faas-cli
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/faas-cli

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/faas-cli/LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_Azure_go-ansiterm_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_Sirupsen_logrus_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker-credential-helpers_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_NOTICE
/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_contrib_selinux-fedora-24_docker-engine-selinux_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_contrib_selinux-oraclelinux-7_docker-engine-selinux_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_contrib_selinux_docker-engine-selinux_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_contrib_syntax_vim_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_pkg_symlink_LICENSE.APACHE
/usr/share/package-licenses/faas-cli/vendor_github.com_docker_docker_pkg_symlink_LICENSE.BSD
/usr/share/package-licenses/faas-cli/vendor_github.com_drone_envsubst_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_inconshreveable_mousetrap_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_mitchellh_go-homedir_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_morikuni_aec_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_openfaas_faas_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_pkg_errors_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_ryanuber_go-glob_LICENSE
/usr/share/package-licenses/faas-cli/vendor_github.com_spf13_cobra_LICENSE.txt
/usr/share/package-licenses/faas-cli/vendor_github.com_spf13_cobra_cobra_cmd_testdata_LICENSE.golden
/usr/share/package-licenses/faas-cli/vendor_github.com_spf13_pflag_LICENSE
/usr/share/package-licenses/faas-cli/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/faas-cli/vendor_golang.org_x_sys_LICENSE
/usr/share/package-licenses/faas-cli/vendor_gopkg.in_yaml.v2_LICENSE
/usr/share/package-licenses/faas-cli/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
