%include	/usr/lib/rpm/macros.php
%define		_class		Auth
%define		_subclass	HTTP
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - HTTP authentication system using PHP
Summary(pl):	%{_pearname} - system uwierzytelniania HTTP przy u¿yciu PHP
Name:		php-pear-%{_pearname}
Version:	2.1.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1f5bca97d0d0c76c68277b7561851b4a
URL:		http://pear.php.net/package/Auth_HTTP/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Auth_HTTP class provides methods for creating an HTTP
authentication system using PHP, that is similar to Apache's
realm-based .htaccess authentication.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa PEAR::Auth_HTTP dostarcza metod do stworzenia autentykacji HTTP
za pomoc± PHP, w sposób zlbi¿ony do bazuj±cej na .htaccess autoryzacji
Apache.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_class}_%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
