%define real_name Sphinx-Search

Summary:	Sphinx search engine API Perl client
Name:		perl-%{real_name}
Version:	0.14
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JJ/JJSCHUTZ/%{real_name}-%{version}.tar.gz
BuildRequires:	perl-devel
#BuildRequires:	perl-Test-Pod-Coverage
#BuildRequires:	perl-File-SearchPath
#BuildRequires:	perl-Path-Class
#BuildRequires:	sphinx
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Sphinx search engine API Perl client for Sphinx 0.9.8-svn-r871 and later.

%prep

%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

#%%check
#make \
#    SPHINX_SEARCHD="%{_sbindir}/sphinx-searchd" \
#    SPHINX_INDEXER="%{_bindir}/sphinx-indexer" \
#    SPHINX_PORT="20000" \
#    test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Sphinx/Search.pm
%attr(0644,root,root) %{_mandir}/man3/Sphinx::Search.3pm*

