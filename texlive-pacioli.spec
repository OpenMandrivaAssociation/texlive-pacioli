# revision 24947
# category Package
# catalog-ctan /fonts/pacioli
# catalog-date 2011-06-16 21:20:53 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-pacioli
Version:	20180303
Release:	2
Summary:	Fonts designed by Fra Luca de Pacioli in 1497
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/pacioli
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pacioli.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pacioli.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pacioli.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110616-1
+ Revision: 758993
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20071010-2
+ Revision: 754615
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20071010-1
+ Revision: 719177
- texlive-pacioli
- texlive-pacioli
- texlive-pacioli
- texlive-pacioli

