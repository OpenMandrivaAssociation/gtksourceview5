%define url_ver %(echo %{version}|cut -d. -f1,2)

%define oname	gtksourceview
%define api	5
%define major	0
%define libname	%mklibname %{oname}- %{api} %{major}
%define girname	%mklibname %{oname}-gir %{api}
%define devname %mklibname -d %{oname}- %{api}

%define _disable_rebuild_configure 1

Summary:	Source code viewing library
Name:		gtksourceview5
Version: 	5.13.1
Release:	1
License:	GPLv2+
Group:		Editors
Url:		https://gtksourceview.sourceforge.net/
Source0:	https://download.gnome.org/sources/gtksourceview/%{url_ver}/%{oname}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gio-2.0) >= 2.28.0
BuildRequires:	pkgconfig(vapigen)

%description
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{libname}
Summary:	Source code viewing library
Group:		Editors
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Libraries and include files for GtkSourceView
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{oname}-%{api}-devel = %{version}-%{release}

%description -n %{devname}
GtkSourceView development files 

%prep
%setup -qn %{oname}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%{find_lang} %{oname}-%{api}

%files -f %{oname}-%{api}.lang
%doc AUTHORS NEWS README.md
%{_datadir}/gtksourceview-%{api}
%{_iconsdir}/hicolor/scalable/actions/completion*
%{_iconsdir}/hicolor/scalable/actions/lang*

%files -n %{libname} 
%{_libdir}/libgtksourceview-%{api}.so.%{major}*

%files -n %{girname} 
%{_libdir}/girepository-1.0/GtkSource-%{api}.typelib

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/GtkSource-%{api}.gir
%{_datadir}/vala/vapi/gtksourceview-%{api}.deps
%{_datadir}/vala/vapi/gtksourceview-%{api}.vapi
