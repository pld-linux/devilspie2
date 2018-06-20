Summary:	Devilspie2 - perform scripted actions on windows as they are created
Name:		devilspie2
Version:	0.43
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://download.savannah.nongnu.org/releases/devilspie2/%{name}_%{version}-src.tar.gz
# Source0-md5:	26eed0b5b4af5c7e13c551eceaeab832
URL:		http://www.nongnu.org/devilspie2/
BuildRequires:	glib2-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libwnck-devel
BuildRequires:	lua51-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devilspie2 is a program that detects windows as they are created, and
performs scripted actions on them. The scripts are written in Lua,
allowing a great deal of customisation.

%prep
%setup -q

sed -i -e's,/usr/share/doc/devilspie2,%{_docdir}/%{name}-%{version},' devilspie2.1

%build
%{__make} \
	PREFIX="%{_prefix}" \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX="%{_prefix}" \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README* TODO
%attr(755,root,root) %{_bindir}/devilspie2
%{_mandir}/man1/devilspie2.1*
