%define upstream_name    Sphinx-Search
%define upstream_version 0.31
Name:		perl-%{upstream_name}
Version:	0.31
Release:	2

Summary:	Sphinx search engine API Perl client
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Sphinx-Search
Source0:	https://cpan.metacpan.org/authors/id/J/JJ/JJSCHUTZ/Sphinx-Search-0.31.tar.gz

#BuildRequires:	perl-Test-Pod-Coverage
#BuildRequires:	perl-File-SearchPath
#BuildRequires:	perl-Path-Class
#BuildRequires:	sphinx
BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Sphinx search engine API Perl client for Sphinx 0.9.8-svn-r871 and later.

%prep
%setup -q -n Sphinx-Search-0.31

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

#%%check
#make \
#    SPHINX_SEARCHD="%{_sbindir}/sphinx-searchd" \
#    SPHINX_INDEXER="%{_bindir}/sphinx-indexer" \
#    SPHINX_PORT="20000" \
#    test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Sphinx/Search.pm
%attr(0644,root,root) %{_mandir}/man3/Sphinx::Search.3pm*

