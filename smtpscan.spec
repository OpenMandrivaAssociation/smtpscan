Summary:	Remote SMTP Server Detection
Name:		smtpscan
Version:	0.5
Release:	%mkrel 5
License:	GPL
Group:		Monitoring
URL:		http://www.greyhats.org/outils/smtpscan/
Source0:	%{name}-%{version}.tar.bz2
Source1:	remote_smtp_detect.pdf.bz2
Patch0:		smtpscan-0.4.patch
Requires:	perl perl-Net-DNS
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Smtpscan is a tool to guess which MTA is used by sending several
"special" SMTP requests and by comparing error codes returned with
those in the fingerprint database. It does not take into account
banners and other text information, that cannot be trusted, only
error codes.

%prep

%setup -q -n %{name} 
%patch0 -p1

%build

%install
rm -rf %{buildroot} 

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_datadir}/smtpscan

install -m755 src/smtpscan %{buildroot}%{_bindir}/
install -m644 docs/man/smtpscan.1 %{buildroot}%{_mandir}/man1/
install -m644 src/fingerprints  %{buildroot}%{_datadir}/smtpscan/
install -m644 src/tests %{buildroot}%{_datadir}/smtpscan/

bzcat %{SOURCE1} > remote_smtp_detect.pdf

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc CHANGELOG CONTRIBUTORS remote_smtp_detect.pdf
%{_bindir}/smtpscan
%{_datadir}/smtpscan
%{_mandir}/man1/*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.5-5mdv2010.0
+ Revision: 433968
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5-4mdv2009.0
+ Revision: 239033
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jul 14 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5-3mdv2007.0
- rebuild

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5-2mdk
- rebuild

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.5-1mdk
- 0.5

