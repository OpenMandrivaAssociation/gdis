%define name 	gdis
%define version 0.89
%define release %mkrel 4

Summary: 	A molecular and crystal model viewer 
Name: 		%name
Version: 	%version
Release: 	%release
License: 	GPL
Group: 		Sciences/Chemistry
URL: 		http://gdis.sourceforge.net/
Source: 	%name-%version-source.tar.bz2
Source2:	%name-models.tar.bz2
BuildRoot: 	%_tmppath/%name-root
BuildRequires: 	mesaglu-devel libmesaglut-devel gtk2-devel gtkglext-devel
Requires: 	povray imagemagick openbabel grace

%description
gdis is a graphical program for displaying and manipulating 
molecular and crystal systems.

%prep
%setup -q -a 2
mv gdis/models .
rm -fr gdis
rm -fr models/CVS

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
make INSTALL=$RPM_BUILD_ROOT/%_bindir install

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=A molecular and crystal model viewer
Exec=%{name} 
Icon=chemistry_section
Terminal=false
Type=Application
Categories=Science;Chemistry;
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root,0755)
%doc README CHANGELOG TODO
%_bindir/*
%_datadir/applications/*
