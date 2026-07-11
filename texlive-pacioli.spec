%global tl_name pacioli
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fonts designed by Fra Luca de Pacioli in 1497
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/pacioli
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pacioli.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pacioli.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pacioli.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Pacioli was a c.15 mathematician, and his font was designed according to
'the divine proportion'. The font is uppercase letters together with
punctuation and some analphabetics; no lowercase or digits. The Metafont
source is distributed in a .dtx file, together with LaTeX support.

