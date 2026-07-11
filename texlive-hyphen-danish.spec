%global tl_name hyphen-danish
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Danish hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/dkhyphen
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-danish.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Danish in T1/EC and UTF-8 encodings.

