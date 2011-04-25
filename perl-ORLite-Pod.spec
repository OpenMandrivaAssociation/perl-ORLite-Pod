%define upstream_name    ORLite-Pod
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Documentation generator for ORLite
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/ORLite/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Inspector)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Remove)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::pushd)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(ORLite)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Template)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Script)
BuildRequires: perl(Test::XT)
BuildRequires: perl(autodie) >= 2.100.0

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
*THIS MODULE IS EXPERIMENTAL AND SUBJECT TO CHANGE WITHOUT NOTICE.*

*YOU HAVE BEEN WARNED!*

The biggest downside of the ORLite manpage is that because it can generate
you an entire ORM in one line of code, you can have a large an extensive
API without anywhere for documentation for the API to exist.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_bindir}/*
%{_mandir}/man?/*
%perl_vendorlib/*
