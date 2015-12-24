#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	Tiger
Summary:	Digest::Tiger - Tiger hash implementation
Summary(pl.UTF-8):	Digest::Tiger - implementacja skrótu Tiger
Name:		perl-Digest-Tiger
Version:	0.03
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Digest/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	30946a6d1b4451a34e142370c2947370
Patch0:		%{name}-amd64.patch
URL:		http://search.cpan.org/dist/Digest-Tiger/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digest::Tiger Perl module implements the Tiger hash, which returns a
192-bit hash value.

%description -l pl.UTF-8
Moduł Perla Digest::Tiger jest implementacją funkcji haszującej Tiger,
zwracającej 192-bitową wartość skrótu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/Tiger/Tiger.so
%{_mandir}/man3/*
