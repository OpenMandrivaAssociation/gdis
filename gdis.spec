%define debug_package %{nil}

Summary: 	A molecular and crystal model viewer 
Name: 		gdis
Version: 	0.89
Release: 	7
License: 	GPL
Group: 		Sciences/Chemistry
URL: 		http://gdis.sourceforge.net/
Source: 	%name-%version-source.tar.bz2
Source2:	%name-models.tar.bz2
BuildRequires: 	mesaglu-devel pkgconfig(glut) gtk2-devel gtkglext-devel
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
export LDFLAGS="-lm"
%make CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}/%{_bindir}
make INSTALL=%{buildroot}/%{_bindir} install

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

%files
%defattr (-,root,root,0755)
%doc README CHANGELOG TODO
%_bindir/*
%_datadir/applications/*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.89-6mdv2011.0
+ Revision: 618445
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.89-5mdv2010.0
+ Revision: 429187
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.89-4mdv2009.0
+ Revision: 245824
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.89-2mdv2008.1
+ Revision: 140735
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - do not harcode icon extension

* Fri Aug 31 2007 Funda Wang <fwang@mandriva.org> 0.89-2mdv2008.0
+ Revision: 76735
- kill old menu & fix comment of xdg menu entry

* Sun May 20 2007 Adam Williamson <awilliamson@mandriva.org> 0.89-1mdv2008.0
+ Revision: 28767
- 0.89, update BuildRequires, fix povray dep (#26358)


* Thu Aug 10 2006 Lenny Cartier <lenny@mandriva.com> 0.86-2mdv2007.0
- xdg

* Thu Jul 21 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.86-1mdk
- 0.86

* Wed Feb 25 2004 Austin Acton <austin@mandrake.org> 0.81-2mdk
- fix locations
- please ignore the screwed up dates; I'm insane

* Wed Feb 25 2004 Austin Acton <austin@mandrake.org> 0.81-1mdk
- 0.81

* Mon Aug 25 2003 Austin Acton <aacton@yorku.ca> 0.77.4-1mdk
- 0.77.4

