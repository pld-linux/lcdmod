Summary:	LCDmod displays anything on a 20x4 backlit LCD
Summary(pl):	LCDmod wy¶wietla wszystko na wy¶wietlaczu LCD 20x4
Name:		lcdmod
Version:	1.0.2
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/lcdmod/%{name}-%{version}.tgz
# Source0-md5:	762bf7c60841ecf0d41d5479f29cceda
Patch0:		%{name}-kernel_version.patch
URL:		http://lcd-mod.sf.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is kernel module for HD44780-based LCDs.

%description -l pl
To jest modu³ kernela dla LCD opartych na HD44780.

%prep
%setup -q
%patch0 -p0

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_sysconfdir}/lcd-mod}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* INSTALL TODO ChangeLog
