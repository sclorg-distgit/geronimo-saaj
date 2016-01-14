%global pkg_name geronimo-saaj
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global spec_ver 1.3
%global spec_name geronimo-saaj_%{spec_ver}_spec

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.1
Release:          14.9%{?dist}
Summary:          Java EE: SOAP with Attachments API Package v1.3
License:          ASL 2.0 and W3C

URL:              http://geronimo.apache.org/
Source0:          http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{spec_name}/%{version}/%{spec_name}-%{version}-source-release.tar.gz
# Use parent pom files instead of unavailable 'genesis-java5-flava'
Patch1:           use_parent_pom.patch
BuildArch:        noarch

BuildRequires:    %{?scl_prefix_java_common}javapackages-tools
BuildRequires:    %{?scl_prefix_java_common}maven-local
BuildRequires:    %{?scl_prefix}geronimo-parent-poms
BuildRequires:    %{?scl_prefix}maven-resources-plugin
BuildRequires:    %{?scl_prefix}maven-surefire-provider-junit
BuildRequires:    %{?scl_prefix}geronimo-osgi-support



%description
Provides the API for creating and building SOAP messages. 

%package javadoc
Summary:          Javadoc for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.


%prep
%setup -q -n %{spec_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.conv && mv -f LICENSE.conv LICENSE
sed -i 's/\r//' LICENSE NOTICE
%patch1 -p0
%pom_remove_dep :geronimo-activation_1.1_spec

%mvn_file : %{pkg_name}
%mvn_alias : org.apache.geronimo.specs:geronimo-saaj_1.1_spec javax.xml.soap:saaj-api
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.1-14.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.1-14.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-14.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-14.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-14.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-14.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-14.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-14.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-14.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1-14
- Mass rebuild 2013-12-27

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 1.1-13
- Migrate away from mvn-rpmbuild (Resolves: #997499)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-12
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue Mar 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-11
- Replace local depmap with POM macro
- Resolves: rhbz#914030

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1-9
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Aug 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-8
- Fix license tag
- Remove dangling symlink
- Update to current guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.1-5
- Build with Maven 3.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 4 2010 Chris Spike <chris.spike@arcor.de> 1.1-3
- Added 'org.apache.geronimo.specs:geronimo-saaj_1.1_spec' to maven depmap

* Mon Aug 2 2010 Chris Spike <chris.spike@arcor.de> 1.1-2
- Consistently using 'rm' now
- Removed W3C from 'License:' field (XMLSchema.dtd not existent)

* Thu Jul 22 2010 Chris Spike <chris.spike@arcor.de> 1.1-1
- Initial version of the package
