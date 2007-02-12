Summary:	bh-75dpi font
Summary(pl.UTF-8):	Font bh-75dpi
Name:		xorg-font-font-bh-75dpi
Version:	1.0.0
Release:	0.1
License:	distributable (see COPYING)
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/font/font-bh-75dpi-%{version}.tar.bz2
# Source0-md5:	6e51cd02f4ce32e1393e34ab17a9b211
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 0.99.2
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bh-75dpi font.

%description -l pl.UTF-8
Font bh-75dpi.

%prep
%setup -q -n font-bh-75dpi-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/75dpi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst 75dpi

%postun
fontpostinst 75dpi

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/75dpi/*.pcf.gz
