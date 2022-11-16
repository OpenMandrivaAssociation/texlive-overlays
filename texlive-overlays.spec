Name:		texlive-overlays
Version:	57866
Release:	1
Summary:	Incremental slides
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/overlays
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/overlays.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/overlays.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows to write presentations with incremental
slides. It does not presuppose any specific document class.
Rather, it is a lightweight alternative to full-fledged
presentation classes like beamer. The package requires xcolor,
environ, and pgffor (from the pgf bundle).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/overlays
%doc %{_texmfdistdir}/doc/latex/overlays

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
