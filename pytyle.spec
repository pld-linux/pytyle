Summary:	Manual tiling manager
Summary(pl.UTF-8):	Manualny manadżer kafelkowania
Name:		pytyle
Version:	0.7.5
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/pytyle/%{name}-%{version}.tar.gz
# Source0-md5:	0475a2f98732ef724423f3c19ecfa52e
URL:		http://pytyle.com/
BuildRequires:	python-Xlib
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-Xlib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyTyle is a manual tiling manager that can slide into any EWMH
compliant window manager. It will allow you to enable/disable tiling
on a per screen per workspace basis, and continually tile your
windows.

%description -l pl.UTF-8
PyTyle jest manualnym manadżerem kafelkowania, który współpracuje
z manadżerami okien zgodnymi z EWMH. Umożliwia włączanie/wyłączanie
kafelkowania na ekranie przestrzeni roboczej oraz ciągłe kafelkowanie
okien.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/pytyle
%attr(755,root,root) %{_bindir}/pytyle-client
%dir %{py_sitescriptdir}/PyTyle
%{py_sitescriptdir}/PyTyle/*.py[co]
%{py_sitescriptdir}/PyTyle/pytylerc
%dir %{py_sitescriptdir}/PyTyle/Tilers
%{py_sitescriptdir}/PyTyle/Tilers/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pytyle-*.egg-info
%endif
