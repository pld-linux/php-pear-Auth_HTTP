%include	/usr/lib/rpm/macros.php
%define		_class		Auth
%define		_subclass	HTTP
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - HTTP authentication system using PHP
Summary(pl):	%{_pearname} - system uwierzytelniania HTTP przy u¿yciu PHP
Name:		php-pear-%{_pearname}
Version:	2.1.0
Release:	0.RC2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}RC2.tgz
# Source0-md5:	2f55b10ae0efb527c4c999ac1e0e8ed7
URL:		http://pear.php.net/package/Auth_HTTP/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Methods for creating an HTTP authentication system using PHP.

This class has in PEAR status: %{_status}.

%description -l pl
Metody do tworzenia systemu uwierzytelniania HTTP przy u¿yciu PHP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c -n %{name}-%{version}RC2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}RC2/%{_class}_%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
