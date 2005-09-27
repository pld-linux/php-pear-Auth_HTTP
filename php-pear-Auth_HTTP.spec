%include	/usr/lib/rpm/macros.php
%define		_class		Auth
%define		_subclass	HTTP
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - HTTP authentication system using PHP
Summary(pl):	%{_pearname} - system uwierzytelniania HTTP przy u¿yciu PHP
Name:		php-pear-%{_pearname}
Version:	2.1.6
Release:	1.5
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d5209f0d1f1874e23b44fbfb397a2aa0
URL:		http://pear.php.net/package/Auth_HTTP
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear >= 4:1.0-8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Auth_HTTP class provides methods for creating an HTTP
authentication system using PHP, that is similar to Apache's
realm-based .htaccess authentication.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa PEAR::Auth_HTTP dostarcza metod do stworzenia uwierzytelniania
HTTP za pomoc± PHP, w sposób zbli¿ony do opartego na .htaccess
uwierzytelniania w Apache.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
