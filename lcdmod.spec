# TODO:
# - build kernel-* subpackages for UP/SMP modules
#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
#
Summary:	LCDmod - display anything on a up to 40x4 chars backlit LCD
Summary(pl):	LCDmod - wy¶wietlanie czegokolwiek na wy¶wietlaczu LCD do 40x4 znaków
Name:		lcdmod
Version:	1.0.2
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://lcd-mod.sourceforge.net/dist/%{name}-%{version}.tgz
# Source0-md5:	762bf7c60841ecf0d41d5479f29cceda
Patch0:		%{name}-kernel_version.patch
URL:		http://lcd-mod.sf.net/
%{?with_dist_kernel:BuildRequires:	kernel24-headers}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is kernel module for HD44780-based LCDs.

%description -l pl
To jest modu³ j±dra dla LCD opartych na HD44780.

%prep
%setup -q
%patch0 -p0

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/kernel/misc

install lcd.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/kernel/misc

%clean
rm -rf $RPM_BUILD_ROOT

%post
%depmod %{_kernel_ver}

%postun
%depmod %{_kernel_ver}

%files
%defattr(644,root,root,755)
%doc README* INSTALL TODO ChangeLog
/lib/modules/%{_kernel_ver}/kernel/misc/lcd.o*
