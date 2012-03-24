%define		status		stable
%define		pearname	Auth_HTTP
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - HTTP authentication system using PHP
Summary(pl.UTF-8):	%{pearname} - system uwierzytelniania HTTP przy użyciu PHP
Name:		php-pear-%{pearname}
Version:	2.1.8
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	8a9f0ce15878a48e8a5d29ebea9f4c34
URL:		http://pear.php.net/package/Auth_HTTP
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear >= 4:1.0-8
Requires:	php-pear-Auth >= 1.2.0
Obsoletes:	php-pear-Auth_HTTP-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Auth_HTTP class provides methods for creating an HTTP
authentication system using PHP, that is similar to Apache's
realm-based .htaccess authentication.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Klasa PEAR::Auth_HTTP dostarcza metod do stworzenia uwierzytelniania
HTTP za pomocą PHP, w sposób zbliżony do opartego na .htaccess
uwierzytelniania w Apache.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Auth_HTTP/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Auth/*.php
