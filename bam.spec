Summary:	Build system
Name:		bam
Version:	0.2.0
Release:	0.1
License:	zlib
Group:		Development/Building
Source0:	http://www.teeworlds.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	d4efe74591a73c1cec8b34d76ffd1049
URL:		http://teeworlds.com/trac/bam/browser/releases/
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
./make_unix.sh

%install
rm -rf $RPM_BUILD_ROOT

install -D src/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.txt license.txt
%attr(755,root,root) %{_bindir}/%{name}
