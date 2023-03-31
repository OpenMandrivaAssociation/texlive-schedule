Name:		texlive-schedule
Version:	51805
Release:	2
Summary:	Weekly schedules
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/schedule
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schedule.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schedule.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schedule.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Automatically format weekly schedules using LaTeX's picture
environment. It requires the packages calc and color. Its main
feature is the accuracy with which appointments are
represented: boxes drawn to represent a particular appointment
are accurate to the minute -- i.e., a 31-minute appointment
will have a box 1/30th longer than a 30-minute appointment. A
number of features are included to allow the user to customize
the output.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/schedule
%{_texmfdistdir}/tex/latex/schedule
%doc %{_texmfdistdir}/doc/latex/schedule

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
