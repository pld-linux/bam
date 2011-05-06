Summary:	Build system
Name:		bam
Version:	0.4.0
Release:	1
License:	zlib
Group:		Development/Building
Source0:	http://github.com/downloads/matricks/bam/%{name}-%{version}.tar.bz2
# Source0-md5:	f8b62ad553c3615a725a034df4fb4257
URL:		http://matricks.github.com/bam/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bam is a build system with the focus on being having fast build times
and flexiable build scripts. Instead of having a custom language it
uses Lua to describe the build steps. It's written in clean C and is
distrubuted under the liberal zlib licence. Available on many
platforms including but not limited to Linux, Mac OS X and Windows.

%prep
%setup -q

%build
./make_unix.sh %{rpmcflags}

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.txt license.txt
%attr(755,root,root) %{_bindir}/%{name}
