%define upstream_name    Sphinx-Search
%define upstream_version 0.28
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.28
Release:	3

Summary:	Sphinx search engine API Perl client
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JJ/JJSCHUTZ/Sphinx-Search-0.28.tar.gz

#BuildRequires:	perl-Test-Pod-Coverage
#BuildRequires:	perl-File-SearchPath
#BuildRequires:	perl-Path-Class
#BuildRequires:	sphinx
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Sphinx search engine API Perl client for Sphinx 0.9.8-svn-r871 and later.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Sat Dec 18 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.240.1-1mdv2011.0
+ Revision: 622890
- update to new version 0.240.1

* Wed Dec 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 616217
- update to new version 0.24

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.0
+ Revision: 404394
- rebuild using %%perl_convert_version

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2010.0
+ Revision: 373793
- update to new version 0.22

* Tue May 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2010.0
+ Revision: 372161
- update to new version 0.21

* Sun May 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2010.0
+ Revision: 371336
- update to new version 0.20

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2010.0
+ Revision: 370177
- update to new version 0.19

* Sat Feb 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2009.1
+ Revision: 345922
- update to new version 0.15

* Mon Feb 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2009.1
+ Revision: 338674
- update to new version 0.14

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2009.0
+ Revision: 270396
- update to new version 0.12

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.11-2mdv2009.0
+ Revision: 268725
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
+ Revision: 194861
- update to new version 0.11
- update to new version 0.11

* Thu Jan 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.1
+ Revision: 160755
- update to new version 0.10

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2008.1
+ Revision: 119230
- update to new version 0.09

* Mon Nov 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2008.1
+ Revision: 112680
- update to new version 0.08
- update to new version 0.08

* Thu Nov 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.07-1mdv2008.1
+ Revision: 104414
- import perl-Sphinx-Search


* Thu Nov 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.07-1mdv2008.1
- initial Mandriva package 

