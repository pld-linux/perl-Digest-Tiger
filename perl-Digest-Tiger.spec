%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	Tiger
Summary:	Digest::Tiger Perl module - Tiger hash implementation
Summary(pl):	Modu³ perla Digest::Tiger - implementacja skrótu Tiger
Name:		perl-Digest-Tiger
Version:	0.02
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
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
%{perl_vendorarch}/Digest/Tiger.pm
%dir %{perl_vendorarch}/auto/Digest/Tiger
%{perl_vendorarch}/auto/Digest/Tiger/autosplit.ix
%{perl_vendorarch}/auto/Digest/Tiger/Tiger.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/Tiger/Tiger.so
%{_mandir}/man3/*
