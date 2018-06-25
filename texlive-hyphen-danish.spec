# revision 23085
# category TLCore
# catalog-ctan /language/hyphenation/dkhyphen
# catalog-date 2009-09-25 22:54:35 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-hyphen-danish
Version:	20180303
Release:	1
Summary:	Danish hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/dkhyphen
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-danish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Danish in T1/EC and UTF-8 encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-danish
%_texmf_language_def_d/hyphen-danish
%_texmf_language_lua_d/hyphen-danish

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-danish <<EOF
\%% from hyphen-danish:
danish loadhyph-da.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-danish
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-danish <<EOF
\%% from hyphen-danish:
\addlanguage{danish}{loadhyph-da.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-danish
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-danish <<EOF
-- from hyphen-danish:
	['danish'] = {
		loader = 'loadhyph-da.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-da.pat.txt',
		hyphenation = '',
	},
EOF


%changelog
* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090925-3
+ Revision: 767534
- Add workaround to rpm bug that broke hyphenation files
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090925-2
+ Revision: 759905
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090925-1
+ Revision: 718646
- texlive-hyphen-danish
- texlive-hyphen-danish
- texlive-hyphen-danish
- texlive-hyphen-danish

