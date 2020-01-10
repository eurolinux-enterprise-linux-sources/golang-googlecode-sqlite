%global debug_package   %{nil}
%global import_path     code.google.com/p/gosqlite
%global gopath          %{_datadir}/gocode
%global rev             74691fb6f83716190870cde1b658538dd4b18eb0
%global shortrev        %(r=%{rev}; echo ${r:0:12})

Name:           golang-googlecode-sqlite
Version:        0
Release:        0.9.hg%{shortrev}%{?dist}
Summary:        Trivial sqlite3 binding for Go
License:        BSD
URL:            http://%{import_path}
Source0:        https://gosqlite.googlecode.com/archive/%{rev}.zip
Source1:        LICENSE-BSD3-Go
%if 0%{?fedora} >= 19
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

This package has no exported API. It registers a driver for the standard Go
database/SQL package.

%package devel
Requires:       golang
Requires:       sqlite-devel
Summary:        Trivial sqlite3 binding for Go
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/sqlite) = %{version}-%{release}
Provides:       golang(%{import_path}/sqlite3) = %{version}-%{release}

%description devel
%{summary}

This package has no exported API. It registers a driver for the standard Go
database/SQL package.

%prep
%setup -n gosqlite-%{shortrev}

%build
# Requested upstream to include LICENSE
# http://code.google.com/p/gosqlite/issues/detail?id=21
cp %{SOURCE1} ./LICENSE

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
for d in sqlite sqlite3; do
   cp -av $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%files devel
%defattr(-,root,root,-)
%doc LICENSE
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/code.google.com
%dir %attr(755,root,root) %{gopath}/src/code.google.com/p
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/sqlite
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/sqlite3
%{gopath}/src/%{import_path}/sqlite/*.go
%{gopath}/src/%{import_path}/sqlite3/*.go

%changelog
* Sun Jan 19 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.9.hg74691fb6f837
- exclusivearch for el6+

* Thu Oct 17 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.8.hg74691fb6f837
- removed double quotes from provides

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.7.hg74691fb6f837
- noarch for f19+ and rhel7+, exclusivearch otherwise
- requires sqlite-devel

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.6.hg74691fb6f837
- sql -> SQL, rpmlint warning fixed

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.hg74691fb6f837
- buildarch: noarch

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.hg74691fb6f837
- description update
- added noarch to exclusivearch list

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.3.hg74691fb6f837
- golang license for 2012 installed

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.hg74691fb6f837
- exclusivearch as per golang
- debug_package nil

* Sun Oct 06 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.hg74691fb6f837
- Initial fedora package
