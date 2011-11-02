Name:		texlive-pacioli
Version:	20071010
Release:	1
Summary:	Fonts designed by Fra Luca de Pacioli in 1497
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/pacioli
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pacioli.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pacioli.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pacioli.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Pacioli was a c.15 mathematician, and his font was designed
according to 'the divine proportion'. The font is uppercase
letters together with punctuation and some analphabetics; no
lowercase or digits. The MetaFont source is distributed in a
.dtx file, together with LaTeX support.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_texmfdistdir}/doc/fonts/pacioli/tryfont.tex
#- source
%doc %{_texmfdistdir}/source/latex/pacioli/pacioli.dtx
%doc %{_texmfdistdir}/source/latex/pacioli/pacioli.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
