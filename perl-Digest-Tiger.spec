#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	Tiger
Summary:	Digest::Tiger - Tiger hash implementation
Summary(pl):	Digest::Tiger - implementacja skr�tu Tiger
Name:		perl-Digest-Tiger
Version:	0.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f72ea5b048b87300f5c906ecc3fb436e
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digest::Tiger Perl module implements the Tiger hash, which returns a
192-bit hash value.

%description -l pl
Modu� Perla Digest::Tiger jest implementacj� funkcji mieszaj�cej
Tiger, zwracaj�cej warto�� 192-bitow�.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

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
