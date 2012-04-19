Name:		qpass
Summary:	Qt4-based password manager
Version:	1.2.1
Release:	1
License:	GPLv2+
Group:		Databases
URL:		http://qpass.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/qpass/source/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	libgcrypt-devel

%description
QPass is easy to use, open source password manager application with built-in
password generator. You can store in it's database such data as passwords
and logins which will be encrypted using AES-256 algorithm. Each entry can
include additional information about entry such as name, url adress
and description.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build
%__rm -f %{buildroot}/%{_datadir}/%{name}/{COPYING,README}
%__mkdir_p  %{buildroot}/%{_docdir}
%if %{mdvver} >= 201200
%find_lang %{name} --with-qt --all-name
%else
touch %{name}.lang
%endif

%files -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_bindir}/qpass
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/qpass.png
%{_datadir}/pixmaps/qpass.png
%doc ChangeLog README
%if %mdvver < 201200
%{_datadir}/%{name}/translations/*
%endif
