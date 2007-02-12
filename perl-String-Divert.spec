#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	Divert
Summary:	String::Divert - string object supporting folding and diversions
Summary(pl.UTF-8):   String::Divert - obiekt łańcucha obsługujący zwijanie i przekierowania
Name:		perl-String-Divert
Version:	0.96
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c574d757af76d55819d18654d1603b48
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::Divert is small Perl 5 module providing a scalar-like string
object with some overloaded operators, supporting the concept of
"Folding" and "Diversion". This allows nested generation of structured
output. The idea is to decouple the sequential generation of output from
the nested and non-sequential structure of the output.

%description -l pl.UTF-8
String::Divert to mały moduł Perla 5 udostępniający podobny do skalara
obiekt łańcucha z paroma przeciążonymi operatorami, obsługujący ideę
"zwijania" i "przekierowywania". Pozwala to na zagnieżdżone
generowanie strukturalnego wyjścia. Idea polega na wyłączeniu
sekwencyjnego generowania wyjścia z zagnieżdżonej, niesekwencyjnej
struktury wyjścia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{perl_vendorlib}/String/Divert.pm
%{_mandir}/man3/*
