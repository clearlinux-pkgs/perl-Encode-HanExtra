#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Encode-HanExtra
Version  : 0.23
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/Encode-HanExtra-0.23.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/Encode-HanExtra-0.23.tar.gz
Summary  : Extra sets of Chinese encodings
Group    : Development/Tools
License  : MIT
Requires: perl-Encode-HanExtra-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)

%description
NAME
Encode::HanExtra - Extra sets of Chinese encodings
VERSION
This document describes version 0.23 of Encode::HanExtra, released
November 10, 2007.

%package dev
Summary: dev components for the perl-Encode-HanExtra package.
Group: Development
Provides: perl-Encode-HanExtra-devel = %{version}-%{release}
Requires: perl-Encode-HanExtra = %{version}-%{release}

%description dev
dev components for the perl-Encode-HanExtra package.


%package perl
Summary: perl components for the perl-Encode-HanExtra package.
Group: Default
Requires: perl-Encode-HanExtra = %{version}-%{release}

%description perl
perl components for the perl-Encode-HanExtra package.


%prep
%setup -q -n Encode-HanExtra-0.23
cd %{_builddir}/Encode-HanExtra-0.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Encode::HanExtra.3
/usr/share/man/man3/Encode::TW::Unisys::SOSI1.3
/usr/share/man/man3/Encode::TW::Unisys::SOSI2.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
