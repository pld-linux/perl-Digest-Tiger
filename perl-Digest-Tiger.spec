%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	Tiger
Summary:	Digest::Tiger Perl module - Tiger hash implementation
Summary(pl):	Modu³ perla Digest::Tiger - implementacja skrótu Tiger
Name:		perl-Digest-Tiger
Version:	0.02
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the Tiger hash, which returns a 192-bit hash
value.

%description -l pl
Ten modu³ jest implementacj± funkcji mieszaj±cej Tiger, zwracaj±cej
warto¶æ 192-bitow±.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitearch}/Digest/Tiger.pm
%dir %{perl_sitearch}/auto/Digest/Tiger
%{perl_sitearch}/auto/Digest/Tiger/autosplit.ix
%{perl_sitearch}/auto/Digest/Tiger/Tiger.bs
%attr(755,root,root) %{perl_sitearch}/auto/Digest/Tiger/Tiger.so
%{_mandir}/man3/*
