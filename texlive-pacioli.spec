Name:		texlive-pacioli
Version:	24947
Release:	1
Summary:	Fonts designed by Fra Luca de Pacioli in 1497
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/pacioli
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pacioli.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pacioli.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pacioli.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pacioli was a c.15 mathematician, and his font was designed
according to 'the divine proportion'. The font is uppercase
letters together with punctuation and some analphabetics; no
lowercase or digits. The Metafont source is distributed in a
.dtx file, together with LaTeX support.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/pacioli/cpclig.mf
%{_texmfdistdir}/fonts/source/public/pacioli/cpcpunct.mf
%{_texmfdistdir}/fonts/source/public/pacioli/cpcr10.mf
%{_texmfdistdir}/fonts/source/public/pacioli/cpcromanp.mf
%{_texmfdistdir}/fonts/source/public/pacioli/cpcromanu.mf
%{_texmfdistdir}/fonts/source/public/pacioli/cpcsl10.mf
%{_texmfdistdir}/fonts/source/public/pacioli/cpctitle.mf
%{_texmfdistdir}/fonts/tfm/public/pacioli/cpcr10.tfm
%{_texmfdistdir}/fonts/tfm/public/pacioli/cpcsl10.tfm
%{_texmfdistdir}/tex/latex/pacioli/ot1cpc.fd
%{_texmfdistdir}/tex/latex/pacioli/pacioli.sty
%{_texmfdistdir}/tex/latex/pacioli/t1cpc.fd
%doc %{_texmfdistdir}/doc/fonts/pacioli/README
%doc %{_texmfdistdir}/doc/fonts/pacioli/tryfont.ps
%doc %{_texmfdistdir}/doc/fonts/pacioli/tryfont.tex
#- source
%doc %{_texmfdistdir}/source/fonts/pacioli/pacioli.dtx
%doc %{_texmfdistdir}/source/fonts/pacioli/pacioli.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
