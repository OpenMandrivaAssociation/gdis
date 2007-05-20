%define name 	gdis
%define version 0.89
%define release %mkrel 1

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
Requires: 	povray ImageMagick openbabel grace

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

# menu
install -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="gdis"\
needs="x11"\
section="More Applications/Sciences/Chemistry"\
title="Gdis"\
icon="chemistry_section.png"\
longtitle="Molecule/crystal viewer"\
xdg="true"
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{name} 
Icon=chemistry_section.png
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Sciences-Chemistry;Science;Chemistry;
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root,0755)
%doc README CHANGELOG TODO
%_bindir/*
%_menudir/%name
%_datadir/applications/*

