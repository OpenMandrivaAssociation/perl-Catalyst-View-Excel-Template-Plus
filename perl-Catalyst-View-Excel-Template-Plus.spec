%define upstream_name    Catalyst-View-Excel-Template-Plus
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Excel::Plus View
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/stevan/catalyst-view-excel-template-plus
Source0:	https://cpan.metacpan.org/authors/id/S/ST/STEVAN/Catalyst-View-Excel-Template-Plus-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Excel::Template::Plus)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(MooseX::Param)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(parent)
BuildArch:	noarch

%description
This is a Catalyst View subclass which can handle rendering excel content
through Excel::Template::Plus.

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
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

