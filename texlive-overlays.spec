%global tl_name overlays
%global tl_revision 57866

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.12
Release:	%{tl_revision}.1
Summary:	Incremental slides
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/overlays
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/overlays.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/overlays.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows to write presentations with incremental slides. It
does not presuppose any specific document class. Rather, it is a
lightweight alternative to full-fledged presentation classes like
beamer. The package requires xcolor, environ, and pgffor (from the pgf
bundle).

