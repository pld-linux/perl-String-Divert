#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Divert
Summary:	String::Divert - string object supporting folding and diversions
Summary(pl):	String::Divert - obiekt ³añcucha obs³uguj±cy zwijanie i przekierowania
Name:		perl-String-Divert
Version:	0.93
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af85944c53c39ce3585a100a91a4bbda
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

%description -l pl
String::Divert to ma³y modu³ Perla 5 udostêpniaj±cy podobny do skalara
obiekt ³añcucha z paroma przeci±¿onymi operatorami, obs³uguj±cy ideê
"zwijania" i "przekierowywania". Pozwala to na zagnie¿d¿one
generowanie strukturalnego wyj¶cia. Idea polega na wy³±czeniu
sekwencyjnego generowania wyj¶cia z zagnie¿d¿onej, niesekwencyjnej
struktury wyj¶cia.

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
