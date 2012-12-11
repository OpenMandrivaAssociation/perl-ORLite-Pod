%define upstream_name    ORLite-Pod
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Documentation generator for ORLite
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/ORLite/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Remove)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::pushd)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(ORLite)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Template)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Script)
BuildRequires:	perl(Test::XT)
BuildRequires:	perl(autodie) >= 2.100.0

BuildArch:	noarch

%description
*THIS MODULE IS EXPERIMENTAL AND SUBJECT TO CHANGE WITHOUT NOTICE.*

*YOU HAVE BEEN WARNED!*

The biggest downside of the ORLite manpage is that because it can generate
you an entire ORM in one line of code, you can have a large an extensive
API without anywhere for documentation for the API to exist.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_bindir}/*
%{_mandir}/man?/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 658934
- update file list
- rebuild for updated spec-helper

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 554109
- adding missing buildrequires:
- update to 0.10

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 491768
- import perl-ORLite-Pod


* Fri Jan 15 2010 cpan2dist 0.06-1mdv
- initial mdv release, generated with cpan2dist
