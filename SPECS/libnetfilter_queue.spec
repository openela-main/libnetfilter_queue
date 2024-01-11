%define libnfnetlink 1.0.1

Name:           libnetfilter_queue
Version:        1.0.5
Release:        1%{?dist}
Summary:        Netfilter queue userspace library
# Most files say GPLv2+, one says v2 only.
License:        GPLv2
URL:            http://netfilter.org
Source0:        http://netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2

Patch1:         0001-src-fix-IPv6-header-handling.patch

BuildRequires:  libnfnetlink-devel >= %{libnfnetlink}, pkgconfig, kernel-headers
BuildRequires:  autoconf, automake, libtool, libmnl-devel >= 1.0.3
BuildRequires: make

%description
libnetfilter_queue is a userspace library providing an API to packets that have
been queued by the kernel packet filter. It is is part of a system that
deprecates the old ip_queue / libipq mechanism.

libnetfilter_queue has been previously known as libnfnetlink_queue. 

%package        devel
Summary:        Netfilter queue userspace library
Requires:       %{name} = %{version}-%{release}, pkgconfig
Requires:	libnfnetlink-devel >= %{libnfnetlink}, kernel-headers

%description    devel
libnetfilter_queue is a userspace library providing an API to packets that have
been queued by the kernel packet filter. It is is part of a system that
deprecates the old ip_queue / libipq mechanism.

libnetfilter_queue has been previously known as libnfnetlink_queue.

%prep
%autosetup -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Aug 13 2021 Phil Sutter <psutter@redhat.com> - 1.0.5-1
- Rebase onto upstream version 1.0.5

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.0.2-20
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Apr 19 2021 Phil Sutter <psutter@redhat.com> - 1.0.2-19
- extra: use inet_ntop instead of inet_ntoa

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.0.2-18
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Paul Komkoff <i@stingr.net> - 1.0.2-1
- upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 17 2012 Paul P. Komkoff Jr <i@stingr.net> - 1.0.1-1
- upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug  4 2010 Paul P. Komkoff Jr <i@stingr.net> - 1.0.0-1
- new upstream version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar  7 2009 Paul P. Komkoff Jr <i@stingr.net> - 0.0.17-1
- upstream update

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 26 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.0.16-3
- fix patch/patch0
- depend on specific libnfnetlink version

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.16-2
- fix license tag

* Wed Jul 16 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.0.16-1
- new upstream version

* Fri Feb 22 2008 Paul P Komkoff Jr <i@stingr.net> - 0.0.15-4
- use system header instead of bundled one

* Fri Feb 22 2008 Paul P Komkoff Jr <i@stingr.net> - 0.0.15-3
- fix compilation with newer glibc/headers/whatever

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.15-2
- Autorebuild for GCC 4.3

* Tue Sep 18 2007 Paul P Komkoff Jr <i@stingr.net> - 0.0.15-1
- new upstream version

* Mon Mar 26 2007 Paul P Komkoff Jr <i@stingr.net> - 0.0.13-3
- own some directories

* Mon Mar 19 2007 Paul P Komkoff Jr <i@stingr.net> - 0.0.13-2
- fix source url
- add pkgconfig to -devel Requires

* Sat Mar 17 2007 Paul P Komkoff Jr <i@stingr.net> - 0.0.13-1
- Preparing for submission to fedora extras
