Summary:	Remote SMTP Server Detection
Name:		smtpscan
Version:	0.5
Release:	%mkrel 3
License:	GPL
Group:		Monitoring
URL:		http://www.greyhats.org/outils/smtpscan/
Source0:	%{name}-%{version}.tar.bz2
Source1:	remote_smtp_detect.pdf.bz2
Patch0:		smtpscan-0.4.patch
Requires:	perl perl-Net-DNS
BuildArch:	noarch

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_datadir}/smtpscan

install -m755 src/smtpscan %{buildroot}%{_bindir}/
install -m644 docs/man/smtpscan.1 %{buildroot}%{_mandir}/man1/
install -m644 src/fingerprints  %{buildroot}%{_datadir}/smtpscan/
install -m644 src/tests %{buildroot}%{_datadir}/smtpscan/

bzcat %{SOURCE1} > remote_smtp_detect.pdf

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc CHANGELOG CONTRIBUTORS remote_smtp_detect.pdf
%{_bindir}/smtpscan
%{_datadir}/smtpscan
%{_mandir}/man1/*

