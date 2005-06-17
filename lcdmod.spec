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
URL:		http://lcd-mod.sourceforge.net/
%{?with_dist_kernel:BuildRequires:	kernel24-headers}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is kernel module for HD44780-based LCDs, it was written because
there was no nice way of controlling these displays from a computer
under Linux, most other software written to control these displays run
in user space, and/or don't support all the features of the displays.
Lcdmod allows users to easily intergrate the LCD, in its simplest
form, into shell scripts, C code, et cetera by simply writing ASCII to
the device file.

%description -l pl
To jest modu³ j±dra dla LCD opartych na HD44780, zosta³ napisany
poniewa¿ nie by³o ¿adnej przyjemnej metody kontrolowania tych
wy¶wielaczy pod Linuksem, wiêkszo¶æ innego oprogramowania steruj±cego
tymi wy¶wielaczami pracowa³a w przestrzeni urzytkownika i/lub nie
wspiera³a wszystkich cech wy¶wietlaczy. Lcdmod pozwala u¿ytkownikom na
³atw± integracjê LCD, w najprostszy mo¿liwy sposób do skryptów pow³oki
czy programów w C poprzez wysy³anie kodów ASCII do pliku urz±dzenia.

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
