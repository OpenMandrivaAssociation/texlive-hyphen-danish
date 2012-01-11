# revision 23085
# category TLCore
# catalog-ctan /language/hyphenation/dkhyphen
# catalog-date 2009-09-25 22:54:35 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-hyphen-danish
Version:	20090925
Release:	2
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
\%\% from hyphen-danish:
danish loadhyph-da.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-danish <<EOF
\%\% from hyphen-danish:
\addlanguage{danish}{loadhyph-da.tex}{}{2}{2}
EOF
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
